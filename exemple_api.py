from api_login import *


# URL examples
# http://www.castelletm12b.cat/api.php?a=userlist&app=lx
# http://www.castelletm12b.cat/api.php?a=login&app=lx&name=pepe&pass=pepe_db
# http://www.castelletm12b.cat/api.php?a=register&app=lx&name=pepe2&pass=pepe2_db

#alex mypasswordzz
#testuser mypassword
#pepe 1234


#exemple de registre d'usuari
print ("\nRegistrem per la app1, usuari=pepe amb pass=1234 ")
print(api_register("chess", "pepe","1234"))


#exemple de login sense exit
print ("\nFem login per la app1, usuari=alex amb pass=mypasswordzz ")
print(api_login("chess","alex","mypasswordzz"))


#exemple de consulta d'usuaris
print ("\nLlistem usuaris per chess:")
print(api_userlist("chess"))



# exemple bucle login
while True:
    nom_aplicacio  ="chess"
    username = input("Nom: ")
    passw = input ("Contrasenya: ")
    
    
    if api_login(nom_aplicacio, username, passw):
        print ("HAS ENTRAT!")
        break
    else:
        print ("El login ha fallat, Torna-ho a intentar... ")
        
        
