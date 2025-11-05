import csv

def lire_codes_postaux_uniques(nom_fichier):
    try:
        with open(nom_fichier, mode='r') as fichier:
            lecteur_csv = csv.reader(fichier)
            next(lecteur_csv) 
            codes_postaux = {ligne[1] for ligne in lecteur_csv}
        return sorted(codes_postaux)
    except FileNotFoundError:
        print(f"pas de fichier")
        return []
    except IndexError:
        print("pas au csv")
        return []
    

