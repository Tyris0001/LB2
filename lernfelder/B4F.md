# Lernfeld B4F

## Kompetenz
Ich kann Map, Filter und Reduce kombiniert verwenden, um Daten zu verarbeiten und zu manipulieren, die komplexere Transformationen erfordern.

## Anwendung von Map, Filter und Reduce in BuxPayApp

In meinem BuxPay-Code gibt es Beispiele für die kombinierte Anwendung der Funktionen `map`, `filter` und `reduce`, um Daten zu verarbeiten und komplexe Transformationen durchzuführen. Hier sind einige Beispiele für die Anwendung dieser Funktionen:

### Beispiel: Kombinierte Anwendung von `map`, `filter` und `reduce`

```python
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
```

In diesem Beispiel werden Transaktionsdaten verarbeitet, indem zuerst Transaktionen für einen bestimmten Benutzer gefiltert werden. Dann werden die Beträge aus den gefilterten Transaktionen extrahiert, und schließlich wird die Gesamtsumme der Beträge mithilfe von `reduce` berechnet.

Die kombinierte Anwendung von `map`, `filter` und `reduce` ermöglicht komplexe Datenverarbeitungsaufgaben, bei denen Daten transformiert, gefiltert und aggregiert werden müssen. Diese Fähigkeit ist entscheidend für die effiziente Verarbeitung großer Datenmengen und trägt zur Verbesserung der Code-Wiederverwendbarkeit und -Lesbarkeit bei.