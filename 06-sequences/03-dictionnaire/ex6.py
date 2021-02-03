###########################################################################################################
# Transformer la liste de courses:
#   La liste de courses reste une liste mais on y mettra des dictionnaires dedans.
#       un dictionnaire contient: un nom de produit (str) et une quantité (int)
#
#   - soit on part sur une liste avec des dictionnaires 
#   - transformer la liste en dictionnaire 
###########################################################################################################

print('Voici le menu:')
print('\t1- Afficher la liste de courses.')
print('\t2- Ajouter un produit à la liste de courses')
print('\t3- Retirer un produit de la liste de course ')
print('\t4- Supprimer toute la liste de courses')
print('\t5- Quitter le programme')

continuer = True
courses = []
# courses = {
#     'pomme': 5
# }
# courses[nom_produit] = quantite_produit
# courses.pop(nom_produit)

# while continuer == True:
while continuer:
    choix = input("Que voulez-vous faire ?")
    if choix == '1':
        if not courses:
            print('La liste est vide')
        else:
            i = 1
            for produit in courses:
                print(f"{i}- {produit.get('nom')} x{produit.get('quantite')}")
                i += 1
    elif choix == '2':
        nom_produit = input('Quel produit voulez-vous ajouter ? ')
        quantite_produit = int(input('Combien en voulez-vous ?'))
        produit = {
            'nom': nom_produit,
            'quantite': quantite_produit
        }
        courses.append(produit)
        print(f"{nom_produit} a bien été ajouté à la liste.")
    elif choix == '3':
        nom_produit = input('Quel produit voulez-vous retirer ? ')
        for produit in courses:
            # print(produit)
            if nom_produit in produit.values():
                courses.remove(produit)
                print(f"{nom_produit} a bien été retiré de la liste.")
        else:
            print(f"{nom_produit} n'est pas dans la liste.")
    elif choix == '4':
        # courses = []
        courses.clear()
        print("La liste a bien été vidée.")
    elif choix == '5':
        continuer = False
        print("Au revoir")