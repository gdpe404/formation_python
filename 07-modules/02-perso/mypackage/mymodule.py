# Docstring
def hello_world():
    """Affiche le message 'Hello world' dans le terminal
    """
    print("Hello World !")

def say_hello(prenom):
    """Affiche le message 'bonjour' suivi du prenom

    Args:
        prenom (str): prenom de l'utilisateur
    """
    print(f"Bonjour {prenom} !")

def multiplication(nombre, nombre2):
    resultat = nombre * nombre2
    print(f"{nombre} x {nombre2} = {resultat}")

def soustraction(nombre, nombre2):
    """Renvoie le resultat d'une soustraction

    Args:
        nombre (int): Nombre 1
        nombre2 (int): Nombre 2

    Returns:
        int: Resultat de la soustraction
    """
    resultat = nombre - nombre2
    return resultat

def print_table(nombre, max_=10):
    """Affiche la table de multiplication d'un nombre

    Args:
        nombre (int): nombre entier
        max_ (int, optional): [description]. Defaults to 10.
    """
    compteur = 1
    while compteur <= max_:
        resultat = nombre * compteur
        print(f"{nombre} x {compteur} = {resultat}")
        compteur += 1
        
def how_many_minutes(heures, minutes):
    return (heures * 60 + minutes)

def find_char(chaine, lettre):
    index = 0
    taille_chaine = len(chaine)
    while index < taille_chaine:
        if lettre == chaine[index]:
            return "Trouvé"
        index += 1
    return "Aucun résultat"

def find_char_avec_for(chaine, lettre_rechercher):
    for lettre_en_cours in chaine:
        if lettre_en_cours == lettre_rechercher:
            return "Trouvé"
    return "Aucun résultat"

print("__name__ : " + __name__ )

if __name__ == "__main__": # <- ca veut dire qu'on execute le fichier en tant que script.
         
    hello_world() 
      
    p = 'John'
    say_hello(p)
    
    multiplication(5,2)
    multiplication(15,7)

    resultat = soustraction(5,2)
    print(f"Resultat: {resultat}")

    print(f"Resultat: { soustraction(10,4) }")

    print_table(7)
    print_table(5, 20)

    print( how_many_minutes(1, 30) )
    resultat = how_many_minutes(2,45)
    print(f"Resultat: {resultat}")

    print( find_char("Salut tout le monde", 'u') )
    resultat = find_char("Salut tout le monde", 'z')
    print(f"Resultat: {resultat}")

    print( find_char_avec_for("Salut tout le monde", 'u') )
    resultat = find_char_avec_for("Salut tout le monde", 'z')
    print(f"Resultat: {resultat}")