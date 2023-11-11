from flask import Flask, jsonify, request, send_from_directory, render_template, Blueprint
import uuid
import json
import threading
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as htmlparser
import requests
import random
from classes.client import Client
from classes.invoice import Invoice
from functools import reduce

app = Flask(__name__, template_folder='./templates/', static_folder='./static/')


class BuxPayApp:
    def __init__(self):
        self.clients = []
        self.load_clients()
        self.load_invoices()
        threading.Thread(target=self.cleanup_paid_transactions).start()

    def load_json(self, filepath):
        """
        Load json file
        :param filepath:
        :return:
        """
        with open(filepath, "r") as file:
            return json.load(file)

    def save_json(self, filepath, data):
        """
        Save json file
        :param filepath:
        :param data:
        :return:
        """
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

    def load_clients(self):
        try:
            data = self.load_json("./buxpay/main.json")
            self.clients = [Client.from_json(client_data) for client_data in data.get("clients", [])]
        except FileNotFoundError:
            pass

    def save_clients(self):
        data = {"clients": [client.to_json() for client in self.clients]}
        self.save_json("./buxpay/main.json", data)

    def load_invoices(self):
        try:
            data = self.load_json("./buxpay/main.json")
            for client_data in data.get("clients", []):
                client = next((c for c in self.clients if c.username == client_data.get("username")), None)
                if client:
                    invoices = [Invoice.from_json(invoice_data) for invoice_data in client_data.get("invoices", [])]
                    client.set_invoices(invoices)

        except FileNotFoundError:
            pass

    def save_invoices(self):
        data = {"clients": []}
        for client in self.clients:
            client_data = client.to_json()
            client_data["invoices"] = [invoice.to_json() for invoice in client.invoices]
            data["clients"].append(client_data)
        self.save_json("./buxpay/main.json", data)

    def cleanup_paid_transactions(self):
        while True:
            current_time = datetime.now()
            for client in self.clients:
                client.remove_expired_invoices(current_time)
            self.save_clients()
            time.sleep(3600)

    def get_all_invoices(self):
        return [client.invoices for client in self.clients]

    def get_unpaid_invoices(self, client):
        # get client invoices
        unpaid_invoices = filter(lambda invoice: invoice.status == "unpaid", self.get_all_invoices())
        return unpaid_invoices
    def get_csrf_token(self, user_cookies):
        """
        Get the CSRF token of the authenticated cookie.
        :param user_cookies:
        :return:
        """
        response = requests.get("https://www.roblox.com/home", cookies={'.ROBLOSECURITY': user_cookies['cookie']})
        soup = htmlparser(response.text, "html.parser")
        csrf_tag = soup.find("meta", {"name": "csrf-token"})
        return csrf_tag["data-token"] if csrf_tag else None

    def create_gamepass(self, price, user_cookie):
        """
        Create a gamepass
        :param price:
        :param user_cookie:
        :return:
        """
        csrf_token = self.get_csrf_token(user_cookie)
        headers = {"x-csrf-token": csrf_token}
        data = {"Name": str(uuid.uuid4()), "Description": None, "UniverseId": user_cookie["universe"], "File": None}
        response = requests.post("https://apis.roblox.com/game-passes/v1/game-passes", headers=headers, data=data,
                                 cookies={'.ROBLOSECURITY': user_cookie['cookie']})

        return response


buxpay_blueprint = Blueprint('buxpay', __name__)


@buxpay_blueprint.route('/payments/create', methods=['POST'])
def payments_create():
    uid = str(uuid.uuid4()).split("-")[0]

    def create_invoice(client):
        user_cookie = random.choice(client.cookies)
        response = app.buxpay_app.create_gamepass(500, user_cookie)

        if not isinstance(response, requests.Response) or response.status_code != 200:
            return None

        try:
            gamepass_id = response.json()["gamePassId"]
            now = datetime.now()
            return Invoice(uid, 500, "unpaid", gamepass_id, now)
        except (json.JSONDecodeError, KeyError):
            return None

    invoices = filter(None, map(create_invoice, app.buxpay_app.clients))
    invoices = list(invoices)

    for invoice in invoices:
        for client in app.buxpay_app.clients:
            if invoice:
                client.add_invoice(invoice)

    app.buxpay_app.save_invoices()

    return jsonify({"ok": True, "data": {"uid": str(uid), "price": 500, "status": "unpaid"}}), 200


