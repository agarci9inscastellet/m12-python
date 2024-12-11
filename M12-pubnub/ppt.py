from pubnub_eloy import *
import random

# # #LOGIN
while True:
    nom_aplicació = "ppt"
    username = input ("Nom:")
    passw = input ("Contrasenya: ")
    if username == "a" and passw == 'a' or username == "b" and passw == 'b' :
        print("autorització correcta")
        break
    else:
        print("dades no validos")
    
        



while True:
    #username="a"
    
    pubn=Pubnub_lx(username,"ppt") # "game" és el nom de la teva aplicació
    oponent = pubn.contrincant_id    
    
    torn = [0, 1]
    jugada = ["", ""]
    name = [username, oponent,"Empats"]
    score = [0, 0, 0]

    mytorn = pubn.mytorn


    while True:   
        print("")
        print("")
        print("")
        print(f"{pubn.torn} --- {int(pubn.mytorn)}")

        if pubn.torn != pubn.mytorn:
            print("********************************************")
            print("***********     OPONENT     ****************")
            print("********************************************")


            jugadaop  = pubn.wait_opponent()
            print(pubn.contrincant_id," ha jugat ", jugadaop)        
            t = random.randint(0, 1)
            print("reposta RESULTAT: ",t)
            pubn.send(f"result: {t}")


        
        
        print("############################################")
        print("###########        JO       ################")
        print("############################################")
        print("")
        print("")
        print(f"Torn: {pubn.torn} --- myTorn: {int(pubn.mytorn)}")
        print("")
        print(f"Juga {name[0]}")
        jugada = input("Tria jugada: ").upper()
        pubn.send(jugada )
        print("Esperant resposta l'oponent...",end="")
        time.sleep(0.1)
        print("")
        print("")
        print("")
        print(f"{pubn.torn} --- {int(pubn.mytorn)}")

        impactop  = pubn.response_opponent()
        
        print(jugada,"--->",impactop)

        print("")
        print("")
        print("")
        print(f"{pubn.torn} --- {int(pubn.mytorn)}")
        #pubn.torn = not pubn.torn
        pubn.jugada = False
        pubn.response = False