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
    student_moy =  {}
    for i in liste_student:
        student_moy[i.get("nom")] = i.get("notes")
        print(student_moy)

def main():
    liste_student = []

    add_student(liste_student)
    remove_student(liste_student)
    moyenne_gen(liste_student)

if __name__ == "__main__":
    main()