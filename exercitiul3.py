#Modelează un cont bancar folosind o clasă ContBancar, apoi creează mai multe conturi și mută bani între ele.

#Clasa ContBancar are proprietățile:

#titular — numele proprietarului (string)
#sold — banii din cont (număr, pornește de la o valoare inițială)

#Și metodele:

#depune(suma) — adaugă suma la sold; refuză sumele ≤ 0
#retrage(suma) — scade suma din sold; refuză dacă suma e ≤ 0 sau mai mare decât soldul
#transfera(suma, alt_cont) — mută suma din contul curent în alt_cont
#afiseaza() — tipărește titularul și soldul curent

#Scriptul principal trebuie să:

#Creeze cel puțin 2 conturi cu titulari și solduri diferite
#Facă o depunere și o retragere pe unul dintre ele
#Facă un transfer dintr-un cont în celălalt
#Afișeze soldurile finale ale ambelor conturi

class ContBancar:
    def __init__(self, titular, sold):
        self.titular = titular
        self.sold = sold

    def depune(self, suma):
        if suma > 0:
            self.sold = self.sold + suma
        else:
            print("Suma trebuie sa fie mai mare decat 0.")

    def retrage (self, suma):
        if suma > 0 and suma <= self.sold:
            self.sold = self.sold - suma
        else:
            print("Suma nu este validă sau depășește soldul disponibil.")

    def transfera(self, suma, cont2):
        if suma > 0 and suma <= self.sold:
            self.sold = self.sold - suma
            cont2.sold = cont2.sold + suma
        else:
            print("Suma nu este validă sau depășește soldul disponibil.")

    def afiseaza(self):
        print(f"Titular: {self.titular}, Sold: {self.sold}")



cont1 = ContBancar("Ion Popescu", 2500)
cont1.depune(500)
cont1.retrage(300)
cont1.afiseaza()

cont2 = ContBancar("Maria Ionescu", 1440)
cont2.depune(-3)
cont2.retrage(1600)
cont2.afiseaza()


    
