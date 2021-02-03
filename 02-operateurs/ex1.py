# Déclarer une variable qui s'appelera 'nb' et contiendra le nombre entier 13.
nb = 13

# déclarer une variable 'nb2' qui, contiendra le nombre flottant (a virgule) 15,5
nb2 = 15.5

# déclarer une variable 'b', qui prendra la valeur : true
b = True

# déclarer une variable 'language' qui aura pour valeur la chaîne de caractères 'python'.
language = "Python"

# déclarer une variable 'z' qui aura la même valeur que nb, sans faire z = 13
z = nb

# le message 'hello world' si nb est supérieur ou égal à 4
if nb > 4:
    print("Hello World !")

# TP: Mini calculatrice
# demander à l'utilisateur de saisir un 1er nombre
# demander à l'utilisateur de saisir un 2ème nombre
# additionner les nombres et afficher le résultat
nombre = input("Saisir un nombre: ")
nombre2 = int(input("Saisir un deuxième nombre: "))

nombre = int(nombre) # int
resultat = nombre + nombre2
# print(resultat)
print(str(nombre) + " + " + str(nombre2) + " = " + str(resultat))

# TP: Convertir des pouces en centimetres
# demander à l'utilisateur de saisir des pouces
# 1" (1 pouce) = 2,54 centimètres
# https://www.pouce-cm.fr/
pouces = input("Saisir un nombre de pouce : ")
pouces = float(pouces) # float

resultat = pouces * 2.54
# print(resultat)
#  "10 pouces = 25.4 centimetres"
print(str(pouces) + "pouces = " + str(resultat) + " en centimetres.")


# TP: Convertir des heures en minutes
# demander à l'utilisateur de saisir des heures
# demander à l'utilisateur de saisir des minutes
# convertir les heures & minutes en minutes
heures = input("Saisir des heures : ")
minutes = input("Saisir des minutes : ")
heures = int(heures) # int
minutes = int(minutes) # int

resultat = heures * 60 + minutes
# "1h30 = 90 minutes"
print(str(heures) + "h" + str(minutes) + " = " + str(resultat) + "minutes")
print(f"{heures}h{minutes} = {resultat} minutes")


# TP: Convertir des degres Celcius en degrès Fahrenheit
# https://www.metric-conversions.org/fr/temperature/fahrenheit-en-celsius.htm
# demander à l'utilisateur de saisir des degres celcius
# convertir les °C en °F
celcius = input("Saisir des °C: ")
celcius = float(celcius) # float

fahrenheit = celcius * 1.8 + 32
# print(resultat)
print(str(celcius) + "°C = " + str(fahrenheit) + "°F")

# TP
# Afficher un message à l'utilisateur pour savoir s'il souhaite
#     1- Convertir des pouces en centimètres
#     2- Convertir des centimètres en pouces
#     3- Quitter
# Si l'utilisateur saisit 1:
#      * Demander a l'utilisateur de saisir un nombre: "Nombre de pouces: "
#      * on convertit
#      * on affiche le resultat
# Si l'utilisateur saisit 2:
#      * Demander a l'utilisateur de saisir un nombre: "Nombre de centimètre: "
#      * on convertit
#      * on affiche le resultat
# Sinon on affiche:
#      *Je n'ai pas compris
print("Voici le menu: ")
print("\t1- Convertir des pouces en centimètres") # \t = tabulation   
print("\t2- Convertir des centimètres en pouces")
print("\t3- Quitter")    

choix = input("Que voulez-vous faire ? ")
if choix == "1":
    pouces = input("Saisir un nombre de pouces : ")
    pouces = float(pouces)
    resultat = pouces * 2.54
    print(str(pouces) + "pouces = " + str(resultat) + " en centimetres.")
elif choix == "2":
    cm = input("Saisir un nombre de centimetres : ")
    cm = float(cm)
    resultat = cm / 2.54
    print(str(cm) + "cm = " + str(resultat) + " pouces.")
elif choix == "3":
    print("Au revoir")
    

# Sans executer, le programme essayez d'imaginer si on passe dans le if ou dans le else
a = 15
b = 20
c = True

print("1- Est-ce qu'on affichera oui ou non ?")
if(a > 15 and b == 20):
    print("oui")
else:
    print("non") # non

print("2- Est-ce qu'on affichera oui ou non ?")
if (a != 15 or b == 20):
    print("oui") # oui
else:
    print("non")

print("3- est-ce qu'on affichera oui ou non ?")
if (not c and a == 15):
    print("oui")
else:
    print("non") # non


# switch <- n'existe pas en python