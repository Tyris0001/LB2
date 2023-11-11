# Gleiche abgabe wie B3G da ich nicht verstehe was hier anders sein soll
<hr>

# Lernfeld B4G

## Kompetenz
Ich kann die Funktionen Map, Filter und Reduce einzeln auf Listen anwenden.

## Map, Filter und Reduce
Die Funktionen `map`, `filter` und `reduce` sind Funktionen der höheren Ordnung, die in Python häufig verwendet werden. Sie sind besonders nützlich, wenn Sie eine Liste von Elementen haben und eine neue Liste mit Elementen erstellen wollen, die auf der ursprünglichen Liste basieren. Sie können diese Funktionen auch verwenden, um die Elemente einer Liste zu filtern oder zu reduzieren.

### Map
Die Funktion `map` wendet eine Funktion auf jedes Element einer Liste an und gibt eine neue Liste mit den Ergebnissen zurück. Nehmen wir zum Beispiel an, wir haben eine Liste von Zahlen und wollen eine neue Liste mit den Quadraten dieser Zahlen erstellen. Wir können die Funktion `map` verwenden, um dies zu tun:

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]
```

### Filter
Die Funktion `filter` wendet eine Funktion auf jedes Element einer Liste an und gibt eine neue Liste mit den Elementen zurück, für die die Funktion `True` zurückgibt. Nehmen wir zum Beispiel an, wir haben eine Liste von Zahlen und wollen eine neue Liste mit den geraden Zahlen erstellen. Wir können die Funktion `filter` verwenden, um dies zu tun:

```python
numbers = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # Output: [2, 4]
```

### Reduce
Die Funktion `reduce` wendet eine Funktion auf jedes Element einer Liste an und gibt eine einzelne Zahl zurück. Nehmen wir zum Beispiel an, wir haben eine Liste von Zahlen und wollen die Summe dieser Zahlen berechnen. Wir können die Funktion `reduce` verwenden, um dies zu tun:

```python
from functools import reduce

numbers = [1, 2, 3, 4]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 10
```

## Codebeispiel
```python
from functools import reduce

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
sum = reduce(lambda x, y: x + y, numbers)
print(squares)  # Output: [1, 4, 9, 16]
print(even)  # Output: [2, 4]
print(sum)  # Output: 10
```
