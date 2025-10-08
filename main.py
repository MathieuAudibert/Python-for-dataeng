"""
fruits = ['pomme', 'banane', 'cerise', 'datte']
print(fruits[0])
print(fruits[-1])
fruits.append('orange')
fruits.insert(1, 'kiwi')
fruits.remove('banane')
print(fruits)
"""

"""
personnes = {'nom': "Dupont", 'prenom': "Jean", 'age': 30, 'ville': "Paris"}
print(personnes['nom'])
personnes['age'] = 31
personnes['profession'] = "Ingenieur"
del personnes['ville']
print(personnes)
"""

def password():
    tentatives = 0
    while tentatives < 3:
        mdp = input("Entrez votre mdp:")
        if mdp == "secret":
            print("bon mdp")
            tentatives = 3
        else:
            tentatives += 1
            print("Access denied")
#password()

def is_pangramme():
    phrase = input("Phrase:")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in alphabet:
        if c not in phrase.lower():
            print("Pas un pangramme")
            return False
    print("C'est un pangramme")
#is_pangramme()

is_palindrome = lambda word : word == word[::-1]
print(is_palindrome("radar"))
print(is_palindrome("python"))