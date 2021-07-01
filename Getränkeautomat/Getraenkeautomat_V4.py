"""''''''''''''''''''''''''''''''''''''''''''''''''
Der Getraenkeautomat Version 4
"""''''''''''''''''''''''''''''''''''''''''''''''''

#die Vereinbahrung der Klasse für die Münzeneinheit
class Muenzeneinheit:
    #die Methode zum Initialisieren
    def init(self):
        #die Attribute
        self.betrag = 0
        self.noch_zu_zahlen =0
        self.rueckgeld =0

    #die weitere Methoden
    def muenzen_annehmen(self, wert):
        self.noch_zu_zahlen=self.noch_zu_zahlen-wert

    def rueckgeld_geben(self):
        #den absoluten Beitrag von dem noch zu zahlen liefern
        self.rueckgeld=abs(self.noch_zu_zahlen)
        return self.rueckgeld

    def set_beitrag(self, preis):
        self.betrag = preis
        self.noch_zu_zahlen = self.betrag

    def get_noch_zu_zahlen(self):
        return self.noch_zu_zahlen

#die Vereinbahrung der Klasse fpr den Automaten
class Getraenkeautomat:
    #die Methoden
    def init(self):
        #die Attribute
        #eine Liste mit Getränkennahmen
        self.getraenk =[]
        #eine leere Liste mit Anzahl der Flaschen
        self.anzahl_flaschen =[]
        #jetzt ist die Münzeneinheit ein Teil eines Getränkeautomat
        self.zahlomat = Muenzeneinheit()
        #die Instanz inizialisieren
        self.zahlomat.init()

        #die Getränke eintragen
        self.getraenk.append("Limonade")
        self.getraenk.append("Wasser")
        self.getraenk.append("Bier")

        #die Anzahl der Flaschen
        self.anzahl_flaschen.append(10)
        self.anzahl_flaschen.append(10)
        self.anzahl_flaschen.append(10)

        #die Kühlung ist aus
        self.kuelung = False

    def getraenke_waelen(self):
        #die Auswahl
        print("Bitte wählen Sie ein Getränk")
        print("Es gibt folgende Auswahl")
        anzeige_auswahl = 1
        for getraenk in self.getraenk:
            print(anzeige_auswahl,getraenk)
            anzeige_auswahl = anzeige_auswahl+1

        auswahl = int(input("Geben Sie die gewünschte Nummer ein:"))

        #gibt es noch Flasche von gewähltem Getränk?
        if self.anzahl_flaschen[auswahl-1]!=0:
            #die Anzahl Flaschen einlesen
            anzahl = int(input("Wie viele Flaschen möchten Sie?"))

            #erst muss bezahl werden
            #der Preis 10 ist fest vorgegeben
            print("Sie müssen", anzahl * 10,"Cent bezahlen")
            self.zahlomat.set_beitrag(anzahl*10)
            while self.zahlomat.get_noch_zu_zahlen()>0:
                print("Es fehlen noch", self.zahlomat.get_noch_zu_zahlen(),"Cent")
                self.zahlomat.muenzen_annehmen(3)

            #das Getränk ausgeben
            auswahl=auswahl-1
            self.getraenke_ausgeben(anzahl, auswahl)
        else:
            print("Das gewählte Getränkt ist leider nicht merh vorhanden.")
            auswahl = -1

        return auswahl

    def getraenk_ausgeben(self, anzahl, getraenke_index):
        #gibt es noch genügend Flacshen?
        if anzahl <= self.anzahl_flaschen[getraenke_index]:
            print("Sie erhalten", anzahl,"Flasche(n)",self.getraenk[getraenke_index])
            self.getraenk[getraenke_index]=self.getraenk[getraenke_index] - anzahl
        else:
            print("Es sind nur noch", self.anzahl_flaschen[getraenke_index], "Flaschen",self.getraenk[getraenke_index],"vorhanden.")
            print("Sie erhalten den Rest")
            self.anzahl_flaschen[getraenke_index]=0
        #Geld zurück geben
        print("Sie erhalten", self.zahlomat.rueckgeld_geben(), "Cent zurück")

    def kuehlen(self, an_aus):
        self.kuelung = an_aus
        if self.kuelung == True:
            print("Die Kühlung ist eingeschaltet.")
        else:
            print("Die Kühlung ist ausgeschaltet.")

#einen automat erzeugen
automat =Getraenkeautomat()
#die Instanz initialisieren
automat.init()

auswahl = -1
#die Kühlung anschalten
automat.kuehlen(True)

#ein Getränk auswählen
while auswahl == -1:
    auswahl = automat.getraenke_waelen()

#die Kühlung ausschakten
automat.kuehlen(False)