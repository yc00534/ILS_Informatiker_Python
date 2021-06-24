"""Der Getränkeautomat"""

class Getraenkeautomat:
    #die Methoden
    def init(self):
        # die Attribute erzeugen
        # eine leere Liste für die Gertränkenamen
        self.getraenk = []
        # eine leere Liste für die Anzahl der Flaschen
        self.anzahl_flaschen = []

        #die Getränke eintrage
        self.getraenk.append("Limonade")
        self.getraenk.append("Wasser")
        self.getraenk.append("Bier")

        # die Anzahl der Flaschen
        self.anzahl_flaschen.append(10)
        self.anzahl_flaschen.append(10)
        self.anzahl_flaschen.append(10)

        #die Kühlung ist aus
        self.kuehlung = False

    def getraenke_waelen(self):
        # die Auswahl
        print("Bitte wählen Sie ein Getränkt: ")
        print("Es gibt folgender Auswahl:")
        anzeige_auswahl = 1
        for getraenk in self.getraenk:
            print(anzeige_auswahl, getraenk)
            anzeige_auswahl=anzeige_auswahl+1

        #bitte in eine Zeile eingeben
        auswahl = int(input("Geben Sie gewünschte Nummer ein:"))

        #es gibt noch Flaschen von gewähltem Getränkt?
        if self.anzahl_flaschen[auswahl-1] != 0:
            auswahl=auswahl-1
        else:
            print("Das gewählte Getränk ist leider nicht mehr vorhanden.")
            auswahl = -1

        return auswahl

    def getraenk_ausgeben(self,anzahl,getraenke_index):
        #gibt es noch genügend Flaschen?
        print("")