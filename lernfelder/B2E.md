# Lernfeld B2E

## Kompetenz
Ich kann Funktionen als Objekte und Argumente verwenden, um komplexe Aufgaben zu lösen, einschließlich der Anwendung von Closures.

## Verwendung von Funktionen als Objekte in BuxPay

In meinem BuxPay-Code verwende ich Funktionen als Objekte und Argumente, um komplexe Aufgaben zu lösen. Hier sind Beispiele für die Anwendung dieser Kompetenz in meinem Code:

**Verwendung von Funktionen als Objekten:**
```python
class BuxPayApp:
    # ...

    def load_json(self, filepath):
        """
        Load json file
        :param filepath:
        :return:
        """
        with open(filepath, "r") as file:
            return json.load(file)
```
In der Methode `load_json` meiner Klasse `BuxPayApp` wird die Funktion `open` als Objekt verwendet, um eine JSON-Datei zu laden.

**Verwendung von Funktionen als Argumenten:**
```python
@buxpay_blueprint.route('/functional-example', methods=['GET'])
def functional_example():
    numbers = list(range(1, 11))
    sum_of_numbers = sum(numbers)

    return jsonify({"result": sum_of_numbers})
```
Der Endpunkt `functional-example` akzeptiert die Funktion `sum` als Argument, um die Summe einer Liste von Zahlen zu berechnen.

**Anwendung von Closures:**
```python
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
```
Im Endpunkt `payments_create` wird die Funktion `create_invoice` als Closure verwendet, um eine spezifische Aufgabe innerhalb des Endpunkts auszuführen.

Die Verwendung von Funktionen als Objekten und Argumenten ermöglicht es, komplexe Aufgaben in meinen BuxPay-Code zu lösen und bietet Flexibilität und Wiederverwendbarkeit bei der Implementierung von Algorithmen und Funktionen. Dies trägt zur Verbesserung der Codeeffizienz und -lesbarkeit bei.