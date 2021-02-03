# Les boucles permettent de repeter un traitement, un ensemble d'instructions

# Imaginons le cas d'un eleve qui quoi recopier 10 fois "je ne dois pas ..."
# On serait obligé de copier/coller sans les boucles

# print("Je ne dois pas ... ")
# print("Je ne dois pas ... ")

# on initialise un compteur à 0
# Tant que ce compteur est inferieur a 10, on affiche le message 
# "Je ne dois pas recopier sans comprendre"
# D'augmenter le compteur
compteur = 1
while compteur <= 10:
    # Bloc d'instructions
    print(f"Ligne {compteur}: Je ne dois pas recopier sans comprendre")
    compteur = compteur + 1 #CTRL + C en cas de boucle infinie

print("On continue")

# pas de do ... while en python
# pas de for classique en python (i =0; i < 10; i++)

# Chaine de caractères
prenom = "John"

# Commence toujours a 0
print( prenom[0] ) # J
print( prenom[1] ) # o
lettre = prenom[2] # h
print("Lettre : " + lettre)

# print(prenom[4]) <- erreur, la position 4 n'existe pas

print(" ___ Parcourir une cgaine de caractères avec while ____")

compteur = 0
while compteur < 4:
    # lettre = prenom[0] => J
    # lettre = prenom[1] => o
    lettre = prenom[compteur]
    print("Lettre : " + lettre)
    # compteur = compteur + 1
    compteur += 1


prenom = input('Quel est votre prenom ? ')
compteur = 0
taille_prenom = len(prenom) # length: Calcul la longeur de la chaine de caracteres
print(f"Longueur de prenom: {taille_prenom}")
# while 0 < 15
# while 0 < 5
while compteur < taille_prenom:
    lettre = prenom[compteur]
    print("Lettre : " + lettre)
    compteur += 1
    
print(" ___ For ... in ____ ")
# For ... in :
# for index,lettre in enumerate(prenom):
for lettre in prenom:
    # lettre = prenom[compteur]
    print("Lettre : " + lettre)