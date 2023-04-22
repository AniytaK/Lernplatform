class Aufgabe:
    def __init__(self, startdatum, enddatum):
        self.startdatum = startdatum
        self.enddatum = enddatum
    def __str__(self):
        return f"Startdatum: {self.startdatum}, Enddatum: {self.enddatum}"
    def drucken(self):
        print("Hello die Aufgabe wird am " + self.enddatum + " enden.")


