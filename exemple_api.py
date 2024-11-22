from api_login import *


# URL examples
# http://www.castelletm12b.cat/api.php?a=userlist&app=lx
# http://www.castelletm12b.cat/api.php?a=login&app=lx&name=pepe&pass=pepe_db
# http://www.castelletm12b.cat/api.php?a=register&app=lx&name=pepe2&pass=pepe2_db

#exemple de registre d'usuari
print ("\nRegistrem per la app1, usuari=pepe3 amb pass=pepe3_pass ")
print(api_register("app1","pepe3","pepe3_pass"))



#exemple de login exitos
print ("\nFem login per la app1, usuari=pepe3 amb pass=pepe3_pass ")
print(api_login("app1","pepe3","pepe3_pass"))



#exemple de login sense exit
print ("\nFem login per la app1, usuari=pepe3 amb pass=wrong_pass ")
print(api_login("app1","pepe3","wrong_pass"))



#exemple de consulta d'usuaris
print ("\nLlistem usuaris per app1:")
print(api_userlist("app1"))



# exemple bucle login
while True:
    nom_aplicacio  ="app1"
    username = input("Nom: ")
    passw = input ("Contrasenya: ")
    
    
    if api_login(nom_aplicacio, username, passw):
        print ("HAS ENTRAT!")
        break
    else:
        print ("El login ha fallat, Torna-ho a intentar... ")
        
        