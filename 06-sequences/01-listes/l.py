# Les listes regroupent un ensemble de données coherent.

# Si on veut faire une liste de notes
# note = 2
# note2 = 3
# note3 = 9

# List vide
notes = []
print(notes)

notes = [2,5,8,9]
print(notes)

print(f"Première note: { notes[0] }")
print(f"Deuxième note: { notes[1] }")

# notes[4] <- IndexError: list index out of range,
# il y a 4 éléments mais le dernier index est 3 car on commence a 0

taille_notes = len(notes)
print(f"Il y a {taille_notes} éléments dans ma liste")

# print(f"Dernière note: { notes[4 - 1] }")
# print(f"Dernière note: { notes[3] }")
print(f"Dernière note: { notes[taille_notes - 1] }")
# En python on peut avoir des index negatifs
print(f"Dernière note: { notes[-1] }")
print(f"Avant dernière note: { notes[-2] }")
# notes[-10] <- erreur, on depasse dans le negatif

notes[0] = 7
print(notes)

# notes[4] = 5 <- il n'y a pas de valeur a l'index 4

print(" ___ Parcourir une liste _____")

index = 0 # i ou index
taille_notes = len(notes)
while index < taille_notes:
    note = notes[index]
    print(note)
    index += 1
    
print(" ___ Parcourir une liste avec un for _____")
# for ma_variable in sequences: 
for elt in notes:
    print(elt)
    
    
print(" ___ Manipulation d'une liste _____")

prenoms = ['Maude', 'Rick', 'Ella']
print(prenoms)

# Ajoute un élément à la fin de ma liste
prenoms.append('John')
print(prenoms)

# Insert l'élément 'Sarah' à l'index 1 de ma liste
prenoms.insert(1, 'Sarah')
print(prenoms)

# Supprime le dernier élément de ma liste
prenoms.pop()
print(prenoms)

# Supprime l'élément à l'index 2 de ma liste
prenoms.pop(2)
print(prenoms)

# Supprime l'élément 'Maude' et supprime le de ma liste
prenoms.remove('Maude')
print(prenoms)

nombre = prenoms.count('Maude')
print(f"Il y a {nombre} fois le prenom 'Maude' dans la liste")

index = prenoms.index('Ella')
print(f"'Ella' se trouve a l'index {index}")

# remove, pop, index, count ... il faut verifier avant si l'element est dans la liste
# Sinon notre programme va planter

# print( 'Ella' in prenoms )
# if ... in ...
if ('Ella' in prenoms): 
    index = prenoms.index('Ella')
else:
    print("Ella n'est pas dans la liste")


prenoms = ['Maude', 'Rick', 'Ella', 'Sarah']
print(prenoms)

prenoms.reverse()
print(prenoms)

# Trie par odre ascii (Alphabetique)
prenoms.sort()
print(prenoms)

liste_courses = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i <= len(liste_courses):
    liste_courses.pop()
    print(f"i = {i}")
    print(f"len = {len(liste_courses)}")
    i+=1
    
print(liste_courses)


ville = "Berlin,Nairobi,Denver,Moscou,Tokyo,Rio,Helsinki,Olso"
liste_ville = ville.split(',')
print(liste_ville)
print( type(liste_ville) )

prenoms = ['Maude', 'Rick', 'Ella', 'Sarah']
prenom_str = " -> ".join(prenoms)
print(prenom_str)
print( type(prenom_str) )

print(" ___ Les slices ___ ")


prenoms = ['Maude', 'Rick', 'Ella', 'Sarah']
nouvelle_liste = prenoms[0:2] # de l'index 0 jusqu'a 2 non inclus
print(nouvelle_liste)

nouvelle_liste = prenoms[1:3] # de l'index 1 jusqu'a 3 non inclus
print(nouvelle_liste)

nouvelle_liste = prenoms[0:] # de 0 jusqu'a la fin
print(nouvelle_liste)

nouvelle_liste = prenoms[:] # du debut jusqu'a la fin
print(nouvelle_liste)

nouvelle_liste = prenoms[:3] # du debut jusqu'a 3 non inclus
print(nouvelle_liste)

nouvelle_liste = prenoms[0:5:2] # du debut jusqu'a 5 non incls 
#                                   avec un pas (step) de 2
print(nouvelle_liste)

nouvelle_liste = prenoms[::-1]
print(nouvelle_liste)

print(" ___ Comphrension List _____ ")

notes = [7,5,8,9]
# Je veux mettre les notes sur 20
notes_sur_20 = []
for note in notes:
    resultat = note * 2
    notes_sur_20.append(resultat)
    
print(notes_sur_20)
# Pour chaque note, dans ma liste de notes, j'ajoute dans ma nouvelle liste
# note
notes_sur_20 = [note*2 for note in notes]
print(notes_sur_20)

notes_pair = [note for note in notes if note % 2 == 0]
print(notes_pair)

notes = [note if note % 2 == 0 else note * 2 for note in notes]
print(notes)



prenoms = ['Maude', 'Rick', 'Ella', 'Sarah']
prenom1, prenom2, prenom3, prenom4 = prenoms
print(prenom1)
print(prenom2)
print(prenom3)
print(prenom4)