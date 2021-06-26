"""''''''''''''''''''''''''''''''''''''''''''''''''
Der Getraenkeautomat Version 3
"""''''''''''''''''''''''''''''''''''''''''''''''''

class Muenzeneinheit:
    #die Methode zu initialisieren
    def init(self):
        #die Attribute
        self.betrag = 0
        self.noch_zu_zahlen = 0
        self.rueckgeld = 0

    #die weitere Methoden
    def muenzen_annehmen(self, wert):
        self.noch_zu_zahlen=self.noch_zu_zahlen - wert

    def rueckgeld_geben(self):
        self.rueckgeld = abs(self.noch_zu_zahlen)
        return self.rueckgeld

    def set_beitrag(self, preis):
        self.betrag = preis
        self.noch_zu_zahlen = self.betrag

    def get_noch_zu_zahlen(self):
        return self.noch_zu_zahlen

# die Vereinbarung der Klasse für den Automaten
class getraenkeautomat:
    #die Methoden
    def init(self):
        #die Attribute

        #eine leere Liste für die Getränkenahmen
        self.getraenk = []

        #eine leere Liste für die Auswahl der Flaschen
        self.anzahl_flaschen =[]

        #die Getränke eingtragen
        self.getraenk.append("Limonade")
        self.getraenk.append("Wasser")
        self.getraenk.append("Bier")

        #die Anzahl der Flaschen
        self.anzahl_flaschen.append(10)
        self.anzahl_flaschen.append(10)
        self.anzahl_flaschen.append(10)

        #die Kühlung ist aus
        self.kuehlung = False

    def getraenke_waehlen(self):
        #die Auswahl
        print("Bitte wählen Sie ein Getränk: ")
        print("Es gibt folgende Auswahl: ")
        anzeige_auswahl = 1
        for getraenk in self.getraenk:
            print(anzeige_auswahl, getraenk)
            anzeige_auswahl = anzeige_auswahl+1
        auswahl = int(input("Geben Sie die gewünschte Nummer ein: "))

        #gibt es noch flaschen von dem gewählten Getränk?
        if self.anzahl_flaschen[auswahl-1]!=0:
            auswahl = auswahl-1
        else:
            print("Das gewählte Getränk ist leider nicht mehrvorhanden.")
            auswahl = -1

        return auswahl

    def getraenk_ausgeben(self, anzahl, getraenke_index):
        #gibt es noch genügend Flaschen?
        if anzahl<=self.anzahl_flaschen[getraenke_index]:
            print("Sie erhalten Anzahl flaschen", anzahl, "Flasche(n)", self.getraenk[getraenke_index])
            self.anzahl_flaschen[getraenke_index]=self.anzahl_flaschen[getraenke_index]-anzahl
        else:
            print("es sind nur noch", self.anzahl_flaschen[getraenke_index],"Flaschen", self.getraenk[getraenke_index],"vorhanden.")
            print("Sie erhalten den Rest.")
            self.anzahl_flaschen[getraenke_index]=0

    def kuehlen(self, an_aus):
        self.kuehlung=an_aus
        if self.kuehlung == True:
            print("Die Kühlung ist eingeschalten")
        else:
            print("Die Kühlung ausgeschlatet")

#einen automaten erzeugen
automat = getraenkeautomat()
#eine Münzeneinheit erzeugen
zahlomat = Muenzeneinheit()

#die instanzen inizialisieren
automat.init()
zahlomat.init()

auswahl = -1
#ein Getränk wählen
while auswahl == -1:
    auswahl = automat.getraenke_waehlen()

#die Kühlung einschalten
automat.kuehlen(True)

#das Getränk ausgeben
anzahl = int(input("Wie viel Flaschen möchten Sie?"))

#erst muss bezahlt werden
#der Preis 10 ist fest vergeben
print("Sie müssen",anzahl *10, "Cent bezahlen")
zahlomat.set_beitrag(anzahl*10)
while zahlomat.get_noch_zu_zahlen()>0:
    print("Es fehlen noch", zahlomat.get_noch_zu_zahlen(),"Cent. ")
    zahlomat.muenzen_annehmen(int(input("Werfen Sie jetzt das Geld ein")))

#das Getränk ausgeben
automat.getraenk_ausgeben(anzahl,auswahl)

#geld zurück geben
print("Sie erhalten", zahlomat.rueckgeld_geben(), "Cent zurück.")

#die Kühlung ausschalten
automat.kuehlen(False)


