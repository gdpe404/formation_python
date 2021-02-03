# Les tuples fonctionnent comme les listes, mais ne sont pas modifiable

t = (1, 2, 5, 5)
print(f'Premiere valeur { t[0] } ')
print(f'Derniere valeur { t[-1] } ')

# t.append() <- erreur, on ne peut pas modifier un tuple
# t.remove() <- erreur, on ne peut pas modifier un tuple

print(f"Il y a { t.count(5) } fois le chiffre 5 ")
print(f"Le premier 5 se trouve a l'index: { t.index(5) } ")

print(t)

print(" __ Paroucrir un tuple ___ ")

taille_tuple = len(t)
i = 0
while i < taille_tuple:
    print(t[i])
    i += 1
    
print(" __ Parcourir un tuple avec un for ___ ")
for element in t:
    print(element)
    
    
t = (5, 5)
print(t)
print( type(t) )

new_liste = list(t)
print(new_liste)
print( type(new_liste) )


resultat = (5 in t)
print(f"resultat = {resultat}")



# Deballage de tuple ou unpacking
var1, var2 = ('Salut', 'Hola')

print(var1)
print( type(var1) )
print(var2)
print( type(var2) )


mon_tuple = ('Maude', 'Rick', 'Alain')

# prenom = mon_tuple[0]
# prenom2 = mon_tuple[1]
# prenom3 = mon_tuple[2]

prenom, prenom2, prenom3 = mon_tuple
print(prenom)
print(prenom2)
print(prenom3)

t = (5)
print(type(t))

t = 5,
print(type(t))

t = 'Salut', 'Hola'
print(type(t))