# Un module: c'est un fichier python contient des variables/fonctions/classes
# Un package: C'est un dossier qui contient des modules et/ou des sous packages
#               et un fichier __init__.py ("Configuation" du package)

# 02-perso
# |_app.py
# |_mypackage
#     |_ __init__.py
#     |_mymodule.py
#     |_module2.py
#     |_mypackage2
#          |

import mypackage.mymodule

mypackage.mymodule.hello_world()
mypackage.mymodule.print_table(12)

# help(mypackage.mymodule)

# import mypackage
# mypackage.mymodule.hello_world()
