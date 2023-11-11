# Lernfeld B3G

## Kompetenz
Ich kann einfache Lambda-Ausdrücke schreiben, die eine einzelne Operation durchführen, z.B. das Quadrieren einer Zahl oder das Konvertieren eines Strings in Großbuchstaben.

## Lambda-Ausdrücke
Lambda-Ausdrücke in Python sind eine leistungsstarke Funktion, mit der Sie kleine, unbenannte Funktionen im Handumdrehen erstellen können. Sie sind besonders nützlich, wenn Sie eine einfache Funktion für einen kurzen Zeitraum benötigen und sie nicht formal definieren wollen. Lambdas werden typischerweise verwendet, um einzelne Operationen oder Aktionen durchzuführen, z. B. arithmetische Berechnungen oder String-Manipulationen.
<br><br>
Wenn Sie zum Beispiel eine Zahl quadrieren wollen, können Sie einen Lambda-Ausdruck wie folgt schreiben:
```python
square = lambda x: x ** 2
print(square(4))  # Output: 16
```
Für die Manipulation von Text, z. B. die Konvertierung in Großbuchstaben, können Sie schreiben:
```python
uppercase = lambda s: s.upper()
print(uppercase('hello'))  # Output: HELLO
```
