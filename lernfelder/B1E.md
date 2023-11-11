# Lernfeld B1E

## Kompetenz
Ich kann Funktionen in zusammenhängende Algorithmen implementieren

## Implementierung von Funktionen in kohärenten Algorithmen

In Python ist eine Funktion ein Codeblock, der eine bestimmte Aufgabe erfüllt. Wir können Funktionen verwenden, um Algorithmen zu erstellen, die größere Aufgaben lösen, indem sie in kleinere Schritte zerlegt werden. Nehmen wir zum Beispiel an, wir wollen die kleinste und größte Zahl in einer Liste finden.

### Codebeispiel
```python
class BuxPayApp:
    def __init__(self):
        self.clients = []
        self.load_clients()
        self.load_invoices()
        threading.Thread(target=self.cleanup_paid_transactions).start()

    def load_json(self, filepath):
        """
        Load json file
        :param filepath:
        :return:
        """
        with open(filepath, "r") as file:
            return json.load(file)
```
Beispiel: `load_json`