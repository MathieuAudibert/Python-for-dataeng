import os
import csv
import json
import shutil
import datetime
from collections import defaultdict

# 1.

def lister_fichiers_csv(path="ventes"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} existe pas")
    
    fichiers = []
    for f in os.listdir(path):
        if f.endswith(".csv") and f.startswith("ventes_"):
            fichiers.append(f)
            print(f)
    return fichiers

# 2. 

def charger_et_fusionner(path="ventes"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} existe pas")
    
    ventes_valides = []
    erreurs = []
    
    fichiers = os.listdir(path)
    for f in fichiers:
        if f.endswith(".csv") and f.startswith("ventes_"):
            filepath = path + "/" + f
            
            with open(filepath, "r", encoding="utf-8") as file:
                lecteur = csv.reader(file, delimiter=";")
                i = 0
                for ligne in lecteur:
                    i += 1
                    
                    if len(ligne) != 4:
                        erreurs.append({
                            'fichier': f,
                            'ligne': i,
                            'donnees': ligne,
                            'erreur': 'nombre de colonnes incorrect'
                        })
                        continue
                    
                    # 3. 
                    id_produit = ligne[0].strip()
                    nom = ligne[1].strip()
                    quantite = ligne[2].strip()
                    prix = ligne[3].strip()
                    
                    erreur_ligne = []
                    
                    if nom == "":
                        erreur_ligne.append("nom vide")
                    
                    try:
                        quantite_num = float(quantite)
                        if quantite_num < 0:
                            erreur_ligne.append("quant negative")
                    except:
                        erreur_ligne.append("quant pas numerique")
                        quantite_num = None
                    
                    try:
                        prix_num = float(prix)
                        if prix_num < 0:
                            erreur_ligne.append("prix négatif")
                    except:
                        erreur_ligne.append("prix non num")
                        prix_num = None
                    
                    if len(erreur_ligne) > 0:
                        erreurs.append({
                            'fichier': f,
                            'ligne': i,
                            'donnees': ligne,
                            'erreur': ', '.join(erreur_ligne)
                        })
                    else:
                        ville = f.replace("ventes_", "").replace(".csv", "").capitalize()
                        ventes_valides.append({
                            'id_produit': id_produit,
                            'nom': nom,
                            'quantite': quantite_num,
                            'prix': prix_num,
                            'ville': ville,
                            'fichier': f
                        })
    
    print(f"{len(ventes_valides)} ventes")
    print(f" {len(erreurs)} erreurs")
    
    return ventes_valides, erreurs

# 4.

