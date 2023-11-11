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

Ja, die Kompetenz "Funktionen als Objekte" ist in meinem BuxPay-Code vorhanden. Hier sind einige Beispiele, wie diese Kompetenz in meinem Code angewendet wird:

1. **Lambda-Ausdrücke als anonyme Funktionen:**
   - In den Endpunkten `lambda-example`, `higher-order-example`, `reduce-example`, `filter-example` und `functional-example` werden Lambda-Ausdrücke verwendet, um anonyme Funktionen zu erstellen und sie als Argumente an andere Funktionen zu übergeben. Dies zeigt die Flexibilität von Funktionen als Objekte erster Klasse.

2. **Verwendung von `map`, `filter` und `reduce`:**
   - Die Endpunkte `higher-order-example`, `reduce-example` und `filter-example` demonstrieren die Verwendung von `map`, `reduce` und `filter`, wobei Funktionen als Argumente übergeben werden, um Operationen auf Datenstrukturen anzuwenden. Dies ist ein Beispiel für die Verwendung von Funktionen höherer Ordnung.

3. **Funktionsrückgabe:**# Lernfeld B2G

## Kompetenz
Ich kann Funktionen als Objekte behandeln und diese in Variablen speichern und weitergeben.

## Anwendung von Funktionen als Objekte in BuxPay

In meinem BuxPay-Code gibt es Beispiele für die Behandlung von Funktionen als Objekte und deren Verwendung in Variablen:

1. **Verwendung von Funktionen als Objekte in `create_gamepass`:**

   ```python
   def create_gamepass(self, price, user_cookie):
       csrf_token = self.get_csrf_token(user_cookie)
       headers = {"x-csrf-token": csrf_token}
       data = {"Name": str(uuid.uuid4()), "Description": None, "UniverseId": user_cookie["universe"], "File": None}
       response = requests.post("https://apis.roblox.com/game-passes/v1/game-passes", headers=headers, data=data, cookies={'.ROBLOSECURITY': user_cookie['cookie']})
       return response
   ```

   Hier wird die Funktion `create_gamepass` als ein Objekt behandelt, da sie in der Variable `response` gespeichert und später zurückgegeben wird. Diese Flexibilität ermöglicht es, die Funktion an verschiedenen Stellen im Code zu verwenden und das Ergebnis in einer Variablen zu speichern.

2. **Verwendung von Funktionen als Objekte in `payments_create`:**

   ```python
   def payments_create():
       # ...
       invoices = filter(None, map(create_invoice, app.buxpay_app.clients))
   ```

   Die Funktion `create_invoice` wird in den Funktionen `map` und `filter` verwendet, was bedeutet, dass sie als Objekt behandelt wird. Dies ermöglicht es, die `create_invoice`-Funktion flexibel in den Algorithmen `map` und `filter` einzusetzen.

Die Fähigkeit, Funktionen als Objekte zu behandeln und in Variablen zu speichern, erhöht die Flexibilität und Wiederverwendbarkeit des Codes. Dies ist ein Beispiel für die Anwendung der Kompetenz "Funktionen als Objekte behandeln" in meinem BuxPay-Projekt.
   - In der Methode `create_gamepass` der Klasse `BuxPayApp` wird die Funktion `get_csrf_token` verwendet, um eine CSRF-Token-Funktion zu erstellen und sie dann als Argument an den `requests.post`-Aufruf zu übergeben.

Die Fähigkeit, Funktionen als Objekte zu verwenden und sie in verschiedenen Kontexten zu manipulieren, ist in meinem BuxPay-Code gut demonstriert und ermöglicht die Erstellung flexibler und leistungsfähiger Codemuster.