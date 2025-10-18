import pickle


noms = ["Anna", "Marc", "Júlia", "Pau"]
noms_carregats=[]

#per guardar a un arxiu que es diu noms.pkl
# w vol dir write   b vol dir binari
# f vol dir file
# dump és el métode per a guardar
with open("noms.pkl", "wb") as f:
    pickle.dump(noms, f)


#per llegir a un arxiu que es diu noms.pkl
# r és read
# load és per carregar l'arxiu
with open("noms.pkl", "rb") as f:
    noms_carregats = pickle.load(f)

print("Llista carregada:", noms_carregats)