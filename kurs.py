class Kurs:
    def __init__(self, kurstitel, startdatum):
        self.titel = kurstitel
        self.startdatum = startdatum
        self.aufgabenliste = []
    def add_aufgabe(self, Aufgabe):
        self.aufgabenliste.append(Aufgabe)
    def drucken(self):
        for i in self.aufgabenliste:
            print(i)


