from pubnub_lx import *
import random

tauler=[[" "," "," "],[" "," "," "],[" "," "," "]]
simbol=["x","o"]
mytorn = 0

def print_tauler():
    global  tauler
    print(f"┌───┬───┬───┐")
    print(f"│ {tauler[0][0]} │ {tauler[0][1]} │ {tauler[0][2]} │") 
    print(f"├───┼───┼───┤")   
    print(f"│ {tauler[1][0]} │ {tauler[1][1]} │ {tauler[1][2]} │") 
    print(f"├───┼───┼───┤")   
    print(f"│ {tauler[2][0]} │ {tauler[2][1]} │ {tauler[2][2]} │") 
    print(f"└───┴───┴───┘") 
    
def jugada_valida(coord, tauler):
    if coord not in ["00","01","02","10","11","12","20","21","22"]:
        return False
    if tauler[int(coord[0])][int(coord[1])] != " ":
        return False
    return True

def check_winner(grid):
    n = len(grid)  # Assuming grid is square (n x n)
    winners = []

    # Check rows for a winner
    for row in grid:
        if len(set(row)) == 1 and row[0] != " ":  # Ensure all elements are the same and not empty
            winners.append(("row", grid.index(row), row[0]))

    # Check columns for a winner
    for col in range(n):
        column = [grid[row][col] for row in range(n)]
        if len(set(column)) == 1 and column[0] != " ":
            winners.append(("column", col, column[0]))

    # Check main diagonal
    main_diagonal = [grid[i][i] for i in range(n)]
    if len(set(main_diagonal)) == 1 and main_diagonal[0] != " ":
        winners.append(("main_diagonal", 0, main_diagonal[0]))

    # Check anti-diagonal
    anti_diagonal = [grid[i][n - i - 1] for i in range(n)]
    if len(set(anti_diagonal)) == 1 and anti_diagonal[0] !=  " ":
        winners.append(("anti_diagonal", 0, anti_diagonal[0]))

    return winners


    
#userid=input("El teu nom? ")
userid="user"+str(random.randint(0, 99))
## Creació del canal del joc
pubn=Pubnub_lx(userid,"game") # "game" és el nom de la teva aplicació
#miro qui comença
mytorn = pubn.mytorn
print_tauler()

#########################################################################
#########################################################################
#########################################################################
while True:
    #juga l'oponent (si comences tu, retorna False)
    coord = pubn.play_opponent()
    if coord:
        print(pubn.contrincant_id," ha jugat")
        tauler[int(coord[0])][int(coord[1])]=simbol[not mytorn]
        print_tauler()
        win = check_winner(tauler)
        if win:
            print ("Ha guanyat ",pubn.contrincant_id)
            break

    #Jugues TU
    print (f"És el teu torn, {userid}")

    while True:
        # Llegeico la jugada pel teclat
        coord=input(">>>")
        #valido la jugada
        if jugada_valida(coord, tauler):
            break
        print("Jugada no vàlida!. Torna a jugar")
        
    ####################
    # envia la jugada
    pubn.send(coord) 
    #######################
    tauler[int(coord[0])][int(coord[1])]=simbol[mytorn]
    print_tauler()
    win = check_winner(tauler)
    if win:
        print ("Has guanyatm ",userid)
        break



pubn.stop()
print('Bye.')