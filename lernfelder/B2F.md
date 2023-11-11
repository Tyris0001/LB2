# Lernfeld B2F

## Kompetenz
Ich kann Funktionen als Argumente für andere Funktionen verwenden und dadurch höherwertige Funktionen erstellen.

## Anwendung von Funktionen als Argumente in BuxPay

In meinem BuxPay-Code gibt es Beispiele für die Verwendung von Funktionen als Argumente für andere Funktionen:

1. **Verwendung von Funktionen als Argumente in `map` und `filter`:**

   ```python
   def create_invoice(client):
       # ...
       invoices = filter(None, map(create_invoice, app.buxpay_app.clients))
   ```

   Hier wird die Funktion `create_invoice` als Argument für die Funktionen `map` und `filter` verwendet. `map` wendet die `create_invoice`-Funktion auf jede Client-Instanz in `app.buxpay_app.clients` an, und `filter` verwendet die `None`-Funktion als Filterfunktion. Dies ermöglicht die Erstellung höherwertiger Funktionen, die spezifische Transformationen auf Daten durchführen.

2. **Verwendung von Funktionen als Argumente in `cleanup_paid_transactions`:**

   ```python
   def cleanup_paid_transactions(self):
       # ...
       client.remove_expired_invoices(current_time)
   ```

   In der Methode `cleanup_paid_transactions` wird die Funktion `remove_expired_invoices` als Argument an die Methode `remove_expired_invoices` jedes Clients übergeben. Dadurch wird die Flexibilität des Codes erhöht, da verschiedene Client-Instanzen unterschiedliche Implementierungen der `remove_expired_invoices`-Funktion haben können.

Die Verwendung von Funktionen als Argumente ermöglicht es, höherwertige Funktionen zu erstellen, die auf abstrakte Weise mit Daten arbeiten können. Dies erhöht die Flexibilität und Wiederverwendbarkeit des Codes und ist ein Beispiel für die Anwendung der Kompetenz "Funktionen als Argumente für andere Funktionen" in meinem BuxPay-Projekt.