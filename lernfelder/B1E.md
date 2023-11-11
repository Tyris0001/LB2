# Lernfeld B1E

# Kompetenz
Ich kann Funktionen in zusammenhängende Algorithmen implementieren

## Implementierung von Funktionen in kohärenten Algorithmen

In Python ist eine Funktion ein Codeblock, der eine bestimmte Aufgabe erfüllt. Wir können Funktionen verwenden, um Algorithmen zu erstellen, die größere Aufgaben lösen, indem sie in kleinere Schritte zerlegt werden. Nehmen wir zum Beispiel an, wir wollen die kleinste und größte Zahl in einer Liste finden.

### Codebeispiel
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

# Now use the function
numbers = [4, 2, 8, 6]
result = find_min_max(numbers)
```
