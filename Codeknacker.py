#die Funktion zum Umdrehen
def dreher_knacken(kette):
    #die Länge der ursprunglichen Zeichenkette ermitteln
    laenge = len(kette)
    #len() liefert die "echte" Länge, daher muss 1 abgezogen werden
    laenge = laenge - 1
    zahler = laenge

    print("Das Umdrehen ergibt")
    #die Zeichen von hinten nach vorne ausgeben
    while zahler >= 0:
        print(kette[zahler],end="")
        zahler = zahler - 1

    print("\n")

#die Funktion zum Knacken der Caeser Verschlüsselung
def caeser_knacken(kette):
    print("Durchprobieren der Cäser-Verschlüsselung")
    verschiebung = 1
    #alle Verschiebewerte von 1 bis 25 durchgehen
    while verschiebung <= 25:
        print("Mit Verschiebezahl ", verschiebung, " ist das Ergebniss; ", end="")
        #jedes Zeichen um den Angegenben Wert veschieben
        for zeichen in kette:
            #ist es ein grosse Buchstabe
            if zeichen.isupper():
                print(chr((ord(zeichen)-verschiebung-65)%26+65), end="")
            else:
                print(chr((ord(zeichen)-verschiebung-97)%26+97), end="")
        print("")
        verschiebung = verschiebung + 1

    print("\n")

#die Funktion zum Knacken der Gartenzaunverschluesselung
def gartenzaun_knacken(kette):
    #eine leere Zeichenkette vereinbahren
    decodiert = ""

    #die Länge der ursprünglichen Zeichenkette ermitteln
    laenge = len(kette)

    #die Mitte finden
    mitte = laenge//2
    #wenn es eine ungerade Anzahl ist, noch 1 addieren
    if laenge % 2 != 0:
        mitte = mitte + 1

    #die Zeichenkette zerlegen
    teil1 = kette[0: mitte]
    teil2 = kette[mitte: laenge+1]

    zaehler = 0

    #die Zeichen verteilen
    while zaehler < laenge:
        # Zeichen mit einem geraden Index kommen aus der Zeichenkette
        #teil1
        if zaehler % 2 == 0:
            decodiert = decodiert + teil1[zaehler // 2]
        else:
            decodiert = decodiert + teil2[zaehler // 2]
        zaehler = zaehler + 1

    #und ausgeben
    #bitte in eine Zeile ausgeben
    print("Der Versuch mit der Gartenzaunverschluesselung ergibt ", decodiert)

#die ursprüngliche Zeichenkette einlesen
eingabe = input("Bitte geben Sie eine Zeichenkette ein: ")
print("Die ursprüngliche Zeichenkette ist ", eingabe, "\n")

dreher_knacken(eingabe)
caeser_knacken(eingabe)
gartenzaun_knacken(eingabe)

