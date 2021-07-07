"""''''''''''''''''''
Lineare Suche
''''''''''''''''''"""

#der Import der Funktion randrange() aus dem MOdul random
from random import randrange

#die Maximale Anzahl der Werte
anzahl = 100

#eine leere Liste für die Werte
werte = []

#wurde schon ein Wert gefunden
gefunden = False

#für die Suche
suchen = 0

print("Lineare Suche")
#die Liste füllen. Benutzt werden zufällige Zahlen bos 200
durchlauf = 1
while durchlauf <= anzahl:
    werte.append(randrange(1, 201))
    durchlauf = durchlauf + 1

#zur Kontrolle ausgeben
print("Die Werte sind:")
for wert in werte:
    print(wert, end=" ")
print()

#Abfrage der Suchkriterien
kriterium = int(input("Wonach soll gesucht werden?"))

#liste mit Ergebnissen
ergebnisse = []

#und jetzt suchen, bis das Ende erreicht wurde und in die Liste ergebnisse[] einfügen
while suchen < anzahl:
    if werte[suchen]==kriterium:
        ergebnisse.append(suchen+1)
    suchen = suchen +1

#hat die Liste ergebnisse[] welche Werte, wenn ja - ausgeben
if len(ergebnisse) == 0:
    print("Der Wert",kriterium,"wurde nicht gefunden")
else:
    for ausgabe_ergebnisse in ergebnisse:
        print("Der Wert",kriterium,"befindet sich an der Position", ausgabe_ergebnisse)