def ecrire_erreurs(erreurs):
    if len(erreurs) == 0:
        print("pas d erreur")
        return
    
    with open("ventes_erreurs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(['fichier', 'lines', 'data', 'error'])
        
        for err in erreurs:
            writer.writerow([
                err['fichier'],
                err['ligne'],
                '|'.join(err['donnees']),
                err['erreur']
            ])
    
    print(f"ventes_erreurs.csv ({len(erreurs)})")

# 5.

def calculer_ca_par_fichier(ventes):
    ca_par_ville = {}
    
    for vente in ventes:
        ville = vente['ville']
        ca = vente['quantite'] * vente['prix']
        
        if ville not in ca_par_ville:
            ca_par_ville[ville] = {'ca': 0, 'nb_ventes': 0}
        
        ca_par_ville[ville]['ca'] += ca
        ca_par_ville[ville]['nb_ventes'] += 1
    
    print("\n ca/magasin :")
    for ville in sorted(ca_par_ville.keys()):
        print(f"   {ville:15} : {ca_par_ville[ville]['ca']:12.2f} € ({ca_par_ville[ville]['nb_ventes']} ventes)")
    
    return ca_par_ville

# 6.

def identifier_produit_top(ventes):
    produits = {}
    
    for vente in ventes:
        id_prod = vente['id_produit']
        
        if id_prod not in produits:
            produits[id_prod] = {
                'nom': vente['nom'],
                'quantite': 0,
                'ca': 0
            }
        
        produits[id_prod]['quantite'] += vente['quantite']
        produits[id_prod]['ca'] += vente['quantite'] * vente['prix']
    
    if len(produits) == 0:
        return None
    
    produit_max = None
    quantite_max = 0
    
    for id_prod in produits:
        if produits[id_prod]['quantite'] > quantite_max:
            quantite_max = produits[id_prod]['quantite']
            produit_max = {
                'id': id_prod,
                'nom': produits[id_prod]['nom'],
                'quantite': produits[id_prod]['quantite'],
                'ca': produits[id_prod]['ca']
            }
    
    print(f"\n produit le + vendu :")
    print(f"   ID: {produit_max['id']}")
    print(f"   nom: {produit_max['nom']}")
    print(f"   quant: {produit_max['quantite']:.0f}")
    print(f"   ca: {produit_max['ca']:.2f} €")
    
    return produit_max

# 7. 

def generer_rapport_texte(ca_par_ville, erreurs, produit_top):
    with open("rapport_ventes.txt", "w", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write("RAPPORT D'ANALYSE DES VENTES\n")
        file.write("=" * 60 + "\n")
        file.write(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        
        file.write("global \n")
        file.write("-" * 60 + "\n")
        
        ca_total = 0
        nb_ventes_total = 0
        for ville in ca_par_ville:
            ca_total += ca_par_ville[ville]['ca']
            nb_ventes_total += ca_par_ville[ville]['nb_ventes']
        
        file.write(f"CA: {ca_total:.2f} €\n")
        file.write(f"ventes: {nb_ventes_total}\n")
        file.write(f"erreurs: {len(erreurs)}\n")
        file.write(f"magasins: {len(ca_par_ville)}\n\n")
        
        file.write("par magasin\n")
        file.write("-" * 60 + "\n")
        
        for ville in sorted(ca_par_ville.keys()):
            file.write(f"\n{ville.upper()}\n")
            file.write(f"  CA: {ca_par_ville[ville]['ca']:.2f} €\n")
            file.write(f"  ventes: {ca_par_ville[ville]['nb_ventes']}\n")
        
        if produit_top is not None:
            file.write("\n" + "-" * 60 + "\n")
            file.write("produit vendu le +\n")
            file.write("-" * 60 + "\n")
            file.write(f"ID: {produit_top['id']}\n")
            file.write(f"nom: {produit_top['nom']}\n")
            file.write(f"quant: {produit_top['quantite']:.0f}\n")
            file.write(f"ca: {produit_top['ca']:.2f} €\n")
        
        file.write("\n" + "=" * 60 + "\n")
    

# 8. 

def exporter_json(ca_par_ville, erreurs, produit_top, ventes):
    produits = {}
    
    for vente in ventes:
        id_prod = vente['id_produit']
        if id_prod not in produits:
            produits[id_prod] = {
                'nom': vente['nom'],
                'quantite': 0,
                'ca': 0
            }
        produits[id_prod]['quantite'] += vente['quantite']
        produits[id_prod]['ca'] += vente['quantite'] * vente['prix']
    
    top_5 = []
    produits_list = []
    for id_prod in produits:
        produits_list.append({
            'id': id_prod,
            'nom': produits[id_prod]['nom'],
            'quantite': produits[id_prod]['quantite'],
            'ca': produits[id_prod]['ca']
        })
    
    produits_list.sort(key=lambda x: x['quantite'], reverse=True)
    top_5 = produits_list[:5]
    
    ca_total = 0
    nb_ventes_total = 0
    for ville in ca_par_ville:
        ca_total += ca_par_ville[ville]['ca']
        nb_ventes_total += ca_par_ville[ville]['nb_ventes']
    
    resultats = {
        'date_generation': datetime.datetime.now().isoformat(),
        'resume_global': {
            'ca_total': ca_total,
            'nb_ventes_total': nb_ventes_total,
            'nb_erreurs': len(erreurs),
            'nb_magasins': len(ca_par_ville)
        },
        'par_magasin': ca_par_ville,
        'produit_top': produit_top,
        'top_5_produits': top_5
    }
    
    with open("resultats_global.json", "w", encoding="utf-8") as file:
        json.dump(resultats, file, indent=2, ensure_ascii=False)

# 9. 

def sauvegarder_resume_csv(ca_par_ville):
    with open("resume_par_magasin.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(['ville', 'ca', 'vente', 'panier moyen)'])
        
        for ville in sorted(ca_par_ville.keys()):
            ca = ca_par_ville[ville]['ca']
            nb = ca_par_ville[ville]['nb_ventes']
            panier_moyen = ca / nb if nb > 0 else 0
            
            writer.writerow([
                ville,
                f"{ca:.2f}",
                nb,
                f"{panier_moyen:.2f}"
            ])

# 10.

def archiver_fichiers(path="ventes"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} existe pas")
    
    path_archives = "archives"
    if not os.path.exists(path_archives):
        os.makedirs(path_archives)
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    path_archive_date = path_archives + "/" + timestamp
    os.makedirs(path_archive_date)
    
    print(f"\n{path_archive_date}/")
    
    fichiers = os.listdir(path)
    nb_archives = 0
    
    for f in fichiers:
        if f.endswith(".csv") and f.startswith("ventes_"):
            source = path + "/" + f
            destination = path_archive_date + "/" + f
            shutil.move(source, destination)
            print(f"   ✓ {f}")
            nb_archives += 1
    
    print(f"{nb_archives} archive")

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            with open("erreurs_execution.log", "a", encoding="utf-8") as file:
                file.write(f"{datetime.datetime.now()} - FileNotFoundError: {str(e)}\n")
        except PermissionError as e:
            with open("erreurs_execution.log", "a", encoding="utf-8") as file:
                file.write(f"{datetime.datetime.now()} - PermissionError: {str(e)}\n")
        except Exception as e:
            with open("erreurs_execution.log", "a", encoding="utf-8") as file:
                file.write(f"{datetime.datetime.now()} - Exception: {str(e)}\n")
    return wrapper

@handle_exceptions
def main():
    print("=" * 60)
    
    path = "ventes"
    
    # 1.
    fichiers = lister_fichiers_csv(path)
    if len(fichiers) == 0:
        return
    
    # 2 & 3. 
    ventes, erreurs = charger_et_fusionner(path)
    
    # 4. 
    ecrire_erreurs(erreurs)
    
    # 5. 
    ca_par_ville = calculer_ca_par_fichier(ventes)
    
    # 6.
    produit_top = identifier_produit_top(ventes)
    
    # 7. 
    generer_rapport_texte(ca_par_ville, erreurs, produit_top)
    
    # 8.
    exporter_json(ca_par_ville, erreurs, produit_top, ventes)
    
    # 9.
    sauvegarder_resume_csv(ca_par_ville)
    
    # 10.
    archiver_fichiers(path)
    
    print("\n" + "=" * 60)
    print("=" * 60)

if __name__ == "__main__":
    main()