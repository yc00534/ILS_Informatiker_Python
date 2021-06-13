#der Import der Funktion randrange() aus dem Modul random
from random import randrange
import time

starttime = time.time()
#die maximale Anzahl der Werte
anzahl = 5000

#eine leere Liste für die Werte
werte = []

print("Bubblesort")
#die Liste fühlen. Benutzt werden zufällige zahlen bis 200
durchlauf = 1
while durchlauf <= anzahl:
    werte.append(randrange(1,5000,1))
    durchlauf = durchlauf +1

#ausgabe zur Kontrolle
print("die unsoertierte Werte sind: ")
for wert in werte:
    print(wert, end= " ")

#sortieren
#alle Werte durchgehen und dann von hinten nach vorne vergleichen
werte.sort()

#die sortierte Ausagabge
print()
print("Die sortierte Werte sind: ")
for wert in werte:
    print(wert, end= " ")


print()
print(time.time()-starttime)