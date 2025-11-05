def remplacer_caractere(fichier, ancien, nouveau):
    try:
        with open(fichier, 'r') as f:
            contenu = f.read()
        
        contenu_modifie = contenu.replace(ancien, nouveau)
        
        with open(fichier, 'w') as f:
            f.write(contenu_modifie)
    except FileNotFoundError:
        print(f"existe pas")
    except Exception as e:
        print(f"erreur")