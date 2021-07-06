"""''''''''''''''''''''''''''''''''''''''
Der Getränkeautomat Version 6
mit der Methode __init__() und __del__()
''''''''''''''''''''''''''''''''''''''"""


class Getraenke:
    # die Methode init()
    def __init__(self, t_name, t_preis, t_anzahl):
        # die Attribute
        self._getraenke_name_ = t_name
        self._getraenke_preis_ = t_preis
        self._getraenke_flaschen_anzahl_ = t_anzahl

    # die Methode liefert den Getränkenamen zurück
    def get_getraenke_name(self):
        return self._getraenke_name_

    # die Methode liefert den Getränkepreis zurück
    def get_getraenke_preis(self):
        return self._getraenke_preis_

    # die Methode liefert den Anzahl der Flaschen zurück
    def get_getraenke_anzahl(self):
        return self._getraenke_flaschen_anzahl_

    def set_anzahl(self, gekaufte_Menge):
        self._getraenke_flaschen_anzahl_ = self._getraenke_flaschen_anzahl_ - gekaufte_Menge


# die Vereinbahrung der Klasse für die Münzeneinheit
class Muenzeneinheit:
    # die Methode __init__()
    def __init__(self):
        # die Attribute
        self.betrag = 0
        self.noch_zu_zahlen = 0
        self.rueckgeld = 0
        self.ruck_geld = 0

    # die Methode __del__()
    def __del__(self):
        print("Eine Instanz der Klasse Muenzeneinheit wurde gelöscht")

    # die weiter Methoden
    def muenzen_annehmen(self, wert):
        self.noch_zu_zahlen = self.noch_zu_zahlen - wert

    def rueckgeld_geben(self):
        # absoluten Beitrag von noch_zu_zahlen als Rückgeld liefern
        self.rueckgeld = abs(self.noch_zu_zahlen)
        return self.rueckgeld

    def set_beitrag(self, preis):
        self.betrag = preis
        self.noch_zu_zahlen = self.betrag

    def get_noch_zu_zahlen(self):
        return self.noch_zu_zahlen

# die Vereinbahrung der Klasse für den Automaten
class Getraenkeautomat:
    # Getränke werden erzeugt
    getraenk1 = Getraenke("Limonade", 10, 10)
    getraenk2 = Getraenke("Wasser", 8, 10)
    getraenk3 = Getraenke("Bier", 13, 10)

    getraenkeListe = []

    getraenkeListe.append(getraenk1)
    getraenkeListe.append(getraenk2)
    getraenkeListe.append(getraenk3)

    # init Methode mit einer Referenz auf die Münzeneinheit
    def __init__(self, temp_zahlomat):
        # die Attribute
        # jetz ist die Muenzeneinheit Teil des Automaten
        self.zahlomat = temp_zahlomat

        # die Kühlung ist aus
        self.kuehlung = False

    def __del__(self):
        print("Eine Instanz der Klasse Getraenkeautomat wurde gelöscht.")

    def getraenke_waehlen(self):
        # die Auswahl
        print("Bitte wählen Sie ein Getränkt.")
        print("Es gibt folgende Auswahl:")
        anzeige_auswahl = 1

        for getraenk in self.getraenkeListe:
            print(anzeige_auswahl, getraenk.get_getraenke_name())
            anzeige_auswahl = anzeige_auswahl+1

        auswahl = int(input("Geben Sie die gewünschte Nummer ein:"))
        getraenk_auswahl = self.getraenkeListe[auswahl - 1]

        #Bestandsprüfung/Bestandsermittlung
        lagerbestand = getraenk_auswahl.get_getraenke_anzahl()
        # gibt es Flaschen von dem Gewaeltem Getränk?

        if lagerbestand <= 0:
            print("Das gewählte Getränkt ist leider nicht mehr vorhanden.")
            auswahl = -1
            return auswahl
        else:
            # die Anzahl der Flaschen einlesen
            anzahl = int(input("Wie viele Flaschen möchten Sie?"))

            #prüfe ob genugend Flaschen zur Verfügung stehen
            if anzahl > lagerbestand:
                anzahl = lagerbestand
                print("Es sind nur noch", lagerbestand, "Flaschen", getraenk_auswahl.get_getraenke_name(), "vorhanden")
                print("Sie erhalten den Rest")

            #Zahlvorgang
            print("Sie müssen", anzahl * getraenk_auswahl.get_getraenke_preis(), "Cent bezahlen.")
            self.zahlomat.set_beitrag(anzahl * getraenk_auswahl.get_getraenke_preis())

            while self.zahlomat.get_noch_zu_zahlen() > 0:
                print("Es fehlen noch", self.zahlomat.get_noch_zu_zahlen(), "Cent.")
                self.zahlomat.muenzen_annehmen(3)

            # Ausgabe des Getränkes und evtl Rückgabe des Geldes
            if self.zahlomat.get_noch_zu_zahlen() < 0:
                print("Sie erhalten", abs(self.zahlomat.get_noch_zu_zahlen()), "Cent als Rückgeld zurück")

            if self.zahlomat.get_noch_zu_zahlen()<= 0:
                self.getraenk_ausgeben(anzahl, getraenk_auswahl)

    def getraenk_ausgeben(self, anzahl, getraenk_auswahl):
        getraenk_auswahl.set_anzahl(anzahl)
        print("Sie erhalten",anzahl, getraenk_auswahl.get_getraenke_name(), "Flasche/n.")

    def kuehlen(self, an_aus):
        self.kuehlung = an_aus
        if self.kuehlung == True:
            print("Kühlung ist eingeschaltet.")
        else:
            print("Kühlung ist ausgeschaltet.")


# eine Münzeneinheit erzeugen
einheit = Muenzeneinheit()
# einen Automaten erzeugen
# die Münzen und die Anzhal der Getränke werden übergeben
automat = Getraenkeautomat(einheit)

auswahl = -1
# die Kühlung einschalten
automat.kuehlen(True)
# ein Getränk auswählen
while auswahl == -1:
    auswahl = automat.getraenke_waehlen()

# die Kühlung einschalten
automat.kuehlen(False)

# die Instanzen ausdrücklich freigeben
# zuerst der Automat
del automat
# und die Münzeneinheit
del einheit

