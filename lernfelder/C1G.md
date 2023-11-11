# Lernfeld C1G

## Kompetenz
:Ich kann einige Refactoring-Techniken aufzählen, die einen Code lesbarer und verständlicher machen.

## Refactoring-Techniken

### Kommentare
Kommentare sind nützlich, um den Code zu dokumentieren und zu erklären. Sie sollten jedoch sparsam verwendet werden, da sie den Code unübersichtlich machen können. Wenn Sie Kommentare verwenden, sollten Sie sich an die folgenden Richtlinien halten:

- Kommentiere nur Code, der schwer zu verstehen ist.
- Kommentiere nicht offensichtliche Dinge.
- Kommentiere nicht mehr als nötig.
- Kommentiere nicht, was Sie tun, sondern warum Sie es tun.
- Kommentiere nicht, was Sie vorhaben, sondern was Sie getan haben.

### Variablen

#### Variablen umbenennen
Variablen sollten so benannt werden, dass sie den Zweck der Variablen widerspiegeln. Wenn Sie eine Variable umbenennen, sollten Sie sich an die folgenden Richtlinien halten:

- Verwende keine Abkürzungen.
- Verwende keine Zahlen am Ende des Variablennamens.
- Verwende keine doppelten Namen.
- Verwende keine Namen, die bereits in Python verwendet werden.
- Schreibe Variabeln nicht mit camel-case sondern mit snake-case.

Beispiel coding conventions python:
```python

# Variablen
my_variable = 1
my_long_variable = 2
my_long_variable_name = 3

# Funktionen
def my_function():
    pass

def my_long_function():
    pass

def my_long_function_name():
    pass

# Klassen
class MyClass:
    pass

class MyLongClass:
    pass

class MyLongClassName:
    pass

```

Beispiel falsche coding conventions python:
```python

# Variablen
myVariable = 1
myLongVariable = 2
myLongVariableName = 3

# Funktionen
def myFunction():
    pass

def myLongFunction():
    pass

def myLongFunctionName():
    pass

# Klassen
class myClass:
    pass

class myLongClass:
    pass

class myLongClassName:
    pass
```