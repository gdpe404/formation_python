# TP:
# Demander a l'utilisateur de saisir un mot
# tant que ce mot est different de "quitter" alors on recommence
# on redemande a l'utilisateur de saisir un mot

mot = '' # On creer une chaine de caracteres avec rien dedans
while mot != "quitter":
    mot = input("Tapez 'quitter' pour quitter: ")
    # mot = mot.lower()
    

#TP
# reprendre le convertisseur Heure -> minutes de 02-Operateurs
# Faire une boucle: tant que l'utilisateur ne tape pas 2, on recommence la boucle
# Dans cette boulce on met:
# Afficher un message à l'utilisateur pour savoir s'il souhaite
#      1- Convertir
#      2- Quitter
# Si l'utilisateur saisit 1:
#       * demander à l'utilisateur de saisir des heures
#       * demander à l'utilisateur de saisir des minutes
#       * convertir les heures en minutes
#       * afficher le resultat
# Si l'utilisateur saisit 2:
#         * afficher au revoir

print("Voici le menu: ")
print("\t1- Convertir des heures en minutes") # \t = tabulation   
print("\t2- Quitter")  
choix = ''
while choix != "2":
    choix = input('Que voulez-vous faire ?')
    if choix == "1":   
        heures = input("Saisir des heures : ")
        minutes = input("Saisir des minutes : ")
        heures = int(heures)
        minutes = int(minutes) 
        resultat = heures * 60 + minutes
        print(f"{heures}h{minutes} = {resultat} minutes")
    elif choix == "2":
        print("Au revoir")
    else:
        print("Je n'ai pas compris.")
# print("Au revoir")
