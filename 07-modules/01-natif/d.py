import datetime

ajd = datetime.date.today()
print(f"Aujourd'hui: {ajd}")

# help(datetime) # q pour quitter

anniversaire = datetime.date(2019, 3, 23)
print(f"anniversaire: {anniversaire}")

temps = datetime.datetime(2020, 3, 27, 9, 47, 45)
print(f"temps: {temps}")

maintenant = datetime.datetime.now()
print(maintenant)

difference = maintenant - temps # timedelta
print(difference)

# On peut se servir des timedelta pour faire des operation
# sur les dates
douze_jours = datetime.timedelta(days=12)
print(douze_jours)

print( maintenant + douze_jours )