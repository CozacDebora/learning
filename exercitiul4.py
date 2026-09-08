#Un mini-magazin: produse cu stoc și un coș de cumpărături care le adună.

#Clasa Produs:

#nume (str), pret (float), stoc (int) — câte bucăți sunt disponibile
#afiseaza() — tipărește nume, preț, stoc

#Clasa Cos:

#ține o colecție de produse adăugate, fiecare cu cantitatea lui
#adauga(produs, cantitate):
#refuză dacă cantitate <= 0
#refuză dacă produs.stoc < cantitate (nu ai destul pe raft)
#altfel: scade din produs.stoc și pune în coș; dacă produsul e deja în coș, cumulează cantitatea
#elimina(nume_produs) — scoate complet produsul din coș și pune stocul înapoi
#total() — returnează suma pret * cantitate pe tot coșul
#afiseaza() — listează fiecare linie (produs, cantitate, subtotal) + totalul general

#Scriptul principal trebuie să:

#creeze 3-4 produse cu prețuri și stocuri diferite
#adauge câteva produse în coș, inclusiv un caz care depășește stocul (ca să vezi refuzul)
#adauge același produs de două ori (ca să testezi cumularea)
#afișeze coșul cu totalul
#elimine un produs și reafișeze

class Produs:
    def __init__(self, nume, pret, stoc):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc

    def afiseaza(self):
        print(f"Produs: {self.nume}, Pret: {self.pret}, stoc: {self.stoc}")

class Cos:
 def __init__(self):
        self.produse = []

 def adauga(self, produs, cantitate):

    if cantitate <= 0:
        print("Cantitatea trebuie sa fie mai mare decat 0")
        return

    if produs.stoc < cantitate:
        print(f"Nu avem destule produse in stoc pentru {produs.nume}.")
        print(f"Stoc disponibil: {produs.stoc}")
        return

    produs.stoc = produs.stoc - cantitate

    for chestie in self.produse:

        #if branza (din cos) == branza (produsul pe care vr sa il adaug)

        if chestie[0] == produs:

        #daca branza e deja in cos, atunci mai adaug o branza
            chestie[1] = chestie[1] + cantitate
            return

    self.produse.append([produs, cantitate])


 def elimina(self, nume_produs):

    for chestie in self.produse:

        produs = chestie[0]
        cantitate = chestie[1]

        if produs.nume == nume_produs:
            produs.stoc = produs.stoc + cantitate
            self.produse.remove(chestie)
            return


 def total(self):

    total = 0

    for chestie in self.produse:

        produs = chestie[0]
        cantitate = chestie[1]

        pret_total = produs.pret * cantitate
        total = total + pret_total

    return total


 def afiseaza(self):

    print("Produsele din cos:")

    for chestie in self.produse:

        produs = chestie[0]
        cantitate = chestie[1]

        subtotal = produs.pret * cantitate

        print(f"- {produs.nume}: {cantitate} x {produs.pret} lei = {subtotal} lei")

    print(f"Total: {self.total()} lei")



produs1 = Produs("Branza", 10.7, 5)
produs2 = Produs("Paine", 7.5, 10)
produs3 = Produs("Lapte", 12.0, 8)

produs1.afiseaza()
produs2.afiseaza()
produs3.afiseaza()

print("""Cosul de cumparaturi:""")

cos = Cos()
cos.adauga(produs1, 3)
cos.adauga(produs2, 5)
cos.adauga(produs3, 9)

#adaugam mai mult decat exista in stoc
cos.adauga(produs3, 20)

cos.afiseaza()

print("Noul cos de cumparaturi:")

produs1.afiseaza()
produs2.afiseaza()
produs3.afiseaza()

cos.elimina("Paine")
cos.afiseaza()

produs1.afiseaza()
produs2.afiseaza()
produs3.afiseaza()


