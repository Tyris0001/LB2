# Lernfeld B1F

## Kompetenz
Ich kann Algorithmen in funktionale Teilstücke aufteilen


## Implementation

Die Zerlegung von Algorithmen in funktionale Komponenten ist eine grundlegende Fähigkeit in der Programmierung, die es ermöglicht, den Code modularer, verständlicher und wartbarer zu gestalten. In Python beinhaltet dieser Prozess die Identifizierung verschiedener Abschnitte des Algorithmus, die separate Aufgaben erfüllen, und die anschließende Implementierung dieser Aufgaben als Funktionen.

Eine Funktion in Python wird mit dem Schlüsselwort def definiert, gefolgt von einem Funktionsnamen, Klammern, die Parameter enthalten können, und einem Doppelpunkt. Der Körper der Funktion enthält den Code, der eine Aufgabe ausführt. Durch die Kapselung spezifischer Funktionalitäten in Funktionen kann jeder Teil des Algorithmus unabhängig getestet und debuggt werden, was eine sauberere und effizientere Codeentwicklung fördert.

## Code Beispiel
```python
def find_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def find_min_max(numbers):
    min_number = find_min(numbers)
    max_number = find_max(numbers)
    return min_number, max_number

numbers = [4, 2, 8, 6]
result = find_min_max(numbers)
```

