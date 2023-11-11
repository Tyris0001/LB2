# Lernfeld B1G

## Kompetenz
Ich kann ein Algorithmus erklären

## Algorithmen verstehen
Ein Algorithmus ist eine Liste von Schritten zur Lösung einer Aufgabe. In Python folgt ein Programm den Schritten eines Algorithmus, um eine Aufgabe zu erledigen. Um zum Beispiel die größte Zahl in einer Liste zu finden, können wir einen Algorithmus verwenden.

## Codebeispiel

```python
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

numbers = [4, 2, 8, 6]
biggest_number = find_max(numbers)
```

Dieser Algorithmus geht Schritt für Schritt vor und findet die größte Zahl in einer gegebenen Liste. In Python schreiben wir diesen Algorithmus mit einer Funktion. Die Funktion durchläuft jede Zahl, vergleicht sie und merkt sich die größte Zahl. So weiß der Computer, wie er die größte Zahl in einer Liste mit diesem Algorithmus finden kann.