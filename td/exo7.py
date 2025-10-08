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
        notes = i.get("notes")
        if isinstance(notes, list):
            for x in notes[:]:
                notes[notes.index(x)] = int(x)
        
        student_moy =  {}
        student_moy["nom"] = i.get("nom")
        student_moy["moyenne"] = sum(notes) / len(i.get("notes"))
        class_moy.append(student_moy)
    print(class_moy)
    return class_moy

def student_best_moy(liste_student):
    moyenne = moyenne_gen(liste_student)
    

def main():
    liste_student = []

    add_student(liste_student)
    remove_student(liste_student)
    moyenne_gen(liste_student)
    #student_best_moy(liste_student)

if __name__ == "__main__":
    main()