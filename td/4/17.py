import os
import csv
from collections import defaultdict
import json

# 1.
def lister_fichiers_notes(path="notes"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} existe pas")
    fichiers_notes = [f for f in os.listdir(path) if f.endswith(".txt")]
    for f in fichiers_notes:
        print(f)
    return fichiers_notes

# 2.
def lire_donnees(fichiers_notes, path="notes"):
    donnees = []
    for fichier in fichiers_notes:
        chemin = os.path.join(path, fichier)
        try:
            with open(chemin, encoding="utf-8") as f:
                reader = csv.reader(f)
                for ligne in reader:
                    if len(ligne) == 4:
                        donnees.append({
                            "nom": ligne[0].strip(),
                            "prenom": ligne[1].strip(),
                            "module": ligne[2].strip(),
                            "note": ligne[3].strip(),
                            "file": fichier
                        })
        except Exception as e:
            print(f"Erreur {fichier}: {e}")

    for d in donnees:
        print(d)
    return donnees

# 3.
def note_valide(note):
    try:
        n = float(note)
        return 0 <= n <= 20
    except Exception:
        return False

def filtrer_notes(donnees):
    notes_valides = [d for d in donnees if note_valide(d["note"])]
    notes_invalides = [d for d in donnees if not note_valide(d["note"])]
    print(f"{len(notes_valides)} notes OK, {len(notes_invalides)} notes KO")
    return notes_valides, notes_invalides

# 4.
def enregistrer_notes_invalides(notes_invalides):
    with open("notes_invalides.txt", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["nom", "prenom", "module", "note", "file"])
        for d in notes_invalides:
            writer.writerow([d["nom"], d["prenom"], d["module"], d["note"], d["file"]])

# 5.
def calculer_moyennes_etudiants(notes_valides):
    etudiants_notes = defaultdict(list)
    for d in notes_valides:
        etudiants_notes[(d["nom"], d["prenom"])].append(float(d["note"]))

    moyennes_etudiants = {
        f"{n} {p}": sum(notes) / len(notes)
        for (n, p), notes in etudiants_notes.items()
    }

    for etudiant, moyenne in moyennes_etudiants.items():
        print(f"{etudiant} : {moyenne:.2f}")

    return moyennes_etudiants

# 6.
def calculer_moyennes_modules(notes_valides):
    modules_notes = defaultdict(list)
    for d in notes_valides:
        modules_notes[d["module"]].append(float(d["note"]))

    moyennes_modules = {
        module: sum(notes) / len(notes)
        for module, notes in modules_notes.items()
    }

    for module, moyenne in moyennes_modules.items():
        print(f"{module} : {moyenne:.2f}")

    return moyennes_modules

# 7.
def trouver_top_etudiant(moyennes_etudiants):
    top_etudiant = max(moyennes_etudiants.items(), key=lambda x: x[1])
    print(f"best student : {top_etudiant[0]}, moy: {top_etudiant[1]:.2f}")
    return top_etudiant

# 8.
def enregistrer_resultats_csv(moyennes_etudiants):
    with open("resultats.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "moy"])
        for etu, moy in moyennes_etudiants.items():
            writer.writerow([etu, round(moy, 2)])

# 9.
def creer_rapport_notes(moyennes_etudiants, moyennes_modules, top_etudiant):
    with open("rapport_notes.txt", "w") as f:
        f.write("rapport\n\n")
        f.write(f"nb student: {len(moyennes_etudiants)}\n")
        f.write(f"nb module: {len(moyennes_modules)}\n\n")
        f.write("moy par module:\n")
        for module, moy in moyennes_modules.items():
            f.write(f"  - {module}: {round(moy, 2)}\n")
        f.write(f"\n best etudiant: {top_etudiant[0]} ({round(top_etudiant[1], 2)})\n")

# 10.
def creer_resultats_json(moyennes_etudiants, moyennes_modules, top_etudiant):
    resultats_json = {
        "moy_etudiant": moyennes_etudiants,
        "moy_module": moyennes_modules,
        "best_student": {
            "nom": top_etudiant[0],
            "moy": top_etudiant[1]
        }
    }

    with open("resultats.json", "w", encoding="utf-8") as f:
        json.dump(resultats_json, f, indent=4, ensure_ascii=False)

def main():
    fichiers_notes = lister_fichiers_notes()
    donnees = lire_donnees(fichiers_notes)
    notes_valides, notes_invalides = filtrer_notes(donnees)
    enregistrer_notes_invalides(notes_invalides)
    moyennes_etudiants = calculer_moyennes_etudiants(notes_valides)
