from api_login import *


# URL examples
# http://www.castelletm12b.cat/api.php?a=userlist&app=lx
# http://www.castelletm12b.cat/api.php?a=login&app=lx&name=pepe&pass=pepe_db
# http://www.castelletm12b.cat/api.php?a=register&app=lx&name=pepe2&pass=pepe2_db

#alex mypasswordzz
#testuser mypassword
#pepe 1234

'''
#exemple de registre d'usuari
print ("\nRegistrem per la app 'pedra', usuari=andres amb pass=1234 ")
print(api_register("pedra", "andres","1234"))


#exemple de registre d'usuari
# print ("\Esborrem per la app 'chess', usuari=userdel amb pass=1234 ")
# print(api_deleteuser("chess", "userdel","1234"))



#exemple de login sense exit
print ("\nFem login per la app 'pedra', usuari=adrian amb pass=1234")
print(api_login("pedra","adrian","1234"))


#exemple de consulta d'usuaris
print ("\nLlistem usuaris per blackjack:")
print(api_userlist("blackjack"))

'''

# exemple bucle login
while True:
    nom_aplicacio  ="blackjack"
    username = input("Nom: ")
    passw = input ("Contrasenya: ")
    
    
    if api_login(nom_aplicacio, username, passw):
        print ("HAS ENTRAT!")
        break
    else:
        print ("El login ha fallat, Torna-ho a intentar... ")
        
 
