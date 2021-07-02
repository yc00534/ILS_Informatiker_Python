"""''''''''''''''''''''''''''''''''''''''
Der Getränkeautomat Version 6
mit der Methode __init__() und __del__()
''''''''''''''''''''''''''''''''''''''"""

#die Vereinbahrung der Klasse für die Münzeneinheit
class Muenzeneinheit:
    #die Methode __init__()
    def __init__(self):
        #die Attribute
        self.betrag = 0
        self.noch_zu_zahlen = 0
        self.rueckgeld = 0

    #die Methode __del__()
    def __del__(self):
        print("Eine Instanz der Klasse Muenzeneinheit wurde gelöscht")

    #die weiter Methoden
    def muenzen_annehmen(self,wert):
        self.noch_zu_zahlen = self.noch_zu_zahlen - wert

    def rueckgeld_geben(self):
        #absoluten Beitrag von noch_zu_zahlen als Rückgeld liefern
        self.rueckgeld = abs(self.noch_zu_zahlen)
        return self.rueckgeld

    def set_beitrag(self, preis):
        self.betrag = preis
        self.noch_zu_zahlen = self.betrag

    def get_noch_zu_zahlen(self):
        return self.noch_zu_zahlen

#die Vereinbahrung der Klasse für den Automaten
class Getraenkeautomat:
    #übergeben werden die Anzahl und eine Referenz azf die Münzeneinheit
    def __init__(self, anzahl1, anzahl2, anzahl3, temp_zahlomat):
        #die Attribute
        #jetz ist die Muenzeneinheit Teil des Automaten
        self.zahlomat = temp_zahlomat

        #eine leere Liste fpr die Getränkenahmen
        self.getraenk = []

        #eine leere Liste fpr die Anzahl der Flaschen
        self.anzahl_flaschen = []

        #die Getränke eintragen
        self.getraenk.append("Limonade")
        self.getraenk.append("Wasser")
        self.getraenk.append("Bier")

        #die Anzahl der Flaschen
        #die werden jetzt durch die Argmente gesetzt
        self.anzahl_flaschen.append(anzahl3)
        self.anzahl_flaschen.append(anzahl2)
        self.anzahl_flaschen.append(anzahl1)

        #die Kühlung ist aus
        self.kuehlung = False

    def __del__(self):
        print("Eine Instanz der Klasse Getraenkeautomat wurde gelöscht.")

    def getraenke_waehlen(self):
        #die Auswahl
        print("Bitte wählen Sie ein Getränkt.")
        print("Es gibt folgende Auswahl:")
        anzeige_auswahl = 1
        for getraenk in self.getraenk:
            print(anzeige_auswahl,getraenk)

        auswahl = int(input("Geben Sie die gewünschte Nummer ein:"))

        #gibt es Flaschen von dem Gewaeltem Getränk?
        if self.anzahl_flaschen[auswahl-1]!=0:
            #die Anzahl der Flaschen einlesen
            anzahl = int(input("Wie viele Flaschen möchten Sie?"))

            #erst muss bezahlt werden
            #der Preis 10 ist fest vorgeschrieben
            print("Sie müssen", anzahl*10,"Cent bezahlen.")
            self.zahlomat.set_beitrag(anzahl*10)
            while self.zahlomat.get_noch_zu_zahlen()>0:
                print("Es fehlen noch", self.zahlomat.get_noch_zu_zahlen(), "Cent.")
                self.zahlomat.muenzen_annehmen(3)

            #das Getraenk ausgeben
            auswahl = auswahl - 1
            self.getraenk_ausgeben(anzahl,auswahl)
        else:
            print("Das gewählte Getränkt ist leider nicht mehr vorhanden.")
            auswahl = -1

        return auswahl
    def getraenk_ausgeben(self, anzahl, getraenke_index):
        #gib es noch genügend Flaschen?
        if anzahl<=self.anzahl_flaschen[getraenke_index]:
            print("Sie erhalten,",anzahl, "Flaschen(n)",self.getraenk[getraenke_index])
            self.anzahl_flaschen[getraenke_index]=self.anzahl_flaschen[getraenke_index]-anzahl
        else:
            print("Es sind nur noch", self.anzahl_flaschen[getraenke_index],"Flaschen", self.getraenk[getraenke_index], "vorhanden")
            print("Sie erhalten den Rest")
            self.anzahl_flaschen[getraenke_index] = 0
            #Geld zurück geben
            print("Sie erhalten", self.zahlomat.rueckgeld_geben(),"Cent zurück.")

    def kuehlen(self, an_aus):
        self.kuehlung = an_aus
        if self.kuehlung ==True:
            print("Kühlung ist eingeschaltet.")
        else:
            print("Kühlung ist ausgeschaltet.")

#eine Münzeneinheit erzeugen
einheit = Muenzeneinheit()
#einen Automaten erzeugen
#die Münzen und die Anzhal der Getränke werden übergeben
automat = Getraenkeautomat(10,20,30,einheit)

auswahl = -1
#die Kühlung einschalten
automat.kuehlen(True)
#ein Getränk auswählen
while auswahl == -1:
    auswahl = automat.getraenke_waehlen()

#die Kühlung einschalten
automat.kuehlen(False)

#die Instanzen ausdrücklich freigeben
#zuerst der Automat
del automat
#und die Münzeneinheit
del einheit
