# Lernfeld B2F

## Kompetenz
Ich kann Funktionen als Argumente für andere Funktionen verwenden und dadurch höherwertige Funktionen erstellen.

## Funktionen als Argumente
Die Verwendung von Funktionen als Argumente für andere Funktionen ist ein Kernkonzept in Python, das die Erstellung von Funktionen höherer Ordnung ermöglicht. Funktionen höherer Ordnung nehmen entweder Funktionen als Argumente an, geben sie zurück oder beides. Dieses Konzept ist in funktionalen Programmierparadigmen von entscheidender Bedeutung und wird in Python ausgiebig für Operationen wie Sortieren, Filtern und die Anwendung von Funktionen auf Iterables verwendet.

```python
def apply_twice(func, value):
    return func(func(value))
def add_five(x):
    return x + 5

result = apply_twice(add_five, 10)
print(result)  # Output: 20

def process_list(func, lst):
    return [func(item) for item in lst]

numbers = [-2, -1, 0, 1, 2]
processed_numbers = process_list(abs, numbers)
print(processed_numbers)  # Output: [2, 1, 0, 1, 2]
```


