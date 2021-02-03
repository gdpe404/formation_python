age = 15
prenom = "Maude"

print("Age = " + str(age))

print("Age = %d" % age) # Avant python 3

# print("Age = " + str(age) + ", prenom = " + prenom)
print("Age = {}, prenom = {}".format(age, prenom)) # A partir de python 3

#fstring (format string)
print(f"age = {age}, prenom = {prenom}") # A partir de python 3.6

code_postal = 75015
rue = f"1 rue bidon"

# "1 rue bidon,75015"

adresse = rue + "," + str(code_postal)
print(adresse)

adresse = f"{rue},{code_postal}"
print(adresse)

