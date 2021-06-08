import time
from random import randrange

start_time = time.time()
#die maximale Anzahl der Werte
anzahl = 5000

#eine leere Liste fuer die Werte
werte = []

print("Einfache Maximumauswahl")
#die Liste füllen, benutzt werden zufällige Zahlen bis 200
durchlauf = 1
while durchlauf <= anzahl:
    werte.append(randrange(1, 5000, 1))
    durchlauf = durchlauf +1

#zur Kontrolle ausgeben
print("die unsortierte Werte sind: ")
for wert in werte:
    print(wert, end=" ")

#solange die unsortierte Bereich merh als ein Element enthält
k = anzahl - 1
while k > 0:
    #das letzte Element wird zum vorläufigen maximum
    maximum = k
    #den unsortierten Bereich durchgehen
    i = 0
    while i < k:
        #ist das neue Element das neue Maximum?
        if werte[maximum]<werte[i]:
            maximum = i
        i = i + 1

    #die Werte tauschen
    if maximum != k:
        tausch_temp = werte[k]
        werte[k] = werte[maximum]
        werte[maximum]=tausch_temp
    k = k - 1

#die sortierte Ausgabe
print()
print("Die sortierte Werte sind: ")
for wert in werte:
    print(wert, end=" ")

print()
ende_time = time.time()
print((ende_time-start_time))