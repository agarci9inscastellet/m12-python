from api_login import *


# api_register("chess", "andres","1234")
# api_deleteuser("chess", "userdel","1234")
# api_login("chess","alex","mypasswordzz")
# api_userlist("chess")
# api_getpunts("chess","alex","mypasswordzz")
# api_updatepunts("chess","alex","mypasswordzz",43)


# URL examples
# http://www.castellet2526m12.cat/api.php?a=userlist&app=lx
# http://www.castellet2526m12.cat/api.php?a=login&app=lx&name=pepe&pass=pepe_db
# http://www.castellet2526m12.cat/api.php?a=register&app=lx&name=pepe2&pass=pepe2_db
# http://www.castellet2526m12.cat/api.php?a=updatepuntsr&app=lx&name=pepe2&pass=pepe2_db

#exemple de registre d'usuari
print ("\nRegistrem per la app 'chess', usuari=manu amb pass=1234 ")
print(api_register("chess", "manu2","1234"))

'''
#exemple de registre d'usuari
print ("\Esborrem per la app 'chess', usuari=userdel amb pass=1234 ")
print(api_deleteuser("chess", "userdel","1234"))



#exemple de login sense exit
print ("\nFem login per la app 'chess', usuari=alex amb pass=mypasswordzz ")
print(api_login("chess","alex","mypasswordzz"))


#exemple de consulta d'usuaris
print ("\nLlistem usuaris per chess:")
print(api_userlist("chess"))


#exemple de login sense exit
print ("\nFem updatepunts per la app 'chess', usuari=alex amb pass=mypasswordzz ")
print(api_updatepunts("chess","alex","mypasswordzz",43))



#exemple de login sense exit
print ("\nFem getpunts per la app 'chess', usuari=alex amb pass=mypasswordzz ")
print(api_getpunts("chess","alex","mypasswordzz"))
'''

# exemple bucle login
while True:
    nom_aplicacio  =input("App: ")
    username = input("Nom: ")
    passw = input ("Contrasenya: ")
    
    
    if api_login(nom_aplicacio, username, passw):
        punts = api_getpunts(nom_aplicacio, username, passw)
        print ("HAS ENTRAT!", username, "Tens ",punts," punts")
        print(api_updatepunts(nom_aplicacio, username, passw,int(input("Update punts: "))))

        break
    else:
        print ("El login ha fallat, Torna-ho a intentar... ")
        
        
