from api_login import *

def login():
    while True:    
        nom = input("nom_: ")
        passw =  input("passw")
        
        if api_login("app1",nom, passw):
            print("Has entrat")
            break
            
        print ("Torna-hi!")
        
        
login()