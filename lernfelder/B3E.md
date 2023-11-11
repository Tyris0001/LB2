# Lernfeld B3E

## Kompetenz
Ich kann Lambda-Ausdrücke verwenden, um den Programmfluss zu steuern, z.B. durch Sortieren von Listen basierend auf benutzerdefinierten Kriterien.

## Lambda-Ausdrücke zur Steuerung des Programmflusses
Lambda-Ausdrücke in Python sind eine leistungsstarke Funktion, mit der Sie kleine, unbenannte Funktionen im Handumdrehen erstellen können. Sie sind besonders nützlich, wenn Sie eine einfache Funktion für einen kurzen Zeitraum benötigen und sie nicht formal definieren wollen. Lambdas werden typischerweise verwendet, um einzelne Operationen oder Aktionen durchzuführen, z. B. arithmetische Berechnungen oder String-Manipulationen.

## Codebeispiel
```python
numbers = [4, 2, 8, 6]
numbers.sort(key=lambda x: x % 2 == 0)
print(numbers)  # Output: [3, 1, 4, 2]
```
