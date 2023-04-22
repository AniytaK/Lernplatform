# Lerninhalt testen
from aufgabe import Lerninhalt
l2 = Lerninhalt('EDA', "viele Bibliotheken")
print(l2)
print (l2.dump())

# Lerninhalt testen
from aufgabe import Aufgabe
a1 = Aufgabe('SAD', 'Klassen und Webapplikationen müsste man kennen', 'Projektarbeit', '1.1.2023', '3.6.2023')
print (a1.dump())

a2 = a1
print(a2)

a3 = Aufgabe('Dashboard', 'Gruppenarbeit machen wir hier nicht', 'Aufgabenblatt', '22.4.2023', '28.4.2023')
print(a3)
a2.startdatum = "12.23.2345"
print(a1.startdatum)
print(a2.startdatum)
print(a3.startdatum)


# Klasse testen
from kurs import Kurs
k1 = Kurs('01.01.2023', '07.08.2023')
k1.add_aufgabe(a1)
k1.add_aufgabe(a2)
k1.drucken()