@buxpay_blueprint.route('/')
def index():
    return render_template('purchase.html')


@buxpay_blueprint.route('/static/<file_type>.wav')
def static_files(file_type):
    return send_from_directory('./static', f'{file_type}.wav', mimetype='audio/wav')


@buxpay_blueprint.route('/download/<invoiceid>')
def download_invoice(invoiceid):
    if str(invoiceid) in app.buxpay_app.purchase_tokens:
        threading.Thread(target=lambda: app.buxpay_app.remove_token(invoiceid)).start()
        return send_from_directory('templates/', 'macro.zip', mimetype='application/zip')
    return render_template("notfound.html")


@buxpay_blueprint.route('/invoices/<invoiceid>')
def invoices(invoiceid):
    try:
        invoice_info = requests.get("http://localhost:443/payments/info",
                                    json={"api_key": "inf", "uid": invoiceid}).json()
        if invoice_info["data"]["status"] == "paid":
            gamepass = invoice_info["data"]["gamepass"]
            rbx = format(invoice_info["data"]["price"], ",")
            return render_template('paid.html', TIMESTRING=invoice_info["data"]["created"],
                                   ROBUXSTRING=f"{rbx} Robux",
                                   DOWNLOAD_URL=f"http://localhost:443/download/{invoiceid}")
        else:
            gamepassid = invoice_info["data"]["gamepass"]
            payload = {
                "data": f"https://roblox.com/game-pass/{gamepassid}",
                "config": {
                    "body": "circle-zebra-vertical",
                    "eye": "frame13",
                    "eyeBall": "ball15",
                    "erf1": [],
                    "erf2": [],
                    "erf3": [],
                    "brf1": [],
                    "brf2": [],
                    "brf3": [],
                    "bodyColor": "#FFFFFF",
                    "bgColor": "#1D1E28",
                    "eye1Color": "#FFFFFF",
                    "eye2Color": "#FFFFFF",
                    "eye3Color": "#FFFFFF",
                    "eyeBall1Color": "#FFFFFF",
                    "eyeBall2Color": "#FFFFFF",
                    "eyeBall3Color": "#FFFFFF",
                    "gradientColor1": "#FFFFFF",
                    "gradientColor2": "#FFFFFF",
                    "gradientType": "linear",
                    "gradientOnEyes": "true",
                    "logo": "",
                    "logoMode": "default"
                },
                "size": 1000,
                "download": "imageUrl",
                "file": "png"
            }
            rss = requests.post("https://api.qrcode-monkey.com/qr/custom", json=payload).json()
            rl = rss["imageUrl"]
            rbx = invoice_info["data"]["price"]
            rbx = format(rbx, ",")
            return render_template('example.html', GAMEPASSLINK=f"https://roblox.com/game-pass/{gamepassid}",
                                   USERCREATED=invoice_info["data"]["username"],
                                   TIMESTRING=invoice_info["data"]["created"], ROBUXSTRING=f"{rbx} Robux",
                                   QRCODELINK=f"https://{rl}")
    except Exception as e:
        return jsonify({"ok": False, "data": {"error": str(e)}}), 400


@buxpay_blueprint.route('/payments/info', methods=['GET', 'POST'])
def payments_info():
    try:
        invoice_data = request.json
        main_json = app.buxpay_app.load_json(f"./buxpay/main.json")
        invoice = next((invoice for client in main_json["clients"] for invoice in client["invoices"] if
                        invoice["uid"] == invoice_data["uid"]), None)
        if invoice:
            invoice["username"] = next(client["username"] for client in main_json["clients"])
            return jsonify({"ok": True, "data": invoice}), 200
        else:
            return jsonify({"ok": False, "data": {"message": "Failed to find invoice."}}), 400
    except Exception as e:
        return jsonify({"ok": False, "data": {"error": str(e)}}), 400


