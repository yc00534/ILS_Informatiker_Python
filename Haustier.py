"""'''''''''''''''''''''''''''''
Eine einfache Klasse fpr Haustiere
'''''''''''''''''''''''''''''"""

#die Verinbarung der Klasse
class Haustier:
    #die Methode zum Initialisieren
    def init(self, vorgabe):
        #die Attribute
        self.gewicht = vorgabe

    #die weitere Methoden
    #zum Füttern
    def fuettern(self, aenderung):
        self.gewicht = self.gewicht + aenderung

    #zum Ausgebe des Gewichts
    def ausgeben(self):
        print("Das aktuelle Gewicht beträgt", self.gewicht)

#eine katze erzeugen
katze = Haustier()

#die methode init aufrufen
katze.init(5)

#das Gewicht ausgeben
print("Nach inizialisierung: ")
katze.ausgeben()

#einmal füttern
katze.fuettern(1)
print("Nach dem Füttern")
katze.ausgeben()

katze.gewicht = katze.gewicht+2
katze.ausgeben()