def afficher_fichier(nom): 
    try:
        with open(nom, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(lines)
    except Exception as e:
        print(e)