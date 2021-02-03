# Une variable stock une valeur
# Une fonction stock un ensemble d'instructions => factoriser du code

# Imaginons le cas d'un eleve qui est souvent puni
# On serait obligé de copier/coller les boucles

def dire_bonjour():
    # Bloc d'instructions.
    print("Bonjour")
    print("Tout")
    print("Le")
    print("Monde")
    prenom = "Maude"
    print("Prenom : "+ prenom)    

dire_bonjour()
#  50 lignes plus tard... 
dire_bonjour()

def faire_punition_simple():
    compteur = 1
    while compteur <= 10:
        # Bloc d'instructions
        print(f"Ligne {compteur}: Je ne dois pas recopier sans comprendre")
        compteur += 1

faire_punition_simple()
faire_punition_simple()



# Imaginons le cas d'un eleve qui est beaucoup trop souvent puni
# Cette fois il doit recopier 100fois

# On definit la valeur du parametre, au moment de l'appel de cette fonction
def faire_punition(combien_de_fois):
    print(f"Combien de fois = {combien_de_fois}")
    compteur = 1
    while compteur <= combien_de_fois:
        # Bloc d'instructions
        print(f"Ligne {compteur}: Je ne dois pas recopier sans comprendre")
        compteur += 1
    

# faire_punition(combien_de_fois = 10)
faire_punition(10) # Argument
# faire_punition(combien_de_fois = 25)
faire_punition(25)
# faire_punition(combien_de_fois = 100)
faire_punition(100)

nombre = 10
# nombre = input('Combien de fois je dois recopier ?')
# nombre = int(nombre)
# faire_punition(combien_de_fois = nombre)
# faire_punition(combien_de_fois = 10)
faire_punition(nombre)

def faire_punition_v2(combien_de_fois, message):
    print(f"Combien de fois = {combien_de_fois}")
    compteur = 1
    while compteur <= combien_de_fois:
        # Bloc d'instructions
        print(f"Ligne {compteur}: {message}")
        compteur += 1
        
# faire_punition(combien_de_fois = 3, message = "Je ne dois pas recopier sans comprendre")
faire_punition_v2(3, "Je ne dois pas recopier sans comprendre")
faire_punition_v2(7, "Je ne dois pas faire ca")
faire_punition_v2(3, "Je ne dois pas faire ci")

print("_____ Fonction qui renvoie une valeur ________")

def carre(nombre): # 5
    # resultat est une variable locale a la fonction
    resultat = nombre * nombre # 5 * 8 = 25
    # print(f"Resultat: {resultat}") # 25
    return resultat # 25
    
carre(5)
# print(resultat) # <- la variable resultat, n'existe pas en dehors de la fonction 

# J'aimerai doubler le resultat. 
# nombre = 25
nombre = carre(5)
print(f"nombre: {nombre}")
# nombre = 49
nombre = carre(7)
print(f"nombre: {nombre}")

nombre = nombre * 2
print(f"nombre: {nombre}")


print("_____ Parametre avec une valeur par defaut ________")

# Les parametres par defaut doivent etre en derniere position
def faire_punition_v3(message, combien_de_fois=10):
    print(f"Combien de fois = {combien_de_fois}")
    compteur = 1
    while compteur <= combien_de_fois:
        # Bloc d'instructions
        print(f"Ligne {compteur}: {message}")
        compteur += 1

faire_punition_v3("Je ne dois pas ....")
faire_punition_v3("Je ne dois pas ....", 3)


def return_multiple(nombre):
    resultat = nombre * nombre
    return resultat, 10

tuples = return_multiple(5)
print(tuples)
print( type(tuples) )

var1, var2 = return_multiple(7)
print(var1)
print( type(var1) )

print(var2)
print( type(var2) )