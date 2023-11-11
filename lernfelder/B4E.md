# Lernfeld B4E

## Kompetenz
Ich kann Map, Filter und Reduce verwenden, um komplexe Datenverarbeitungsaufgaben zu lösen, wie z.B. die Aggregation von Daten oder die Transformation von Datenstrukturen.

## Anwendung von Map und Filter in BuxPay

In meinem BuxPay-Code verwende ich die Funktionen `map` und `filter` zur Datenverarbeitung in einem Flask-Endpunkt. Hier ist ein Beispiel für die Anwendung dieser Kompetenz in meinem Code:

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

Im Endpunkt `payments_create` verwende ich die `map`- und `filter`-Funktionen, um eine Liste von Rechnungen (`invoices`) zu erstellen. Zuerst wende ich `map` auf die `create_invoice`-Funktion auf jede Client-Instanz in `app.buxpay_app.clients` an, um eine Liste von möglichen Rechnungen zu erstellen. Dann verwende ich `filter`, um alle `None`-Elemente aus dieser Liste zu entfernen, da nicht jede Anfrage erfolgreich ist.

Das Ergebnis ist eine Liste von Rechnungen, die erfolgreich erstellt wurden (`invoices`). Diese Technik ermöglicht die effiziente Verarbeitung von Daten und die Erstellung einer Liste von Rechnungen, die anschließend weiterverarbeitet wird.

Die Anwendung von `map` und `filter` in diesem Beispiel erleichtert die Erstellung von Rechnungen und trägt zur Verbesserung der Codeeffizienz und -qualität bei.

### Verwendung von `reduce` zur Datenaggregation:
```python
@buxpay_blueprint.route('/reduce-example', methods=['GET'])
def reduce_example():
    numbers = [1, 2, 3, 4, 5]
    product = lambda x, y: x * y
    result = reduce(product, numbers)

    return jsonify({"data": result})
```
Im Endpunkt `reduce_example` verwende ich die `reduce`-Funktion, um eine Funktion (`product`) auf jedes Paar von Elementen in einer Liste (`numbers`) anzuwenden und das Endergebnis zu berechnen. Hier berechne ich das Produkt aller Zahlen in der Liste.

Die Anwendung von `map`, `filter` und `reduce` in meinem Code ermöglicht es mir, komplexe Datenverarbeitungsaufgaben zu lösen, Datenstrukturen zu transformieren und Daten zu aggregieren. Dies verbessert die Effizienz und Funktionalität meiner Funktionen und trägt zur Verbesserung der Codequalität bei.