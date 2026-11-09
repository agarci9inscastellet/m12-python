import cartes
from color import Color
import random
import time
import os

 
pila = cartes.cartes4.copy() #fem un còpia de les cartes
random.shuffle(pila) #barregem la pila

encerts = 0
errors = 0
carta = pila.pop() #agafem la primera carta
inici = time.perf_counter() #mirem el tremps a l'inici

while pila:
    os.system("cls" if os.name == "nt" else "clear")
    
    cartauser = pila.pop() #agafem una nova carta
    rest = len(pila)
    print(f"{Color.BLANC}Encerts: {Color.VERD}{encerts}{Color.BLANC} | Errors: {Color.VERMELL}{errors} {Color.BLANC}| Cartes restants: {Color.GROC}{rest}")
    print("-------------------------------------------------")
    print(carta)
    print(cartauser)
    
    n=int(input("\nQuin element coincideix?"))
    if (cartauser[n-1] in carta):
        #print("Molt bé!")
        encerts +=1
    else:
        #print({Color.VERMELL},"\n\nNooo\n\n")
        errors +=1

final = time.perf_counter() #mirem el tremps a l'inici
print("\n\n")
print(f"{Color.BLANC}Temps: {Color.VERD}",int(final-inici))
print(f"{Color.BLANC}Penalització: (5s per cada error) ",errors*5)
print(f"{Color.BLANC}Resultat: {Color.BLAU}",int((final-inici)+errors*5))