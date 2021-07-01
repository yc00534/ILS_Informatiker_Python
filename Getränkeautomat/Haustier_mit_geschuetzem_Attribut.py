"""''''''''''''''''''''''''''''''
Eine einfache kLasse fpr Haustier mit
geschütztem Attribut
'''''''''''''''''''''''''''''''"""

#die Vereinbahrung der Klasse
class Haustier:
    #die Methode zum Initialisieren
    def init(self, vorgabe):
        #auf das Anttribut soll nicht von außen zugegriffen werden
        self.__gewicht = vorgabe

    #die weitere Methden
    #zum Füttern
    def fuettern(self, aenderung):
        self.__gewicht = self.__gewicht + aenderung

    #zum Ausgeben des Gewichts
    def ausgeben(self):
        print("Das aktuelle Gewicht beträgt:", self.__gewicht)

katze = Haustier()

#die Methode init aufrufen
katze.init(5)

#einmal fuettern
#der Zugruff efrikgt von außen
katze._Haustier__gewicht = katze._Haustier__gewicht+2
print("Nach dem Füttern")
katze.ausgeben()

