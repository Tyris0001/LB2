# Lernfeld B4G

## Kompetenz
Ich kann die Funktionen Map, Filter und Reduce einzeln auf Listen anwenden.

## Anwendung von Map, Filter und Reduce in BuxPayApp

In meinem BuxPay-Code gibt es Beispiele für die Anwendung der Funktionen `map`, `filter` und `reduce` zur Lösung von Datenverarbeitungsaufgaben. Hier sind einige Beispiele für die Anwendung dieser Funktionen:

### Anwendung von `map`:

#### Beispiel 1: Quadratwurzeln berechnen
```python
@buxpay_blueprint.route('/map-example', methods=['GET'])
def map_example():
    numbers = [1, 4, 9, 16, 25]
    square_root = lambda x: x ** 0.5
    square_root_values = list(map(square_root, numbers))
    return jsonify({"data": square_root_values})
```

In diesem Beispiel wird die `map`-Funktion verwendet, um die Quadratwurzeln von Zahlen in der Liste `numbers` zu berechnen.

### Anwendung von `filter`:

#### Beispiel 2: Filtern von geraden Zahlen
```python
@buxpay_blueprint.route('/filter-example', methods=['GET'])
def filter_example():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_even = lambda x: x % 2 == 0
    even_numbers = list(filter(is_even, numbers))
    return jsonify({"data": even_numbers})
```

In diesem Beispiel wird die `filter`-Funktion verwendet, um nur gerade Zahlen aus der Liste `numbers` herauszufiltern.

### Anwendung von `reduce`:

#### Beispiel 3: Berechnung des Produkts aller Zahlen
```python
@buxpay_blueprint.route('/reduce-example', methods=['GET'])
def reduce_example():
    numbers = [1, 2, 3, 4, 5]
    product = lambda x, y: x * y
    result = reduce(product, numbers)
    return jsonify({"data": result})
```

In diesem Beispiel wird die `reduce`-Funktion verwendet, um das Produkt aller Zahlen in der Liste `numbers` zu berechnen.

Die Anwendung von `map`, `filter` und `reduce` in meinem BuxPay-Code ermöglicht die Verarbeitung von Daten auf effiziente Weise und ist ein wichtiger Bestandteil der Datenverarbeitungsfähigkeiten in Python. Diese Funktionen werden verwendet, um Daten zu transformieren, zu filtern und zu aggregieren, was die Code-Wiederverwendbarkeit und -Lesbarkeit erhöht.