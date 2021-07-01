"""'''''''''''''''''''''''''''
Der Getränkeautomat Version 5
mit der Methode __init__()
''''''''''''''''''''''''"""

#die Vereinbahrung der Klasse für die Münzeneinheit
class Muenzeneinheit:
    #die Methode __init__()
    def __init__(self):
        #die Attribute
        self.beitrag = 0
        self.noch_zu_zahlen = 0
        self.rueckegeld = 0

    #die weitere Methoden
    def muenzen_annehmen(self, wert):
        self.noch_zu_zahlen = self.noch_zu_zahlen - wert

    def rueckgeld_geben(self):
        #den absoluten Beitrag von noch_zu_zahlen aks Rückgeld liefern
        self.rueckegeld = abs(self.noch_zu_zahlen)
        return self.rueckegeld

    def set_betrag(self, preis):
        self.beitrag = preis
        self.noch_zu_zahlen = self.beitrag

    def get_noch_zu_zahlen(self):
        return self.noch_zu_zahlen

#die Vereinbahrung der Klasse fpr den Automaten
class Getraenkeautomat:
    #übergeben wertden die Anzahl und eine Referenz auf die Muenzeneinheit
    def __init__(self, anzahl1, anzahl2, anzahl3, temp_zahlomat):
        #die Attribute
        #jetzt ist die Münzeneinheit Teil des Automaten
        self.zahlomat = temp_zahlomat

        #eine leere Liste für die Getränkenahmen
        self.getraenk = []

        #eine leere Liste für die Anzahl der Flaschen
        self.anzahl_flaschen = []

        #die Getränke eintragen
        self.getraenk.append("Limonade")
        self.getraenk.append("Wasser")
        self.getraenk.append("Bier")

        #die Anzahl der Flaschen
        #die werden jetzt durch die Argumente gesetzt
        self.anzahl_flaschen.append(anzahl1)
        self.anzahl_flaschen.append(anzahl2)
        self.anzahl_flaschen.append(anzahl3)

        #die Kühlung ist aus
        self.kuehlung = False

    def getraenke_waehlen(self):
        #die Auswahl
        print("Wählen Sie bitte ein Getränk:")
        print("Es gibt folgender Auswahl:")
        anzeige_auswahl = 1
        for getraenk in self.getraenk:
            print(anzeige_auswahl, getraenk)
            anzeige_auswahl = anzeige_auswahl +1

        auswahl = int(input("Geben Sie die gewünschte Nummer ein: "))

        #gibt es noch Flaaschen von dem Gewähltem Getränk?
        if self.anzahl_flaschen[auswahl-1]!=0:
            #die Anzahl Flaschen einlesen
            anzahl = int(input("Wie viele Flaschen möchten Sie?"))

            #erst muss bezahlt werden
            #der Preis 10 ist fest vergeben

            print("Sie müssen ", anzahl*10, "Cent bezahlen.")
            self.zahlomat.set_betrag(anzahl*10)
            while self.zahlomat.get_noch_zu_zahlen()>0:
                print("Es fehlen noch",self.zahlomat.get_noch_zu_zahlen(), "Cent.")
                self.zahlomat.muenzen_annehmen(3)

            #das Getränk ausgeben
            auswahl = auswahl -1
            self.getraenk_ausgeben(anzahl, auswahl)
        else:
            print("Das gewählte Getränk ist leider nicht mher vorhanden.")
            auswahl = -1

        return auswahl

    def getraenk_ausgeben(self, anzahl, getraenke_index):
        #gibt es noch genügend Flaschen?
        if anzahl <= self.anzahl_flaschen[getraenke_index]:
            #bitte jeweils in eine Zeile eingeben
            print("Sie erhalten", anzahl, "Flaschen", self.getraenk[getraenke_index])
            self.anzahl_flaschen[getraenke_index] = self.anzahl_flaschen[getraenke_index]-anzahl
        else:
            print("Es sind nur noch", self.anzahl_flaschen[getraenke_index], "vorhanden")
            print("Sie erhalten den Rest")
            self.anzahl_flaschen[getraenke_index] = 0
        #Geld zurück geben
        print("Sie erhalten", self.zahlomat.rueckgeld_geben(), "Cent zurück.")

    def kuehlen(self, an_aus):
        self.kuehlung = an_aus
        if self.kuehlung == True:
            print("Kühlung ist eingeschaltet.")
        else:
            print("Kühlung ist ausgeschaltet,")

#eine Muenzeneinheit erzeugen
zahlomat = Muenzeneinheit()
#einen Automaten Erzeigen
#die Muenzeneinheit und die Anzahl der Getränke werden übergeben
automat = Getraenkeautomat(10,20,30,zahlomat)

auswahl = -1
automat.kuehlen(True)

while auswahl == -1:
    auswahl = automat.getraenke_waehlen()

automat.kuehlen(False)

