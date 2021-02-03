# Un module: c'est un fichier python contient des variables/fonctions

# Differentes manieres d'importer un module
import random
from random import randrange
from random import uniform as r_uni
# from random import *

# print( dir() )

r = random.randint(0, 10) # Genere un nombre aléatoire entre 0 et 10
print(r)

r = randrange(10) # Genere un nombre entre 0 et 10 non inclus
print(r)

r = randrange(5,13) # Genere un nombre entre 5 et 13 non inclus
print(r)

r = randrange(0,101,5) # Genere un nombre entre 0 et 101 non inclus
#                               avec un pas (step) de 5
print(r)

r = r_uni(0, 1) # Genere un nombre entre 0 et 1 (Float)
print(r) 


prenoms = ['Ella', 'John', 'Rick', 'Maude']

# r = random.randrange(len(prenoms))
# prenom = prenoms[r]

prenom = random.choice(prenoms)
print(prenom)

alphabet = "abcedefghi"
lettre = random.choice(alphabet)
print(lettre)