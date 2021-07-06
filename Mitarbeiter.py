#die Klasse Mitarbeiter erbt von der Klasse Person
from Getränkeautomat.Person import Person


class Mitarbeiter(Person):
    #die Methode init
    def __init__(self, t_name, t_geschlecht, t_gehalt):
        super().__init__(t_name, t_geschlecht)
        self.gehalt = t_gehalt

    def get_gehalt(self):
        return self.gehalt

#    def __del__(self):
#        print("Eine Instanz der Klasse Mitarbeiter wurde gelöscht")


person1=Person("Hans","m")
mitarbeiterin1 = Mitarbeiter("Konigunde", "w", 2000)

#die Werte der Attribute ausgeben
print("Die Person heißt", person1.get_name()+",","hat das Geschlecht", person1.get_geschlecht())
print("Der Mitarbeiter heißt",mitarbeiterin1.get_name()+",","hat das Geschlecht",mitarbeiterin1.get_geschlecht(),"und verdient",mitarbeiterin1.get_gehalt())

del person1
del mitarbeiterin1