# Lernfeld B1G

## Kompetenz
Ich kann ein Algorithmus erklären

## Algorithmen verstehen
Ein Algorithmus ist eine Liste von Schritten zur Lösung einer Aufgabe. In Python folgt ein Programm den Schritten eines Algorithmus, um eine Aufgabe zu erledigen. Um zum Beispiel die größte Zahl in einer Liste zu finden, können wir einen Algorithmus verwenden.

## Codebeispiel

```python
@buxpay_blueprint.route('/procedural-example', methods=['GET'])
def procedural_example():
    result = 0
    for num in range(1, 11):
        result += num

    return jsonify({"result": result})
```

In meinem BuxPay-Code gibt es mehrere Beispiele für die Anwendung von Algorithmen und Schritten zur Lösung von Aufgaben. Hier ist eine Liste von Fällen, in denen diese Kompetenz in meinem BuxPay-Code vorhanden ist:

1. **Flask-Endpunkte als Algorithmen:**
   - Die verschiedenen Flask-Endpunkte in meinem BuxPay-Code sind Algorithmen, die Schritte zur Lösung bestimmter Aufgaben definieren. Zum Beispiel der Endpunkt `payments_create`, der Schritte zur Erstellung von Zahlungsinformationen definiert.

2. **Verwendung von Funktionen als Schritten in Algorithmen:**
   - In meiner Klasse `BuxPayApp` werden Funktionen wie `load_json`, `save_json`, `load_clients`, `save_clients`, `load_invoices`, `save_invoices`, `cleanup_paid_transactions`, `get_csrf_token` und `create_gamepass` verwendet, um bestimmte Schritte in den Algorithmen auszuführen.

3. **Anwendung von funktionalem Programmieren:**
   - Die Endpunkte `lambda-example`, `higher-order-example`, `reduce-example`, `filter-example` und `functional-example` demonstrieren die Anwendung von Algorithmen und Schritten unter Verwendung funktionaler Programmierkonzepte, um Aufgaben wie Mapping, Filtern und Reduzieren von Daten durchzuführen.

4. **Prozedurale Programmierung:**
   - Der Endpunkt `procedural-example` zeigt einen prozeduralen Algorithmus, der die Summe von Zahlen von 1 bis 10 berechnet. Dies ist ein Beispiel für die Anwendung von Schritten zur Lösung einer Aufgabe in einer prozeduralen Programmierweise.

