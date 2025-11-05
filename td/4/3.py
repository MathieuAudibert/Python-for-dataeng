def sans_saut(file_in, file_out):
    try:
        with open(file_in, 'r') as fin:
            contenu = fin.read()
        
        contenu_sans_saut = contenu.replace('\n', ' ')
        
        with open(file_out, 'w') as fout:
            fout.write(contenu_sans_saut)

    except FileNotFoundError:
        print(f"Erreur : existe pas '{file_in}'")
    except Exception as e:
        print(f"Erreur : {e}")

print(sans_saut("15.py", "1.py"))
