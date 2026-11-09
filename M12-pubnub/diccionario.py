class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'  # Resetea el color


temes = ["menjars","animals","mobles","ciutats","paisos","muntanyes"]

def reset_abecedari():
    abecedari = {chr(i): [False,False] for i in range(ord('a'), ord('z') + 1)}
    abecedari.pop('w')
    abecedari.pop('x')
    abecedari.pop('y')
    abecedari.pop('z')
    # abecedari['a'][0]="aaAA"
    # abecedari['a'][1]=1
    # abecedari['b'][0]="bbBB"
    # abecedari['b'][1]=2
    # abecedari['c'][0]="ccCC"
    # abecedari['c'][1]=1
    return abecedari