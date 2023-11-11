# Lernfeld B3G

## Kompetenz
Ich kann einfache Lambda-Ausdrücke schreiben, die eine einzelne Operation durchführen, z.B. das Filtern von Elementen in einer Liste.

## Anwendung von Lambda-Ausdrücken
In meinem BuxPay-Code gibt es ein Beispiel für die Anwendung von Lambda-Ausdrücken. Hier ist der relevante Code:

```python
def get_unpaid_invoices(self, client):
    # get client invoices
    unpaid_invoices = filter(lambda invoice: invoice.status == "unpaid", self.get_all_invoices())
    return unpaid_invoices
```

In diesem Beispiel wird die `filter`-Funktion zusammen mit einem Lambda-Ausdruck verwendet, um unbezahlte Rechnungen aus der Liste aller Rechnungen eines Clients zu filtern. Der Lambda-Ausdruck `lambda invoice: invoice.status == "unpaid"` wird verwendet, um zu überprüfen, ob der Status einer Rechnung "unpaid" ist. Dieser Lambda-Ausdruck ist eine einfache Funktion, die eine einzelne Operation durchführt, nämlich das Filtern von Rechnungen nach ihrem Status.

Die Verwendung von Lambda-Ausdrücken in diesem Kontext ermöglicht es, eine spezifische Filterlogik in einer kompakten und lesbaren Form darzustellen, ohne eine separate Funktion definieren zu müssen. Dies macht den Code effizienter und wartbarer, insbesondere wenn solche Filterlogik an verschiedenen Stellen im Code benötigt wird.