class Test:
    def __init__(self, wert):
        self.ein_Wert = wert
        print(self.ein_Wert*2)

    def __del__(self):
        print("Eine Instanz der Klasse Test wurde gelöscht")

test = Test(4711)
