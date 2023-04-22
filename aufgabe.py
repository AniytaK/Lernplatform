class Lerninhalt:
    def __init__(self, titel, beschreibung):
        self.titel = titel
        self.beschreibung = beschreibung

    def __str__(self):
        return f"Titel: {self.titel}, Beschreibung: {self.beschreibung}"
    def dump (self):
        return self.__dict__

class Aufgabe (Lerninhalt):
    def __init__(self, titel, beschreibung, aufgabe, startdatum, enddatum):
        super().__init__(titel, beschreibung)
        self.aufgabe = aufgabe
        self.startdatum = startdatum
        self.enddatum = enddatum
    def __str__(self):
        return f"Startdatum: {self.startdatum}, Enddatum: {self.enddatum}, Titel: {self.titel}, Beschreibung: {self.beschreibung}"
    def drucken(self):
        print("Hello die Aufgabe wird am " + self.enddatum + " enden.")


