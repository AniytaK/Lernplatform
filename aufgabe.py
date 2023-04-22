class Aufgabe:
    def __init__(self, startdatum, enddatum):
        self.startdatum = startdatum
        self.enddatum = enddatum

    def __str__(self):
        return f"Startdatum: {self.startdatum}, Enddatum: {self.enddatum}"

    def drucken(self):
        print("Hello die Aufgabe wird am " + self.enddatum + " enden.")

class Kurs():
    def __init__(self):
        self.aufgabenliste = []
    def add_aufgabe(self, Aufgabe):
        self.aufgabenliste.append(Aufgabe)
    def drucken(self):
        for i in self.aufgabenliste:
            print(i)
