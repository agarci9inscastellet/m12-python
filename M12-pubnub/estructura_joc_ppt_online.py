from pubnub_lx import *
import random

#########################################################################
#########################################################################
#########################################################################
# PREPAREM EL JOC
#
# Fem login. Mentre desenvolupem, en lloc de login fem un nom random    
# username=login()
username="user"+str(random.randint(0, 99))

## Creació del canal del joc
pubn=Pubnub_lx(username,"game") # "game" és el nom de la teva aplicació
#mytorn = pubn.mytorn
jugada_teva = False
#########################################################################
#########################################################################
#########################################################################
# BUCLE PRINCIPAL
while True:
    while True:
    #########################################################################
    #juga l'oponent (si comences tu, retorna False)
    #########################################################################
        jugada_oponent = pubn.play_opponent()
        if jugada_oponent:
            #print(pubn.contrincant_id," ha jugat ", jugada_oponent)
            print(pubn.contrincant_id," ha jugat! ")
            #processa la jugada de l'oponent
            #marca la jugada al tauler
            #comprova si ha guanyat, si són taules, si s'ha

        if jugada_oponent and jugada_teva:
            break
    #########################################################################
    #Jugues TU
    #########################################################################
        print (f"És el teu torn, {username}")

        # Llegeixo la jugada pel
        # teclat
        jugada_teva=input(">>>")
        #valido la jugada
            
        ####################
        # envia la jugada a l'oponent
        pubn.send(jugada_teva) 
        #######################
        
        #processa la teva jugada
        #marca la jugada al tauler
        #comprova si has guanyat, si són taules, si t'has rendit....   
        if jugada_oponent and jugada_teva:
            break  
        #break

    print(f"TU: {jugada_teva} / ELL: {jugada_oponent}")
    jugada_oponent = jugada_teva = False
pubn.stop()
print('Bye.')