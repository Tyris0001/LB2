# Lernfeld B3F

## Kompetenz
Ich kann Lambda-Ausdrücke schreiben, die mehrere Argumente verarbeiten können.

## Anwendung von Lambda-Ausdrücken in BuxPay

In meinem BuxPay-Code gibt es ein Beispiel für die Verwendung von Lambda-Ausdrücken, die mehrere Argumente verarbeiten können:

```python
invoices = filter(lambda invoice: invoice.status == "unpaid", app.buxpay_app.get_all_invoices())
```

In diesem Beispiel wird ein Lambda-Ausdruck verwendet, um eine Liste von Rechnungen zu filtern. Der Lambda-Ausdruck nimmt eine Rechnung als Argument und überprüft, ob ihr Status "unpaid" ist. Der Ausdruck `lambda invoice: invoice.status == "unpaid"` verarbeitet effektiv zwei Argumente: `invoice` (die Rechnung selbst) und `"unpaid"` (der zu vergleichende Status).

Die Verwendung von Lambda-Ausdrücken, die mehrere Argumente verarbeiten können, ermöglicht die präzise Definition von Filter- oder Vergleichslogik in einer kompakten Form. In diesem Fall hilft der Lambda-Ausdruck dabei, alle unbezahlten Rechnungen auszuwählen. Dies ist ein Beispiel für die Anwendung der Kompetenz "Lambda-Ausdrücke schreiben, die mehrere Argumente verarbeiten können" in meinem BuxPay-Projekt.