class Etudiant:
    def __init__(self, id_etudiant, nom_etudiant):
        self.id_etudiant = id_etudiant
        self.nom_etudiant = nom_etudiant

    def display(self):
        return f"ID etudiant: {self.id_etudiant}, nom: {self.nom_etudiant}"
    
etudiant2 = Etudiant(1, "Mathieu")
print(etudiant2.display())