from colorama import Fore, Back, Style, init
init(autoreset=True)

cols = rows = 5
tauler = [[" " for x in range(5)] for y in range(53)] # x = width, y = height
tauler2 = [[" " for x in range(5)] for y in range(53)]

def print_tauler(tauler, bcolor, tauler2, bcolor2):
    def colored(txt):
        bg = bcolor2 if t2 else bcolor
        if txt=="A":
            txt= Back.BLUE+txt+bg
        if txt=="T":
            txt = Back.YELLOW + txt + bg
            
        if txt=="H":
            txt = Back.RED + txt + bg
        if txt.isnumeric():
            txt = Back.MAGENTA + txt + bg

   
        
        return txt
    
    sep=15
    t2=False
    print(Style.RESET_ALL)
    print(bcolor)
    print(bcolor+f"    1   2   3   4   5  "+Back.BLACK+" "*sep+bcolor2+"    1   2   3   4   5  ")
    print(bcolor+f"  ┌───┬───┬───┬───┬───┐"+Back.BLACK+" "*sep+bcolor2+"  ┌───┬───┬───┬───┬───┐")
    print(bcolor+f" A│ {colored(tauler[0][0])} │ {colored(tauler[0][1])} │ {colored(tauler[0][2])} │ {colored(tauler[0][3])} │ {colored(tauler[0][4])} │",end="") 
    t2=True
    print(Back.BLACK+" "*sep+bcolor2+f" A│ {colored(tauler2[0][0])} │ {colored(tauler2[0][1])} │ {colored(tauler2[0][2])} │ {colored(tauler2[0][3])} │ {colored(tauler2[0][4])} │") 
    print(bcolor+f"  ├───┼───┼───┼───┼───┤"+Back.BLACK+" "*sep+bcolor2+"  ├───┼───┼───┼───┼───┤")   
    t2=False
    print(bcolor+f" B│ {colored(tauler[1][0])} │ {colored(tauler[1][1])} │ {colored(tauler[1][2])} │ {colored(tauler[1][3])} │ {colored(tauler[1][4])} │",end="") 
    t2=True
    print(Back.BLACK+" "*sep+bcolor2+f" B│ {colored(tauler2[1][0])} │ {colored(tauler2[1][1])} │ {colored(tauler2[1][2])} │ {colored(tauler2[1][3])} │ {colored(tauler2[1][4])} │") 
    print(bcolor+f"  ├───┼───┼───┼───┼───┤"+Back.BLACK+" "*sep+bcolor2+"  ├───┼───┼───┼───┼───┤")   
    t2=False
    print(bcolor+f" C│ {colored(tauler[2][0])} │ {colored(tauler[2][1])} │ {colored(tauler[2][2])} │ {colored(tauler[2][3])} │ {colored(tauler[2][4])} │",end="") 
    t2=True
    print(Back.BLACK+" "*sep+bcolor2+f" C│ {colored(tauler2[2][0])} │ {colored(tauler2[2][1])} │ {colored(tauler2[2][2])} │ {colored(tauler2[2][3])} │ {colored(tauler2[2][4])} │") 
    print(bcolor+f"  ├───┼───┼───┼───┼───┤"+Back.BLACK+" "*sep+bcolor2+"  ├───┼───┼───┼───┼───┤")   
    t2=False
    print(bcolor+f" D│ {colored(tauler[3][0])} │ {colored(tauler[2][1])} │ {colored(tauler[3][2])} │ {colored(tauler[3][3])} │ {colored(tauler[3][4])} │",end="") 
    t2=True
    print(Back.BLACK+" "*sep+bcolor2+f" D│ {colored(tauler2[3][0])} │ {colored(tauler2[2][1])} │ {colored(tauler2[3][2])} │ {colored(tauler2[3][3])} │ {colored(tauler2[3][4])} │") 
    print(bcolor+f"  ├───┼───┼───┼───┼───┤"+Back.BLACK+" "*sep+bcolor2+"  ├───┼───┼───┼───┼───┤")   
    t2=False
    print(bcolor+f" E│ {colored(tauler[4][0])} │ {colored(tauler[4][1])} │ {colored(tauler[4][2])} │ {colored(tauler[4][3])} │ {colored(tauler[4][4])} │",end="") 
    t2=True
    print(Back.BLACK+" "*sep+bcolor2+f" E│ {colored(tauler2[4][0])} │ {colored(tauler2[4][1])} │ {colored(tauler2[4][2])} │ {colored(tauler2[4][3])} │ {colored(tauler2[4][4])} │") 
    print(bcolor+f"  └───┴───┴───┴───┴───┘"+Back.BLACK+" "*sep+bcolor2+"  └───┴───┴───┴───┴───┘") 
    print(Style.RESET_ALL)

###################
### COORDENADES D'EXEMPLE    
tauler[0][1]="2"
tauler[0][2]="2"
tauler[1][4]="3"
tauler[2][4]="3"
tauler[3][4]="3"


tauler2[0][0]="A"
tauler2[0][2]="T"
tauler2[2][2]="H"
tauler2[3][2]="H"

print_tauler(tauler, Back.GREEN, tauler2, Back.CYAN)
    
