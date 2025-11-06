import os
import csv
from collections import defaultdict
import json
import shutil
from datetime import datetime

# 1.
def lister_csv(path="ventes"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} existe pas")

    fichiers_csv = [f for f in os.listdir(path) if f.endswith(".csv")]
    for f in fichiers_csv:
        print(f)
    return fichiers_csv

# 2.
def lire_ventes(fichiers_csv, path="ventes"):
    ventes = []
    for fichier in fichiers_csv:
        chemin = os.path.join(path, fichier)
        with open(chemin, "r", encoding="utf-8") as f:
            lecteur = csv.DictReader(f, delimiter=";")
            for ligne in lecteur:
                ligne["source"] = fichier
                ventes.append(ligne)
    for v in ventes:
        print(v)
    return ventes

# 3.
def est_valide(ligne):
    try:
        q = int(ligne["quantite"])
        p = float(ligne["prix_unitaire"])
        return q > 0 and p > 0 and ligne["nom"].strip() != ""
    except Exception:
        return False

def filtrer_ventes(ventes):
    ventes_valides = [v for v in ventes if est_valide(v)]
    ventes_invalides = [v for v in ventes if not est_valide(v)]
    print(f"{len(ventes_valides)} lignes OK, {len(ventes_invalides)} lignes KO.")
    return ventes_valides, ventes_invalides

# 4.
def enregistrer_erreurs(ventes_invalides, ventes):
    if ventes:
        with open("ventes_erreurs.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=ventes[0].keys(), delimiter=";")
            writer.writeheader()
            writer.writerows(ventes_invalides)
        print(f"{len(ventes_invalides)} lignes")
    else:
        print("pas de vente")

# 5.
def calculer_ca_par_fichier(ventes_valides):
    ca_par_fichier = defaultdict(float)
    for v in ventes_valides:
        ca_par_fichier[v["source"]] += int(v["quantite"]) * float(v["prix_unitaire"])
    for f, ca in ca_par_fichier.items():
        print(f"{f} : {ca:.2f} €")
    return ca_par_fichier

# 6.
def produit_le_plus_vendu(ventes_valides):
    quantites = defaultdict(int)
    for v in ventes_valides:
        quantites[v["nom"]] += int(v["quantite"])
    produit_max = max(quantites.items(), key=lambda x: x[1])
    print(f"best produit : {produit_max[0]} ({produit_max[1]} unités)")
    return produit_max

# 7.
def creer_rapport(ca_par_fichier, produit_max):
    rapport = [
        "rapport",
        "",
        "ca /fichier :",
    ]
    for f, ca in ca_par_fichier.items():
        rapport.append(f"{f} : {ca:.2f} €")

    rapport.append("")
    rapport.append(f"produit : {produit_max[0]} ({produit_max[1]} unités)")

    with open("rapport_ventes.txt", "w") as f:
        f.write("\n".join(rapport))

# 8.
def creer_resultats_json(ca_par_fichier, produit_max, ventes_valides, ventes_invalides):
    resultats = {
        "ca": ca_par_fichier,
        "produit": {"nom": produit_max[0], "quantite": produit_max[1]},
        "lignes OK": len(ventes_valides),
        "lignes KO": len(ventes_invalides)
    }

    with open("resultats_global.json", "w", encoding="utf-8") as f:
        json.dump(resultats, f, ensure_ascii=False, indent=2)

# 9.
def creer_resume_par_magasin(ca_par_fichier):
    with open("resume_par_magasin.csv", "w") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["magasin", "CA_total"])
        for f_csv, ca in ca_par_fichier.items():
            ville = f_csv.replace("ventes_", "").replace(".csv", "")
            writer.writerow([ville, round(ca, 2)])

# 10.
def archiver_fichiers(fichiers_csv, path="ventes", path_archive="archives"):
    os.makedirs(path_archive, exist_ok=True)
    date_du_jour = datetime.now().strftime("%Y-%m-%d")
    dossier_archive_date = os.path.join(path_archive, date_du_jour)
    os.makedirs(dossier_archive_date, exist_ok=True)

    for f in fichiers_csv:
        shutil.move(os.path.join(path, f), os.path.join(dossier_archive_date, f))

def main():
    fichiers_csv = lister_csv()
    ventes = lire_ventes(fichiers_csv)
    ventes_valides, ventes_invalides = filtrer_ventes(ventes)
    enregistrer_erreurs(ventes_invalides, ventes)
    ca_par_fichier = calculer_ca_par_fichier(ventes_valides)
    produit_max = produit_le_plus_vendu(ventes_valides)
    creer_rapport(ca_par_fichier, produit_max)
    creer_resultats_json(ca_par_fichier, produit_max, ventes_valides, ventes_invalides)
    creer_resume_par_magasin(ca_par_fichier)
    archiver_fichiers(fichiers_csv)

if __name__ == "__main__":
    main()
