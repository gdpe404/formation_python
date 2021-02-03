a = "2" # str
b = "3" # str

# str + str = concatenation
# str + number = erreur
# number + number = addition 
c = a + b
print(c)
print( type(c) )

print(" => Operateur Arithmetique")

print('____ Addition ____')
# nombre = int("2")
# nombre = 2
nombre = int(a) # convertion d'une chaine de caracteres en nombre entier
nombre2 = int(b)

# resultat = 2 + 3
# resultat = 5
resultat = nombre + nombre2
print("Le resultat = " + str(resultat))

# resultat2 = resultat + 2

# resultat = 5 + 2
# resultat = 7
resultat = resultat + 2
print("Le resultat = " + str(resultat))

# resultat = resultat + 2
# resultat = 7 + 2
# resultat = 9
resultat += 2
print("Le resultat = " + str(resultat))

# resultat++ <- n'existe pas en python

print('____ Soustraction ____')
nombre = 2
nombre2 = 3

resultat = nombre - nombre2
print("Le resultat = " + str(resultat))

resultat = resultat - 2
print("Le resultat = " + str(resultat))

resultat -= 2
print("Le resultat = " + str(resultat))

# resultat-- <- n'existe pas en python

print('____ Multiplication ____')
nombre = 2
nombre2 = 3

resultat = nombre * nombre2
print("Le resultat = " + str(resultat))

resultat = resultat * 2
print("Le resultat = " + str(resultat))

resultat *= 2
print("Le resultat = " + str(resultat))


print('____ Division ____')

nombre = 2
nombre2 = 3

resultat = nombre / nombre2 # Float, même si la division
print("Le resultat = " + str(resultat))

resultat = resultat / 2
print("Le resultat = " + str(resultat))

resultat /= 2
print("Le resultat = " + str(resultat))

print('____ Division Entiere ____')

nombre = 11
nombre2 = 5

# 11 // 5 = 2 et il reste 1
resultat = nombre // nombre2 # int 
print("Le resultat = " + str(resultat))

resultat = resultat // 2
print("Le resultat = " + str(resultat))

resultat //= 2
print("Le resultat = " + str(resultat))

print('____ Modulo ____')

nombre = 11
nombre2 = 5

# 11 % 5 = 2 et il reste 1 <- modulo 
# 11 % 2 = 5 et il reste 1 
# 12 % 2 = 6 et il reste 0
# 13 % 2 = 6 et il reste 1
resultat = nombre % nombre2 # int 
print("Le resultat = " + str(resultat))

resultat = resultat % 2
print("Le resultat = " + str(resultat))

resultat %= 2
print("Le resultat = " + str(resultat))


print('____ Puissance ____')

nombre = 5
nombre2 = 2

resultat = nombre ** nombre2 # 5²
print("Le resultat = " + str(resultat))

resultat = resultat ** 3
print("Le resultat = " + str(resultat))

resultat **= 2
print("Le resultat = " + str(resultat))


print(" => Operateur Comparaisons")

nombre = 5
nombre2 = 7
# Une comparaison renvoie Vrai ou Faux (True/False)

# Est-ce que nombre2 est strictement superieur à nombre
resultat = (nombre2 > nombre)
print("Le resultat = " + str(resultat))

# Est-ce que nombre2 est superieur ou égal à nombre
resultat = (nombre2 >= nombre)
print("Le resultat = " + str(resultat))

resultat = (nombre2 < nombre)
print("Le resultat = " + str(resultat))

resultat = (nombre2 <= nombre)
print("Le resultat = " + str(resultat))

# Est-ce que nombre2 est égal à nombre
resultat = (nombre2 == nombre)
print("Le resultat = " + str(resultat))

# Est-ce que nombre2 est différent de nombre
resultat = (nombre2 != nombre)
print("Le resultat = " + str(resultat))

print("___ Structure conditionnelle ___")

# Si l'age est strictement inferieur a 18, alors on affiche le message:
#           "Vous ne pouvez pas louer de voiture"

# pour rentrer dans la condition, il faut que le test soit vrai
# if (comparaison est vrai): 
#     bloc d'instructions

age = 22
if age < 18: # True -> donc on rentre dans la condition
    print("Vous ne pouvez pas louer de voiture")

# on continue

# Si l'age est strictement inferieur a 18, alors on affiche le message:
#           "Vous ne pouvez pas louer de voiture"
# Sinon (Dans tous les autres cas)on affiche le message
#           "Quel modèle voulez-vous ?"
if age < 18:
    print("Vous ne pouvez pas louer de voiture")
else:
    print("Quel modèle voulez-vous ?")
    
    

if age < 18:
    print("Reduction - 18 ans")
elif age <= 25:
    print("Reduction jeune")
else:
    print("Pas de réduction")
    
print("On continue")

# elif(age < 18): <- erreur, on ne peut pas avoir de elif ou de else tout seul
#     print("Salut")
# else:
#     print("Salut")


age = 12

if age < 18:
    print("Reduction - 18 ans")
elif age <= 25:
    print("Reduction jeune")

print("Les if sont independants")
if age < 18:
    print("Reduction - 18 ans")
if age <= 25:
    print("Reduction jeune")
    


print(" => Operateur Logique")

age = 28
# [18:25]
if (age >= 18 and age <= 25): # True and False -> False
    print("Vous avez entre 18ans et 25ans")

# and (ET): Il faut que les deux tests soient vrais (True and True)
# pour eviter ça
# if age >= 18:
#     if age <= 25:
#         print("Vous avez entre 18ans et 25ans")

# or (OU):Il faut qu'au moins 1 des deux test soit vrai
age = 17
derogation = True
if (age >= 18 or derogation == True): # False or True -> True
    print("Vous avez au moins 18ans ou une dérogation")
    
# pour eviter ça  
# if age >= 18:
#     print("..")
# elif derogation == True:
#     print("..")


# not : inverse le resultat d'un boolean
error = True
print("Error = " + str(error))
print("Error = " + str(not error))

# if error == True:
if error: 
    print("Il y a une erreur ... ")

# Executer ce code s'il n'y a pas d'erreur
# if error == False:
if not error:
    resultat = 5 + 2
    


bouton = False # off par défaut
if bouton == False:
    bouton = True # on
elif bouton == True:
    bouton = False # off

bouton = not bouton

##########################################
# Tester si un nombre est pair ou impair #
##########################################

# demande a l'utilisateur de saisir quelque chose
nombre = input("Saisir un nombre: ") 
# Tout ce que l'utilisateur saisit, est une chaine de caracteres
print("L'utilisateur a saisi : " + nombre)
# nombre = int("15")
# nombre = 15
nombre = int(nombre)

resultat = nombre % 2 # soit 0 soit 1
# 15 % 2 = 7 et il reste 1
# 10 % 2 = 4 et il reste 2 <- impossible car on peut faire 10 / 2 = 5 et il reste 0
if (resultat == 0):
    # "17 est pair"
    print(str(nombre) + " est pair")
else:
    print(str(nombre) + " est impair")
    
