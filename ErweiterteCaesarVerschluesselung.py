#die erweiterte Funktion zur Cäser Verschlüsselung
def caesar(kette):
    print("Caesar Verschlüsseung")
    verschiebung = int(input("Bitte geben SIe den Verschiebewert ein: "))

    #jedes Zeichen um den angegeben Wert und deren Stelle verschieben
    for zeichen in range(len(kette)):

        #ist es ein großer Buchstabe?
        if kette[zeichen].isupper():
            print(chr((ord(kette[zeichen]) + verschiebung + zeichen - 65) % 26 + 65), end="")

        else:
            print(chr((ord(kette[zeichen]) + verschiebung + zeichen - 97) % 26 + 97), end="")

    print("\n")

caesar("Viktor")