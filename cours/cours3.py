import pickle
import json

# Exercice 1
try: 
    with open('bonjour.txt', 'r') as f:
        c = f.read()
        print(c)
except FileNotFoundError:
    print('Bjr.txt existe pas')

# Exercice 2
with open('nombre.txt', 'r', encoding='utf-8') as f:
    for ligne in f:
        print(f'ligne: {ligne}')

# Exercice 3
etudiant = {'nom': 'Audibert', 'age': 20, 'notes': [13, 15, 18], 'admis': True}

with open('etudiant.pkl', 'wb') as f:
    pickle.dump(etudiant, f)

with open('etudiant.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)

# Exercice 4
try:    
    with open('utilisateur.json', 'w') as f:
        data = {'name': input("Nom: "), 'age': input("age: ")}
        json.dump(data, f)

    with open('utilisateur.json', 'r') as f:
        data = json.load(f)
        print(f"Bonjour {data["name"]}, vous avez {data["age"]} ans.")
except FileNotFoundError:
    print("file not found")
except json.JSONDecodeError:
    print("json decoder")

