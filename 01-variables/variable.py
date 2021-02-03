# Variable: Une zone mémoire dans laquelle on stock des valeurs
# L'age d'un utilisateur, son prenom etc... 

# Str (String): Chaine de caractères (une phrase, un mot ou une lettre)
# Int (Integer): Nombre entier
# Float : Nombre à virgule
# Bool (Boolean): Vrai/Faux -> True/False 

# Typage dynamique.
prenom = "John" # str
age = 19 # int
pi = 3.14 # float
b = False # bool

print('Bonjour ! ')

# print('John')
print(prenom)
print(age)
print(pi)
print(b)

# Concatenation: Ajoute une chaine de caractere a la fin d'une autre chaine

#  print('BonjourTout le monde')
print('Bonjour' + "Tout le monde")

# print('La variable prenom a pour valeur: ' + 'John')
# print('La variable prenom a pour valeur: John')
print('La variable prenom a pour valeur: ' + prenom)

# Python est un langage fortement typé 
# (on ne peut pas faire d'operation entre les types)
# print('La variable age a pour valeur: ' + age ) <- erreur

# print('La variable age a pour valeur: ' + str(19) )
# print('La variable age a pour valeur: ' + "19" )
# print('La variable age a pour valeur: 19' )
print('La variable age a pour valeur: ' + str(age) )

print('La variable pi a pour valeur: ' + str(pi) )
print('La variable b a pour valeur: ' + str(b) )

# On peut changer la valeur et le type de la variable a n'importe quel moment
age = 20
print('La variable age a pour valeur: ' + str(age) )
age = "20"
print('La variable age a pour valeur: ' + age)

# Nommage des variables: 
#   1. Le nom d'une variable ne peut contenir que des chiffres, des lettres
#       et/ou un underscore(_)
#   2. Le nom d'une variable ne doit pas pas commencer par un chiffre
#   3. Le nom est sensible aux majuscules: age, Age, AgE sont 3 variables 
#           differentes

# $var = 5 <- erreur
# 5variables = 4 <- erreur
v1s2d3sd1s2225d5 = 12
# print(Age) <- Age n'existe pas

# Conventions de nommage:
#   1- snake_case + minuscule: _ a la place des espaces. nom_de_ma_variable
#   2- snake_case + Majuscule: NOM_DE_LA_CONSTANTE /!\ il n'y a pas de vrai constante en python
#   3- une variable qui commence par un _ est une variable privée
#   4- Toujours avoir des noms explicites pour nos variables

MAX_ECRAN = 1080
