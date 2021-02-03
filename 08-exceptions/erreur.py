# Par defaut, lorsque python rencontre une erreur, il quitte le programme
# Et il affiche une erreur dans le terminal
# On dit que python leve une exception

# 1 / 0
# print("On continue")

# On peut capturer une erreur en faisant
try:
    # bloc d'instruction
    1 / 0
except:
    print("Erreur, division par 0 impossible")
    
print("On continue")


nombre = input('Saisir un nombre: ')
# if nombre.isnumeric() # '12' -> True, '12ab' ->False

try:
    a = 15
    nombre = int(nombre)
    1 / nombre
    # je ne suis pas assuré d'aller jusqu'ici 
except ZeroDivisionError:
    print("Erreur, division par 0 impossible")
except ValueError:
    print("Erreur, vous devez saisir un nombre")
except Exception as e:
    print(f"Erreur inconnu: {e} ")
else:
    print("Super ! Tout s'est bien passé, donc je passe ici")
finally:
    print("Je passe ici dans tous les cas")

print("On continue")

# Exeception
#  |_ArithmeticError
#  |   |_ ZeroDivisionError
#  |_ValueError