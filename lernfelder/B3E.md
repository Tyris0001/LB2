# Lernfeld B3E

## Kompetenz
Ich kann Lambda-Ausdrücke verwenden, um den Programmfluss zu steuern, z.B. durch Sortieren von Listen basierend auf benutzerdefinierten Kriterien.

## Verwendung von Lambda-Ausdrücken in BuxPay

In meinem BuxPay-Code verwende ich Lambda-Ausdrücke, um den Programmfluss zu steuern und Listen basierend auf benutzerdefinierten Kriterien zu sortieren. Hier sind Beispiele für die Anwendung dieser Kompetenz in meinem Code:

**Verwendung von Lambda-Ausdrücken zur Sortierung:**
```python
@buxpay_blueprint.route('/payments/create', methods=['POST'])
def payments_create():
    # ...

    invoices = filter(None, map(create_invoice, app.buxpay_app.clients))
    invoices = list(invoices)

    # Sortieren der Rechnungen nach dem Erstellungsdatum
    invoices.sort(key=lambda x: x.created)
```
Im Endpunkt `payments_create` verwende ich einen Lambda-Ausdruck, um die Liste der Rechnungen nach dem Erstellungsdatum zu sortieren.

**Verwendung von Lambda-Ausdrücken in `map` und `filter`:**
```python
@buxpay_blueprint.route('/higher-order-example', methods=['GET'])
def higher_order_example():
    numbers = [1, 2, 3, 4, 5]
    square = lambda x: x ** 2
    squared_numbers = list(map(square, numbers))

    return jsonify({"data": squared_numbers})
```
Im Endpunkt `higher_order_example` verwende ich einen Lambda-Ausdruck in der `map`-Funktion, um eine Funktion auf jedes Element einer Liste anzuwenden und eine neue Liste mit den Quadraten der Zahlen zu erstellen.

Die Verwendung von Lambda-Ausdrücken ermöglicht es mir, benutzerdefinierte Kriterien und Funktionen in meinen Code einzuführen, um den Programmfluss zu steuern und Listen basierend auf diesen Kriterien zu sortieren oder zu transformieren. Dies erhöht die Flexibilität und Funktionalität meiner Funktionen und trägt zur Verbesserung der Codeeffizienz bei.