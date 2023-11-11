# Lernfeld B2E

## Kompetenz
Ich kann Funktionen als Objekte und Argumente verwenden, um komplexe Aufgaben. (Anwenden von Closures)

## Funktionen als Objekte
In Python ermöglicht die Nutzung von Funktionen als Objekte und Argumente die Bewältigung komplexer Aufgaben durch die Verwendung von Closures. Ein Closure ist ein Funktionsobjekt, das sich Werte in umschließenden Bereichen merkt, auch wenn sie nicht im Speicher vorhanden sind. Es handelt sich um einen Datensatz, der eine Funktion zusammen mit einer Umgebung speichert: eine Zuordnung, die jede freie Variable der Funktion mit dem Wert oder Verweis verbindet, an den der Name bei der Erstellung der Closure gebunden war. Closures werden häufig für Funktionsfabriken verwendet, mit denen spezialisierte Funktionen im Handumdrehen erstellt werden können, sowie zur Kapselung privater Daten in der objektorientierten Programmierung.

```python
def power_exponentiator(exponent):
    def exponentiate(base):
        return base ** exponent
    return exponentiate

square = power_exponentiator(2)
print(square(10))  # Output: 100
cube = power_exponentiator(3)
print(cube(10))  # Output: 1000
```

