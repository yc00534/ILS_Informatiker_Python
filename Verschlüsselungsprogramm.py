# die Funktion zum Umdrehen
def dreher(kette):
    # die Länge der ursprünglichen Zeichenkette ermitteln
    laenge = len(kette)
    laenge = laenge - 1
    zahler = laenge

    print("Verschlüsselung durch Umdrehen")
    # die Zeichen von hinten nach vorne ausgeben
    while zahler >= 0:
        print(kette[zahler], end="")
        zahler = zahler - 1

    print("\n")

#die Funktion zur numerischen Verschlüsselung über Ausgabe des ASCII Wertes
def ascii_code(kette):
    print("Verschlüsselung durch ASCII Asugabe")
    #für jedes Zeichen über ord() den ASCII-Wert ausgeben
    for zeichen in kette:
        print(ord(zeichen),end="")

    print("\n")

#die Funktion zur Cäser Verschlüsselung
def caesar(kette):
    print("Caesar Verschlüsseung")
    verschiebung = int(input("Bitte geben SIe den Verschiebeweer ein: "))
    #jedes Zeichen um den angegeben Wert verschieben
    for zeichen in kette:
        #ist es ein großer Buchstabe?
        if zeichen.isupper():
            print(chr((ord(zeichen)+verschiebung-65)%26+65),end="")
        else:
            print(chr((ord(zeichen)+verschiebung-97)%26+97),end="")

    print("\n")

#die Funktion zur Gartenzaunverschlüsselung
def gartenzaun(kette):
    #zwei leeren Zeichenketten vereinbahren
    teil1 = ""
    teil2 = ""

    #die Länge der ursprünglichen Zeichenkette ermitteln
    laenge = len(kette)
    #fuer den Index
    zahler = 0

    #die Zeichen verteilen
    while zahler<laenge:
        #Zeichen mit graden Index kommen in ie Zeichenkette teil1
        if zahler%2==0:
            teil1 = teil1+kette[zahler]
        #bei ungraden Index werden die Zeichen in der Zeichenkette teil2 abgelegt
        else:
            teil2 = teil2 + kette[zahler]
        zahler = zahler + 1

    #die beiden Zeichenketten werden zusammen gebaut
    codiert = teil1 + teil2

    #und ausgeben
    print("Gartenzaunverschlüsselung")
    print("Die obere Hälfte ist: ", teil1)
    print("Die untere Hälfte ist: ", teil2)
    print("Das komplette Woet ist: ", codiert)

#die ursprüngliche Zeichenkette einlesen:
eingabe = input("Bitte geben Sie eine Zeichenkette ein: ")
print("Die ursprüngliche Zeichenkette ist: ", eingabe, "\n")

#die Verschlüsselungen durchführen
dreher(eingabe)
ascii_code(eingabe)
caesar(eingabe)
gartenzaun(eingabe)