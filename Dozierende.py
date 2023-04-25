
class Dozierende:
    def __init__(self, vorname, name, kurs):
        self.vorname = vorname
        self.name = name
        self.kurs = kurs

    def sich_vorstellen(self):
        print("Mein Name ist " +self.vorname+" " + self.name)
        print("Ich bin Dozent in " +self.kurs + " Kurs")

d1 = Dozierende("Muster", "Max", "Python")
d2 = Dozierende("Kunt", "Tom", "Design")

d1.sich_vorstellen()
d2.sich_vorstellen()