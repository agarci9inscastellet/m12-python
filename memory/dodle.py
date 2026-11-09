import cartes
from color import Color
import random
import time
import os

def encetaSimbol():
    ###
    ###
    ###
    return True/False
 
 
joc = menu()
if joc == 4: 
    pila = cartes.cartes4.copy() #fem un còpia de les cartes
elif joc == 5:
    pila = cartes.cartes5.copy() #fem un còpia de les cartes

    
random.shuffle(pila) #barregem la pila

encerts = 0
errors = 0
carta = pila.pop() #agafem la primera carta
restants = "[Aquí guardem quantes cartes queden a la pila]"

TempsInici = int(time.perf_counter()) #mirem el temps a l'inici
while pila:
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{Color.BLANC}Encerts: {Color.VERD}{encerts}{Color.BLANC} | Errors: {Color.VERMELL}{errors} {Color.BLANC}| Cartes restants: {Color.GROC}{restants}")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    ###############################################3
    print(carta)
    novacarta = pila.pop()
    
    print(novacarta)
    encert = encertaSimbol()
    if encert:
        encerts += 1
    else:
        errors += 1

    print("...Compta encerts/errors...")
    
    

tempsFinal = int(time.perf_counter()) #mirem el tremps al final

print("-------------------------------------------------")
print("------------------  RESULTAT  -------------------")
print("-------------------------------------------------")

print(f"{Color.BLANC}Temps: {Color.VERD}", "[Aquí es mostra el temps]")
print(f"{Color.BLANC}Penalització: (5s per cada error) ","[Aquí es mostren els errors]")
print(f"{Color.BLANC}Resultat: {Color.BLAU}","[Aquí es mostra el temps amb penalitzacio]")


