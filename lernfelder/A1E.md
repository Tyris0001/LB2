# Lernfeld A1E

# Kompetenz
Ich kann aufzeigen wie Probleme in den verschiedenen Konzepten (OO, prozedural und funktional) gelöst werden und diese miteinander vergleichen.

# Wege zur Lösung von Problemen mit Code erforschen
Bei der Programmierung gibt es drei Hauptansätze zur Problemlösung: Objektorientiert (OO), prozedural und funktional.

### Objektorientiert (OO)
Bei OO werden Probleme durch die Erstellung von Objekten gelöst. Diese Objekte enthalten Daten und haben Aktionen, die sie ausführen können. Es ist ein strukturierter Ansatz, bei dem verschiedene Objekte miteinander interagieren, um eine Lösung zu erreichen.

#### Code
```python
class Object:
    def __init__(self, a, b):
        self.data = a
        self.__private_var = b
        
    @property # this is one way to make a getter, you can also just do it without annotations
    def private_var(self):
        return self.__private_var

# we create the object
obj = Object(1, 2)

# we can freely access the "data" property
print(obj.data)

# we cannot freely access the "private_var" property, as it is private. Since we have an annotation and a getter, we are now able to call it like a regular variable.
print(obj.private_var)
```

### Prozedural
Bei diesem Ansatz wird eine Liste von Anweisungen geschrieben, die der Computer in einer bestimmten Reihenfolge befolgen soll. Jede Anweisung wird Schritt für Schritt ausgeführt, um das anstehende Problem zu lösen.

```python
# to be honest I don't really get this part :P
def add(a, b):
    return a+b

print(add(1, 2))
```
### Funktional
Bei der funktionalen Programmierung werden Probleme durch die Erstellung von Funktionen gelöst. Jede Funktion nimmt Daten auf, verarbeitet sie und gibt ein Ergebnis zurück, ohne etwas außerhalb der Funktion zu verändern.
Jeder dieser Ansätze hat seine eigenen Regeln und Wege, den Code zu organisieren. Im Flask-Projekt wurden die verschiedenen Paradigmen erforscht, um zu verstehen, wie sie bei der Lösung verschiedener Probleme helfen. Durch diese Erkundung wurde ein tieferes Verständnis für die Herangehensweise an die Problemlösung beim Programmieren erlangt.
```python
# I'll use fibonacci sequence as an example because it's the only one that comes to mind right now
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
```


