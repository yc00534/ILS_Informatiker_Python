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
i = 0
while i < anzahl:
    k = 0
    while k < anzahl -i - 1:
        #wenn das aktuelle Element größer ist als Folgeelement, wird getauscht
        if werte[k]>werte[k+1]:
            #den Wert sichern, damit der nicht überschrieben wird
            tausch_temp = werte[k]
            werte[k]=werte[k+1]
            werte[k+1]=tausch_temp
        k = k + 1
    i = i + 1

#die sortierte Ausagabge
print()
print("Die sortierte Werte sind: ")
for wert in werte:
    print(wert, end= " ")


print()
print(time.time()-starttime)