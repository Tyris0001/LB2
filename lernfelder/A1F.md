# Lernfeld A1E

## Kompetenz
Ich kann aufzeigen, wie Probleme in den verschiedenen Programmierkonzepten (Objektorientierte Programmierung - OO, prozedurale Programmierung und funktionale Programmierung) gelöst werden und diese miteinander vergleichen.

## Objektorientierte Programmierung (OO)

In meinem BuxPay-Code gibt es mehrere Beispiele für die Anwendung von objektorientierter Programmierung (OO) zur Lösung von Problemen:

**Client- und Invoice-Klassen:**
```python
class Client:
    # ...

class Invoice:
    # ...
```

Die Klassen `Client` und `Invoice` sind Beispiele für die Verwendung von OO, um Daten und Verhalten zu kapseln und zu organisieren. Diese Klassen repräsentieren Entitäten in meinem BuxPay-System.

**Methoden in der BuxPayApp-Klasse:**
```python
class BuxPayApp:
    # ...

    def load_clients(self):
        # ...

    def save_clients(self):
        # ...
```

In der `BuxPayApp`-Klasse werden verschiedene Methoden verwendet, um Aufgaben im Zusammenhang mit den Clients und Rechnungen auszuführen. Diese Methoden sind Teil der OO-Struktur des Codes.

## Prozedurale Programmierung

Die prozedurale Programmierung ist ebenfalls in meinem BuxPay-Code präsent. Hier ist ein Beispiel:

**Prozedurales Beispiel:**
```python
@buxpay_blueprint.route('/procedural-example', methods=['GET'])
def procedural_example():
    result = 0
    for num in range(1, 11):
        result += num

    return jsonify({"result": result})
```

Dieses Beispiel zeigt einen prozeduralen Algorithmus, der die Summe von Zahlen von 1 bis 10 berechnet. In diesem Fall werden Schritte nacheinander ausgeführt, um das gewünschte Ergebnis zu erzielen.

## Funktionale Programmierung

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

    for invoice in invoices:
        for client in app.buxpay_app.clients:
            if invoice:
                client.add_invoice(invoice)

    app.buxpay_app.save_invoices()

    return jsonify({"ok": True, "data": {"uid": str(uid), "price": 500, "status": "unpaid"}}), 200

```