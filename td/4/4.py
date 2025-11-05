def ajouter_fin(fichier1, fichier2):
    try:
        with open(fichier2, 'r', encoding='utf-8') as f2:
            contenu_f2 = f2.read()
        
        with open(fichier1, 'a', encoding='utf-8') as f1:
            f1.write('\n' + contenu_f2)
    except FileNotFoundError as e:
        print(f"erreur not found : {e}")
    except Exception as e:
        print(f"erreur : {e}")