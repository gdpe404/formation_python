# Exercice: Faire un programme qui permet d'ajouter ou retirer des produits d'une liste de courses
#      Lorsque le programme demarre, l'utilisateur a le choix entre:
#           1- Afficher la liste de courses.
#           2- Ajouter un produit a la liste de courses (chaine de caracteres ex: pomme)
#           3- Retirer un produit de la liste de course 
#           4- Supprimer toute la liste de courses
#           5- Quitter le programme
#  
# tant que l'utilisateur ne saisit pas 5, on continue la boucle
# Si l'utilisateur tape 1 : on affiche la liste des produits 
# Si l'utilisateur tape 2 : on lui demande le nom du produit à ajouter et on l'ajoute à la liste de courses
# Si l'utilisateur tape 3 : on lui demande le nom du produit à retirer et on le retire de la liste de courses
# Si l'utilisateur tape 4 : on vide la liste
# Si l'utilisateur tape 5: on affiche "Au revoir" et on quitte le programme

print('Voici le menu:')
print('\t1- Afficher la liste de courses.')
print('\t2- Ajouter un produit à la liste de courses')
print('\t3- Retirer un produit de la liste de course ')
print('\t4- Supprimer toute la liste de courses')
print('\t5- Quitter le programme')

continuer = True
courses = []
# while continuer == True:
while continuer:
    choix = input("Que voulez-vous faire ?")
    if choix == '1':
        # 0, 0.0, '', False, [] -> False
        # taille_courses = len(courses)
        # if not taille_courses:
        if not courses:
            print('La liste est vide')
        else:
            for produit in courses:
                print(f'- {produit}')
    elif choix == '2':
        nom_produit = input('Quel produit voulez-vous ajouter ? ')
        # courses.append('pomme')
        courses.append(nom_produit)
        print(f"{nom_produit} a bien été ajouté à la liste.")
    elif choix == '3':
        nom_produit = input('Quel produit voulez-vous retirer ? ')
        if nom_produit in courses:
            courses.remove(nom_produit)
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