from pubnub_lx import *
import random

tauler=[]


def print_tauler():
    global  tauler
    #cal pintar també les jugades dins de les cel.les
    print(f"┌───┬───┬───┐")
    print(f"│   │   │   │") 
    print(f"├───┼───┼───┤")   
    print(f"│   │   │   │") 
    print(f"├───┼───┼───┤")   
    print(f"│   │   │   │") 
    print(f"└───┴───┴───┘") 
    
def jugada_valida(coord, tauler):
    #comprova que la jugada és vàlida
    #que la casella no està ocupada
    return True

def check_winner(grid):
    #compreva si ha guanyat
    return False


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

#miro qui comença. mytorn serà 0 (començo jo) o 1
mytorn = pubn.mytorn
#pinto el tauler buit
print_tauler()


#########################################################################
#########################################################################
#########################################################################
# BUCLE PRINCIPAL

while True:
    #########################################################################
    #juga l'oponent (si comences tu, retorna False)
    #########################################################################
    coord = pubn.play_opponent()
    if coord:
        print(pubn.contrincant_id," ha jugat ", coord)
        
        #####################
        #processa la jugada de l'oponent
        #marca la jugada al tauler
        print_tauler()   
        #comprova si ha guanyat, si són taules, si s'ha rendit....     
        win = check_winner(tauler)
        if win:
            print ("Ha guanyat ",pubn.contrincant_id)
            break

    #########################################################################
    #Jugues TU
    #########################################################################
    print (f"És el teu torn, {username}")

    # Fem un bucle fins que faci una jugada vàlida
    while True:
        # Llegeixo la jugada pel teclat
        coord=input(">>>")
        #valido la jugada
        if jugada_valida(coord, tauler):
            break
        print("Jugada no vàlida!. Torna a jugar")
        
    ####################
    # envia la jugada a l'oponent
    pubn.send(coord) 
    #######################
    
    #processa la tea jugada
    #marca la jugada al tauler
    print_tauler()   
    #comprova si has guanyat, si són taules, si t'has rendit....     
    win = check_winner(tauler)
    if win:
        print ("Has guanyat ",username)
        break



pubn.stop()
print('Bye.')