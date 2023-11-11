# Lernfeld A1F

## Kompetenz
Ich kann das Konzept von *immutable values* erläutern und dazu Beispiele anwenden. Somit kann ich dieses Konzept funktionaler Programmierung im Unterschied zu anderen Programmiersprachen erklären (z.Bsp. im Vergleich zu referenzierten Objekten)

# Unveränderliche Werte und ihre Rolle verstehen

In der Programmierung gibt es ein Konzept, das als "unveränderliche Werte" bekannt ist. Das bedeutet, dass ein Wert, sobald er erstellt wurde, nicht mehr geändert werden kann. Es ist wie ein Blatt Papier, auf dem etwas geschrieben steht; man kann die Worte nicht löschen oder ändern. In der funktionalen Programmierung ist dieses Konzept wichtig, weil es die Dinge einfach und vorhersehbar macht.

Bei einigen anderen Programmierstilen hingegen können sich die Werte im Laufe der Zeit ändern, wie bei einer Tafel, auf der man löschen und neue Dinge schreiben kann. Dies ist häufig bei der objektorientierten Programmierung mit Objekten der Fall, die ihre Daten ändern können.

## Codebeispiel

```python
@buxpay_blueprint.route('/immutable-example', methods=['GET'])
def immutable_example():
    immutable_data = (1, 2, 3)
    return jsonify({"data": immutable_data})


@buxpay_blueprint.route('/mutable-example', methods=['GET'])
def mutable_example():
    mutable_data = [1, 2, 3]
    mutable_data[0] = 5
    return jsonify({"data": mutable_data})
```