from pubnub_eloy import *

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


    
    def next_torn(torn):
        import random
        torn = [0, 1]
        ## AIXÒ HO FARÀ EL LOGIN
        name[0] = input("Indica el teu nom")
        name[1] = input("Indica el teu nom")
        torn = random.randint(0, 1)
        return 1 - torn
        
    #score
    def mira_qui_guanya(name, score):
        global jugada
        guanyador=3
        #R, P, T
        if jugada[0] == "R" and jugada[1] == "R":
            guanyador = 2
        elif jugada[0] == "R" and jugada[1] == ("P"):
            guanyador = 1
        elif jugada[0] == "R" and jugada[1] == ("T"):
            guanyador = 0

        elif jugada[0] == "T" and jugada[1] == "T":
            guanyador = 2
        elif jugada[0] == "T" and jugada[1] == "R":
            guanyador = 1
        elif jugada[0] == "T" and jugada[1] == "P":
            guanyador = 0

        elif jugada[0] == "P" and jugada[1] == "P":
            guanyador = 2
        elif jugada[0] == "P" and jugada[1] == ("T"):
            guanyador = 1
        elif jugada[0] == "P" and jugada[1] == "R":
            guanyador = 0

        elif jugada[1] == "R" and jugada[0] == "R":
            guanyador = 2
        elif jugada[1] == "R" and jugada[0] == "P":
            guanyador = 1
        elif jugada[1] == "R" and jugada[0] == "T":
            guanyador = 0

        elif jugada[1] == "T" and jugada[0] == ("T"):
            guanyador = 2
        elif jugada[1] == "T" and jugada[0] == ("R"):
            guanyador = 1
        elif jugada[1] == "T" and jugada[0] == ("P"):
            guanyador = 0

        elif jugada[1] == "P" and jugada[0] == "P":
            guanyador = 2
        elif jugada[1] == "P" and jugada[0] == "T":
            guanyador = 1
        elif jugada[1] == "P" and jugada[0] == "R":
            guanyador = 0

        score[guanyador] += 1
        
        return guanyador


    def print_score(score):
        global name
        #print(score)
        print("\n\n")
        print("PUNTUACIONS")
        print(name[0]," -> ",score[0])
        print(name[1]," -> ",score[1])
        print("\n\n")

    ## PREGUNTA QUANTES PATIDES
    #num_partides_a_guanyar = int(input(" Quantes partides vol guanyar un jugador? "))
    num_partides_a_guanyar=3
    
    partida_en_proces = True
    mytorn = pubn.mytorn


    while True:   
        pubn.reset()        
        print(f"Juga {name[0]}")
        jugada[0] = input("Tria jugada (R,P,T): ").upper()
        pubn.send( jugada[0])
        print("Esperant jugada de l'oponent...")
        
        jugada[1]  = pubn.play_opponent()
        print(pubn.contrincant_id," ha jugat ", jugada[1])        
        
        pubn.reset()

        # print(f"Juga {name[1]}")
        # jugada[1] = input("Tria jugada (R,P,T): ").upper()

       
    
    

        guanyador = mira_qui_guanya(name, score)
        print("guanya ", name[guanyador])
        print_score(score)

        num_partides_a_guanyar -= 1

        if not num_partides_a_guanyar:
            print("FINAL DEL JOC")
            exit()
        
        #   DEF guarda partida??  SI UN DELS DOS ARRIBA A LES PARTIDES
        #
        #
        #   1 Register
        #   2 Login

        #   1 Jugar
        #   2 Veure partida guardada


        def guarda_partida(name, score):
            partida = score
            if score == 3:
                print("guanya", name)
                