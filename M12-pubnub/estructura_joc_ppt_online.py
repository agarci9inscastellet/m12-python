from api_login import *
from pubnub_lx import *
import random

def login():
    return {'nom':'alex','punts':100}
    while True:
        nom_aplicacio  = "chess"
        username = input("Nom: ")
        passw = input ("Contrasenya: ")
        
        
        if api_login(nom_aplicacio, username, passw):
            punts = api_getpunts(nom_aplicacio, username, passw)
            #print ("HAS ENTRAT!", username, "Tens ",punts," punts")
            #print(api_updatepunts(nom_aplicacio, username, passw,int(input("Update punts: "))))

            break
        else:
            print ("El login ha fallat, Torna-ho a intentar... ")
    
    return {'nom':username,'punts':punts}

def resultat_joc(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empat!"
    
    if (jugador1 == 'pd' and jugador2 == 'ts') \
       or (jugador1 == 'ts' and jugador2 == 'pp') \
       or (jugador1 == 'pp' and jugador2 == 'pd'):
        return "Guanyes tu!"
    else:
        return "Guanya ell"
  
  
  
def juga():
    
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
    # lletres = "abcdefghijklmnopqrstuvz"
    # lletres = list(lletres)

    #########################################################################
    #########################################################################
    #########################################################################
    # BUCLE PRINCIPAL
    jugada_teva = False
    while True:
        while True:
        #########################################################################
        #juga l'oponent (si comences tu, retorna False)
        #########################################################################
            
            jugada_oponent = pubn.play_opponent()
            if jugada_oponent:
                print(pubn.contrincant_id," ha jugat ")
                
                #lletra = jugada_oponent[0]
                #processa la jugada de l'oponent
                #marca la jugada al tauler
                #comprova si ha guanyat, si són taules, si s'ha
                

        #########################################################################
        #Jugues TU
        #########################################################################
            print (f"És el teu torn, {username}")

            # Llegeixo la jugada pel teclat
            if not jugada_teva:
                jugada_teva=input(">>>")
                #valido la jugada
                    
                ####################
                # envia la jugada a l'oponent
                pubn.send(jugada_teva) 
                #######################
                
                #processa la teva jugada
                #marca la jugada al tauler
            if jugada_teva and jugada_oponent:
                print("Heu jugat els dos: Tu ", jugada_teva, " i ell", jugada_oponent)
            #comprova si has guanyat, si són taules, si t'has rendit....     
                print(resultat_joc(jugada_teva, jugada_oponent))
                jugada_oponent = jugada_teva = False
                break
    
    


        #pubn.stop()
        #print('Bye.')




while True:
    juga()
    # exemple bucle login
    # print("E Entrar")
    # print("R Registrar-se")
    # print("S SOrtir")
    # opcio = input("Escull una opcio: ")
    # opcio = opcio.upper()
    # if opcio == "E":
    #     user = login()
    #     print("Benvingut ",user['nom'],"Tens ",user['punts']," punts")
    #     juga()
    # elif opcio == "R":
    #     #register()
    #     print("Not implemented")
    # elif opcio == "S":
    #     exit()



