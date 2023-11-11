# Lernfeld A1G

## Kompetenz
Ich kann die Eigenschaften von Funktionen beschreiben (z.Bsp. pure function) und den Unterschied zu anderen Programmier-Strukturen erläutern (z.Bsp. zu Prozedur).

## Verstehen von Funktionen und ihren Unterschieden zu Prozeduren
Als wir das Programmieren lernten, entdeckten wir, dass es verschiedene Möglichkeiten gibt, 
dem Computer zu sagen, was er tun soll. Eine dieser Möglichkeiten ist die Verwendung von sogenannten "Funktionen". 
Eine Funktion ist wie ein Miniprogramm, das eine bestimmte Aufgabe erledigen kann. Wir können zum Beispiel eine Funktion haben, 
die zwei Zahlen zusammenzählt. Wir können diese Funktion immer dann verwenden, wenn wir Zahlen addieren wollen, was ziemlich cool ist!

Wir haben auch etwas über eine besondere Art von Funktion gelernt, die "reine Funktion". 
Eine reine Funktion ist ein guter Freund, der immer die Wahrheit sagt. 
Egal, wie oft du ihr die gleiche Frage stellst, sie wird dir immer die gleiche Antwort geben. 
Wenn wir zum Beispiel eine reine Funktion haben, die zwei Zahlen addiert, wird sie auf die Frage, was 2 plus 2 ist, immer 4 sagen. 
Sie wird nicht plötzlich 5 oder 3 sagen, wenn wir das nächste Mal fragen. Das ist gut, denn wir können uns darauf verlassen, 
dass reine Funktionen uns bei der Lösung unserer Probleme helfen.
## Codebeispiel

```python
import random
# bester freund:
def friendly_function(a, b):
    return a+b 

# a-hole:
def unfriendly_function(a, b):
    return a+b+random.randint(0, 100)
```

