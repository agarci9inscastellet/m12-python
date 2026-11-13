from api_login import *

# api_register(app, "pepe","1234")
# api_login(app,"alex","1234")
# api_userlist(app)
# api_deleteuser(app, "pepe","1234")
# api_userlist(app)
# api_getpunts(app,"alex","1234")
# api_updatepunts(app,"alex","1234",43)


# URL examples
# http://www.castellet2526m12.cat/api.php?a=userlist&app=lx
# http://www.castellet2526m12.cat/api.php?a=login&app=lx&name=pepe&pass=pepe_db
# http://www.castellet2526m12.cat/api.php?a=register&app=lx&name=pepe2&pass=pepe2_db
# http://www.castellet2526m12.cat/api.php?a=updatepuntsr&app=lx&name=pepe2&pass=pepe2_db

#exemple de registre d'usuari
#print ("\nRegistrem per la app 'chess', usuari=manu amb pass=1234 ")
#print(api_register(app, "manu2","1234"))
'''
'''
##############################################################################################
app="chess" # és un exemple, aquí ha d'anar la teva app



#exemple de consulta d'usuaris
print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");

print(api_userlist(app))

#exemple de registre d'usuari
print (f"Esborrem per la app {app}, usuari=userdel amb pass=1234 ")
print(api_deleteuser(app, "alex","mypasswordzz"))

print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");

print (f"Registrem per la app {app}, usuari=user2 amb pass=1234 ")
print(api_register(app, "user2","1234"))


print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");

#exemple de login sense exit
print (f"\nFem login per la app {app}, usuari=alex amb pass=1234 ")
print(api_login(app,"alex","1234"))


print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");


#exemple de login sense exit
print (f"\nFem updatepunts per la app {app}, usuari=alex amb pass=mypasswordzz ")
print(api_updatepunts(app,"alex","1234",43))



#exemple de login sense exit
print (f"\nFem getpunts per la app {app}, usuari=alex amb pass=mypasswordzz ")
print(api_getpunts(app,"alex","mypasswordzz"))


print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");

print("Fes un login amb un dels usuaris existents")
# exemple bucle login
while True:
    nom_aplicacio  = app
    username = input("Nom: ")
    passw = input ("Contrasenya: ")
    
    
    if api_login(nom_aplicacio, username, passw):
        punts = api_getpunts(nom_aplicacio, username, passw)
        print ("HAS ENTRAT!", username, "Tens ",punts," punts")
        #print(api_updatepunts(nom_aplicacio, username, passw,int(input("Update punts: "))))

        break
    else:
        print ("El login ha fallat, Torna-ho a intentar... ")