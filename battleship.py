from api_login import *

def login():
    while True:    
        nom = input("nom_: ")
        passw =  input("passw")
        
        if api_login("chess",nom, passw):
            print("Has entrat")
            break
            
        print ("MAAAL! Torna-hi!")
        
        
login()