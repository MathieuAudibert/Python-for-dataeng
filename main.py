"""
fruits = ['pomme', 'banane', 'cerise', 'datte']
print(fruits[0])
print(fruits[-1])
fruits.append('orange')
fruits.insert(1, 'kiwi')
fruits.remove('banane')
print(fruits)
"""

personnes = {'nom': "Dupont", 'prenom': "Jean", 'age': 30, 'ville': "Paris"}
print(personnes['nom'])
personnes['age'] = 31
personnes['profession'] = "Ingenieur"
del personnes['ville']
print(personnes)