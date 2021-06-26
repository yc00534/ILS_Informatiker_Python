#die Vereinbarung der Klasse für die Münzeneinheit
class Muenzeneinheit:
    def init(self):
        self.betrag = 0
        self.noch_zu_zahlen = 0
        self.rueckgeld = 0

    def muenzen_annehmen(self, wert):
        self.noch_zu_zahlen=self.noch_zu_zahlen-wert

    def rueckgeld_geben(self):
        self.rueckgeld = abs(self.noch_zu_zahlen)
        return self.rueckgeld

    def set_beitrag(self, preis):
        self.betrag = preis
        self.noch_zu_zahlen = self.betrag

    def get_noch_zu_zahlen(self):
        return self.noch_zu_zahlen