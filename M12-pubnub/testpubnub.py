from pubnub_lx import *
import time

tauler=[[" "," "," "],[" "," "," "],[" "," "," "]]
mysimbol=""
theirsimbol=""
torn = "x" 
ready = False
tim = time.time()

def print_tauler():
    global  tauler
    print(f"┌───┬───┬───┐")
    print(f"│ {tauler[0][0]} │ {tauler[0][1]} │ {tauler[0][2]} │") 
    print(f"├───┼───┼───┤")   
    print(f"│ {tauler[1][0]} │ {tauler[1][1]} │ {tauler[1][2]} │") 
    print(f"├───┼───┼───┤")   
    print(f"│ {tauler[2][0]} │ {tauler[2][1]} │ {tauler[2][2]} │") 
    print(f"└───┴───┴───┘") 
    


def pubnub_listener(publisher, message):
    global  tauler, ready, mysimbol, theirsimbol, tim, pubnub, torn
    #print(f"[{publisher}]<<< {message}\n>>>\n\n")
    if message.startswith("ready"):
        ready = True
        #print (f"zzzzz {message} zzzzzzzzzz ready:{tim}")
        mysimbol = "x" if message > f"ready:{tim}" else "o"
        theirsimbol = "o" if mysimbol == "x" else "x"
        print ("El teu símbol: ",mysimbol)
        if mysimbol == torn:
            print ("És el teu torn")
        return
            
   
    coord = message.split(",")
    tauler[int(coord[0])][int(coord[1])]=theirsimbol
    print_tauler()
    print (check_winner(tauler))
    torn = mysimbol
    print ("És el teu torn")


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


    
userid=input("El teu nom? ")
pubn=Pubnub_lx(userid,"game",pubnub_listener)
while not ready:
    publish_result = pubn.send( f"ready:{tim}") 
    print (f"ready ... {ready} - {tim} >>> Esperant connexió")
    time.sleep(0.5)


pubn.send(f"ready:{tim}") 
print_tauler()

while True:
    if  mysimbol != torn:
        print ("Esperant jugada...")
    while  mysimbol != torn:
        time.sleep(0.1)
    torn=theirsimbol
    msg=input(">>>")
    publish_result = pubn.send(msg) 
    coord = msg.split(",")
    tauler[int(coord[0])][int(coord[1])]=mysimbol
    print_tauler()
    print (check_winner(tauler))
    
    if msg=="quit":
        break



pub.stop()
print('Bye.')