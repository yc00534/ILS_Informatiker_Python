from Katze import Katze


class Elternkatze(Katze):
    def __init__(self, t_anzahl_kinder, t_große, t_gewicht):
        super().__init__(t_große, t_gewicht)
        self.anzahl_kinder = t_anzahl_kinder

    def get_anzahlKinder(self):
        return self.anzahl_kinder


TestKatze = Katze(10, 22)
print(TestKatze.get_große(), TestKatze.get_gewicht())

TestElternkatze = Elternkatze(1, 2, 3)
print(TestElternkatze.get_anzahlKinder(), TestElternkatze.get_gewicht(), TestElternkatze.get_große())
