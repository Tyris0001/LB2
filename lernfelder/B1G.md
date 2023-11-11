# Lernfeld B1G

## Kompetenz
Funktionen höherer Ordnung sind Funktionen, die andere Funktionen als Parameter akzeptieren oder Funktionen zurückgeben können. Dies ermöglicht die Komposition von Funktionen und die Verwendung von Funktionsfabriken, was die Code-Wiederverwendbarkeit und -Lesbarkeit erhöht. In Python sind Funktionen höherer Ordnung ein wichtiger Bestandteil der funktionalen Programmierfähigkeiten und werden häufig in Verbindung mit Funktionen wie `map`, `filter` und `reduce` verwendet.

## Anwendung von Funktionen höherer Ordnung in BuxPay

In meinem BuxPay-Code sind Funktionen höherer Ordnung in verschiedenen Teilen des Codes vorhanden. Hier sind einige Beispiele:

1. **Verwendung von `map` und Funktionen höherer Ordnung:**

   ```python
   def create_invoice(client):
       # ...
       invoices = filter(None, map(create_invoice, app.buxpay_app.clients))
   ```

   Hier wird die Funktion `map` verwendet, um die Funktion `create_invoice` auf jede Client-Instanz in `app.buxpay_app.clients` anzuwenden. Dies ist ein Beispiel für die Verwendung einer Funktion höherer Ordnung (`map`), um eine andere Funktion (`create_invoice`) auf eine Liste von Elementen anzuwenden.

2. **Filtern mit einer Funktion höherer Ordnung:**

   ```python
   invoices = filter(None, map(create_invoice, app.buxpay_app.clients))
   ```

   Die `filter`-Funktion wird verwendet, um ungültige Rechnungen aus der Liste `invoices` zu filtern. Hier wird die Funktion `None` als Filterfunktion verwendet, um ungültige Rechnungen zu entfernen. Dies ist ein weiteres Beispiel für die Verwendung einer Funktion höherer Ordnung (`filter`), um die Daten zu transformieren.

3. **Verwendung von Funktionen als Argumente:**

   ```python
   def cleanup_paid_transactions(self):
       # ...
       client.remove_expired_invoices(current_time)
   ```

   In der Methode `cleanup_paid_transactions` wird die Funktion `remove_expired_invoices` auf jede Client-Instanz angewendet. Hier wird eine Funktion (`remove_expired_invoices`) als Argument an eine andere Funktion übergeben.

Die Verwendung von Funktionen höherer Ordnung in meinem BuxPay-Code erhöht die Lesbarkeit und Wiederverwendbarkeit des Codes, da Funktionen modular und flexibel kombiniert werden können, um komplexe Aufgaben zu erfüllen. Dies ist ein Beispiel für die Anwendung der Kompetenz "Funktionen höherer Ordnung" in meinem BuxPay-Projekt.