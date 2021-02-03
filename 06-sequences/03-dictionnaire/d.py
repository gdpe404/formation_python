# une association clef / valeur
# La clef d'un dictionnaire est unique

dictionnaire = { 
    'Ornithorynque': 'Animal semi-aquatique tres etrange',
    'herbe': 'pelouse verte',
    'Avion': 'Oiseau de metal'
}

print( dictionnaire['Ornithorynque'] )
print( dictionnaire['Avion'] )
print(dictionnaire)

# dictionnaire['avion'] <- erreur, la clef avion n'existe pas.
# Avec la fonction .get() si la clef n'existe pas, on aura comme valeur: None
definition = dictionnaire.get('avion') 
print(definition)

dictionnaire['herbe'] = 'Super !' # Si la clef existe, la valeur est modifiée
print(dictionnaire)

dictionnaire['HERBE'] = 'pelouse verte' # Si la clef n'existe pas, elle est créée
print(dictionnaire)

utilisateur = {
    'nom': 'Doe',
    'prenom': 'John',
    'age': 15,
    'email': 'j.doe@exemple.fr'
}

print( utilisateur.get('nom') )
print( utilisateur.get('prenom') )

print("___ Parcourir un dictionnaire ___ ")

for clef in utilisateur:
    print(f"clef: {clef}")
    print(f"valeur: {utilisateur.get(clef)}")



# print( utilisateur.items() )
# for item in utilisateur.items():
for clef, valeur in utilisateur.items():
    # print(item)
    # clef = item[0]
    # valeur = item[1]
    # clef, valeur = item # clef, valeur = ('nom', 'John')
    print(f"{clef}: {valeur}")


for valeur in utilisateur.values():
    print(f"valeur: {valeur}")


# for clef in utilisateur.keys():
#     print(f"clef: {clef}")


resultat = 'John' in utilisateur.values()
print(resultat)


# utilisateur_list = [
#     {},
#     {}
# ]

# utilisateur_list = [
#     {'nom': 'Doe','prenom': 'John','age': 15,'email': 'j.doe@exemple.fr'}, 
#     {'nom': 'x','prenom': 'x','age': 15,'email': 'j.doe@exemple.fr'},
#     {'nom': 'y','prenom': 'y','age': 15,'email': 'j.doe@exemple.fr'} 
# ]

utilisateur = {
    'nom': 'Doe',
    'prenom': 'John',
    'age': 15,
    'email': 'j.doe@exemple.fr'
}

utilisateur2 = {
    'nom': 'Zarella',
    'prenom': 'Maude',
    'age': 32,
    'email': 'm.zarella@exemple.fr'
}

utilisateurs = [utilisateur, utilisateur2]
print(utilisateurs)

print( utilisateurs[0] )
# dictionnaire = utilisateurs[0]
# print(dictionnaire.get('nom'))
print( utilisateurs[0].get('nom') )