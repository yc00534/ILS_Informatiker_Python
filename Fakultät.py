
#eingabe = int(input("Von welchem Wert soll die Fakultät berechnet werden"))
def fakultaetMethode(i: int):
    fakultaet=1
    while i > 0:
        fakultaet = fakultaet * i
        i = i - 1
    return fakultaet
