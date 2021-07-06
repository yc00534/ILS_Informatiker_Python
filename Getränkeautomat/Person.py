#die Vereinbarung der Klasse Person
class Person:
    #die Methode init
    def __init__(self, t_name, t_geschlecht):
        self.name = t_name
        self.geschlecht = t_geschlecht

    #die Methode liefert den Namen zurück
    def get_name(self):
        return self.name

    #die Methode liefer Geschlecht zurück
    def get_geschlecht(self):
        return self.geschlecht

    def __del__(self):
        print("Eine Instanz der Klasse Person wurde gelöscht")

