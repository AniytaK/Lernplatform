from aufgabe import Aufgabe
a1 = Aufgabe('25.4.2023', '27.4.2023')

print(a1)

a1.drucken()

a2 = a1
print(a2)

a3 = Aufgabe('25.5.2023', '27.5.2023')
print(a3)
a2.startdatum = "12.23.2345"
print(a1.startdatum)
print(a2.startdatum)
print(a3.startdatum)