@buxpay_blueprint.route('/static/favicon.ico')
def favicon():
    return send_from_directory('./static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@buxpay_blueprint.route('/clients/<rd>', methods=['GET'])
def clients(rd):
    if rd == "info":
        api_key = request.args.get("api_key")
        clients = app.buxpay_app.clients
        client_data = next((client for client in clients if client.api_key == api_key), None)
        if client_data:
            return jsonify({"ok": True, "data": client_data.to_json()}), 200
        else:
            return jsonify({"ok": False, "data": {"message": "Invalid API key."}}), 400


## useless endpoints 😢

@buxpay_blueprint.route('/immutable-example', methods=['GET'])
def immutable_example():
    immutable_data = (1, 2, 3)
    return jsonify({"data": immutable_data})


@buxpay_blueprint.route('/mutable-example', methods=['GET'])
def mutable_example():
    mutable_data = [1, 2, 3]
    mutable_data[0] = 5
    return jsonify({"data": mutable_data})


@buxpay_blueprint.route('/lambda-example', methods=['GET'])
def lambda_example():
    square = lambda x: x ** 2
    result = square(5)
    return jsonify({"data": result})


@buxpay_blueprint.route('/higher-order-example', methods=['GET'])
def higher_order_example():
    numbers = [1, 2, 3, 4, 5]
    square = lambda x: x ** 2
    squared_numbers = list(map(square, numbers))
    return jsonify({"data": squared_numbers})

@buxpay_blueprint.route('/combined-example', methods=['GET'])
def combined_example():
    # Eine Liste von Transaktionen mit Beträgen
    transactions = [
        {"user_id": 1, "amount": 100},
        {"user_id": 2, "amount": 200},
        {"user_id": 1, "amount": 50},
        {"user_id": 3, "amount": 300},
        {"user_id": 2, "amount": 150},
    ]

    # Zuerst filtern wir die Transaktionen für einen bestimmten Benutzer (z.B., Benutzer 1)
    filtered_transactions = filter(lambda trans: trans["user_id"] == 1, transactions)

    # Dann extrahieren wir die Beträge aus den gefilterten Transaktionen
    amounts = map(lambda trans: trans["amount"], filtered_transactions)

    # Schließlich berechnen wir die Gesamtsumme der Beträge
    total_amount = reduce(lambda x, y: x + y, amounts, 0)

    return jsonify({"total_amount": total_amount})

@buxpay_blueprint.route('/reduce-example', methods=['GET'])
def reduce_example():
    numbers = [1, 2, 3, 4, 5]
    product = lambda x, y: x * y
    result = reduce(product, numbers)
    return jsonify({"data": result})

@buxpay_blueprint.route('/filter-example', methods=['GET'])
def filter_example():
    numbers = [1, 2, 3, 4, 5]
    is_even = lambda x: x % 2 == 0
    even_numbers = list(filter(is_even, numbers))
    return jsonify({"data": even_numbers})

@buxpay_blueprint.route('/functional-example', methods=['GET'])
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return jsonify({"data":fibonacci(n-1) + fibonacci(n-2)})

@buxpay_blueprint.route('/procedural-example', methods=['GET'])
def procedural_example():
    result = 0
    for num in range(1, 11):
        result += num

    return jsonify({"result": result})

@buxpay_blueprint.route('/functional-example', methods=['GET'])
def functional_example():
    numbers = list(range(1, 11))
    sum_of_numbers = sum(numbers)

    return jsonify({"result": sum_of_numbers})


app.register_blueprint(buxpay_blueprint, url_prefix='/')

if __name__ == "__main__":
    app.buxpay_app = BuxPayApp()
    app.run(host="0.0.0.0", port=443)
