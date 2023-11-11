# Lernfeld B2G

## Kompetenz
Ich kann Funktionen als Objekte behandeln und diese in Variablen speichern und weitergeben.

## Funktionen als Objekte
In Python sind Funktionen Objekte erster Klasse, das heißt, sie können wie jedes andere Objekt behandelt werden. Diese Eigenschaft ermöglicht leistungsfähige und flexible Codierungsmuster. So können Funktionen beispielsweise Variablen zugewiesen, in Datenstrukturen gespeichert, als Argumente an andere Funktionen übergeben und sogar von Funktionen zurückgegeben werden. Diese Flexibilität erleichtert die Erstellung von Funktionen höherer Ordnung, die andere Funktionen als Parameter akzeptieren oder zurückgeben können, was die Komposition von Funktionen und die Verwendung von Funktionsfabriken ermöglicht. Die Fähigkeit, Funktionen als Objekte zu manipulieren, ist ein wesentlicher Bestandteil der funktionalen Programmierfähigkeiten von Python, wo Operationen wie map, filter und reduce auf der Übergabe von Funktionen als Argumente beruhen, um Logik auf Datensammlungen anzuwenden.
## Codebeispiel

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(a, b, operation):
    return operation(a, b)

result = calculate(4, 2, add)
print(result)
```

