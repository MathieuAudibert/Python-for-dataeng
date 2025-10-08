#!bin/bash/env/python3 

def add_student(liste_student):
    student = {}
    nb_student = int(input("Nombre de student: "))
    for i in range(nb_student):
        nom = input("Nom de l'étudiant: ")
        nb_notes = int(input("Nombre de notes: "))
        notes_list = []
        for i in range(nb_notes):
            notes = input("Notes: ")
            notes_list.append(notes)
        student['nom'] = nom
        student['notes'] = notes_list
        print(student)
        liste_student.append(student)

def remove_student(liste_student):
    print(liste_student)
    student = input("le nom du student a supprimer: ")
    for i in liste_student
    if student == liste_student.get("nom"):
        liste_student.remove(student)
        print("retiré")

def moyenne_gen(liste_student):

def main():
    liste_student = []

    add_student(liste_student)
    remove_student(liste_student)

if __name__ == "__main__":
    main()