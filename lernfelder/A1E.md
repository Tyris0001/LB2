# Lernfeld A1E

## Kompetenz
Ich kann aufzeigen wie Probleme in den verschiedenen Konzepten (OO, prozedural und funktional) gelöst werden und diese miteinander vergleichen.

# Wege zur Lösung von Problemen mit Code erforschen
Bei der Programmierung gibt es drei Hauptansätze zur Problemlösung: Objektorientiert (OO), prozedural und funktional.

### Objektorientiert (OO)
Bei OO werden Probleme durch die Erstellung von Objekten gelöst. Diese Objekte enthalten Daten und haben Aktionen, die sie ausführen können. Es ist ein strukturierter Ansatz, bei dem verschiedene Objekte miteinander interagieren, um eine Lösung zu erreichen.

#### Code
Example public properties
```python
class Client:
    def __init__(self, username, api_key, robux_earned, robux_balance, expires, plan, invoices, cookies):
        self.username = username
        self.api_key = api_key
        self.robux_earned = robux_earned
        self.robux_balance = robux_balance
        self.expires = expires
        self.plan = plan
        self.invoices = invoices
        self.cookies = cookies

    def get_invoices(self): 
        return self.invoices

"""
Since all of our class properties do not begin with ._ or .__ they are publicly accessible!
Any piece of code that instances the "Client" object is able to access all of it's properties simply by doing the following:
"""
new_client = Client()
# now we get a random property
print(new_client.username)
```
Example private properties
```python
class Client:
    def __init__(self, username, api_key, robux_earned, robux_balance, expires, plan, invoices, cookies):
        self._username = username
        self._api_key = api_key
        self._robux_earned = robux_earned
        self._robux_balance = robux_balance
        self._expires = expires
        self._plan = plan
        self._invoices = invoices
        self._cookies = cookies

# so now if we wanted to access one of the properties, we wouldn't be able to do it by conventional means:

new_client = Client()

print(new_client.username) # this piece of code would result in an error
```
So how the F*** would we access these protected properties??<br>
Well the answer is quite simple actually (*It isn't, this is python dummy nothing is simple*)
#### Method 1:
We use a regular getter
```python
class Client:
    def __init__(self, username, api_key, robux_earned, robux_balance, expires, plan, invoices, cookies):
        self._username = username
        self._api_key = api_key
        self._robux_earned = robux_earned
        self._robux_balance = robux_balance
        self._expires = expires
        self._plan = plan
        self._invoices = invoices
        self._cookies = cookies

    def get_username(self):
        return self._username
```
#### Method 2:
You will use this method if you are one of the following:
- a smartass
- working at a company that has a strict coding convention
```python
class Client:
    def __init__(self, username, api_key, robux_earned, robux_balance, expires, plan, invoices, cookies):
        self._username = username
        self._api_key = api_key
        self._robux_earned = robux_earned
        self._robux_balance = robux_balance
        self._expires = expires
        self._plan = plan
        self._invoices = invoices
        self._cookies = cookies

    @property
    def username(self):
        return self._username

# fun thing is, now if you want to call this property, you can do so as if it was a public one
new_client = Client()
print(new_client.username)
# HOW COOL IS THAT!!!!
```
### Prozedural
Bei diesem Ansatz wird eine Liste von Anweisungen geschrieben, die der Computer in einer bestimmten Reihenfolge befolgen soll. Jede Anweisung wird Schritt für Schritt ausgeführt, um das anstehende Problem zu lösen.

```python
# to be honest I don't really get this part :P, nor do I think I've done this in my code
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


