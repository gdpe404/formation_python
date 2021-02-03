# Faire une fonction qui affiche 'Hello World !'
def hello_world():
    print("Hello World !")

hello_world()

# Faire une fonction qui prend un paramètre 'prenom' et affiche Bonjour suivi du prénom
def say_hello(prenom):
    print(f"Bonjour {prenom} !")

# p = input('Quel est votre prenom ? ')
p = 'John'
say_hello(p)

# Faire une fonction qui affiche la multiplication de 2 nombres passés en paramètres
def multiplication(nombre, nombre2):
    resultat = nombre * nombre2
    print(f"{nombre} x {nombre2} = {resultat}")

multiplication(5,2)
multiplication(15,7)

# Faire une fonction qui renvoie la soustraction de 2 nombres passés en paramètre
def soustraction(nombre, nombre2):
    resultat = nombre - nombre2
    return resultat
    # return nombre - nombre2

resultat = soustraction(5,2)
print(f"Resultat: {resultat}")

print(f"Resultat: { soustraction(10,4) }")

# Faire une fonction qui affiche la table de multiplication d'un nombre passé en paramètre
def print_table(nombre, max_=10):
    compteur = 1
    while compteur <= max_:
        resultat = nombre * compteur
        print(f"{nombre} x {compteur} = {resultat}")
        compteur += 1
        
        
print_table(7)
print_table(5, 20)

# Faire une fonction qui convertit des heures en minutes, elle prend 2 arguments: heures et minutes.
# exemple: how_many_minutes(heure, minutes): #...
# exemple d'appel: how_many_minutes(1,30)  <- renvoie 90
def how_many_minutes(heures, minutes):
    return (heures * 60 + minutes)

print( how_many_minutes(1, 30) )
resultat = how_many_minutes(2,45)
print(f"Resultat: {resultat}")

# Faire une fonction qui cherche une lettre dans une chaine de caractères et qui retourne "trouvée" si la lettre a été trouvée
# et 'aucun résultat' dans le cas contraire.
# find_char(chaine, lettre) : #...
# exemple d'appel: find_char("Salut tout le monde", 'u') <- cherche la lettre 'u' dans la chaine
# etape 2: faire la fonction find_char(chaine,letter)
# indice: une chaine de caractère se comporte comme un tableau
# indice: une boucle et un if sont necessaires

def find_char(chaine, lettre):
    index = 0
    taille_chaine = len(chaine)
    while index < taille_chaine:
        # if "u" == "S":
        # if "u" == "a":
        # if "u" == "l":
        if lettre == chaine[index]:
            return "Trouvé"
        index += 1
    return "Aucun résultat"

print( find_char("Salut tout le monde", 'u') )
resultat = find_char("Salut tout le monde", 'z')
print(f"Resultat: {resultat}")

def find_char_avec_for(chaine, lettre_rechercher):
    for lettre_en_cours in chaine:
        # if "u" == "S":
        # if "u" == "a":
        # if "u" == "l":
        if lettre_en_cours == lettre_rechercher:
            return "Trouvé"
    return "Aucun résultat"

print( find_char_avec_for("Salut tout le monde", 'u') )
resultat = find_char_avec_for("Salut tout le monde", 'z')
print(f"Resultat: {resultat}")