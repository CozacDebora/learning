#O sa jucam 'Fizz-buzz'. 
#Fa un program care afiseaza numerele de la 1 la 100 cu un fun spin. 
#Daca numarul afisat este divizibil cu 3 pe ecran va aparea fizz. 
#Daca numarul este divizibil cu 5 va aparea buzz. 
#Daca este divizibil cu ambele va aparea fizz-buzz.

#Exemplu: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizz-buzz, 16, ...

for numar in range(1, 101):

    if numar % 3 == 0 and numar % 5 == 0:
        print("fizz-buzz")

    elif numar % 5 == 0:
        print("buzz")

    elif  numar % 3 == 0:
        print("fizz")

    else:
        print(numar)