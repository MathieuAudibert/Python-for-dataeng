#!bin/bash/env/python3 

def add_student(liste_student):
    nb_student = int(input("Nombre de student: "))
    for _ in range(nb_student):
        student = {}
        nom = input("Nom de l'étudiant: ")
        nb_notes = int(input("Nombre de notes: "))
        notes_list = []
        for _ in range(nb_notes):
            notes = input("Notes: ")
            notes_list.append(notes)
        student['nom'] = nom
        student['notes'] = notes_list
        print(student)
        liste_student.append(student)

def remove_student(liste_student):
    print(liste_student)
    student = input("le nom du student a supprimer: ")
    for i in liste_student:
        if student == i.get("nom"):
            liste_student.remove(i)
            print("retiré")

def moyenne_gen(liste_student):
    print(liste_student)
    class_moy = []
    for i in liste_student:
        student_moy = {}
        notes = i.get("notes")
        
        if isinstance(notes, list):
            for x in notes[:]:
                notes[notes.index(x)] = int(x)
        
        student_moy["nom"] = i.get("nom")
        student_moy["moyenne"] = int(sum(notes) / len(i.get("notes")))
        class_moy.append(student_moy)
    return class_moy
    
def student_best_moy(liste_student):
    moyenne = moyenne_gen(liste_student)
    print(moyenne)

    best_student = max(moyenne, key=lambda x: x["moyenne"])
    print(f"{best_student['nom']}: {best_student['moyenne']}")

def main():
    liste_student = []

    add_student(liste_student)
    remove_student(liste_student)
    moyennes = moyenne_gen(liste_student)
    best_student = None
    if moyennes:
        best_student = max(moyennes, key=lambda x: x["moyenne"])

    with open("result.txt", 'w') as f:
        f.write("liste student:\n")
        for student in liste_student:
            f.write(f"{student['nom']}: {student['notes']}\n")
        f.write("\nmoyenne:\n")
        for m in moyennes:
            f.write(f"{m['nom']}: {m['moyenne']}\n")
        if best_student:
            f.write(f"\nbest moy: {best_student['nom']}: {best_student['moyenne']}\n")

if __name__ == "__main__":
    main()