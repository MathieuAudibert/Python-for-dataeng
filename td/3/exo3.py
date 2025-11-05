class Etudiant:
    def __init__(self, nom_etudiant, notes):
        self._nom_etudiant = nom_etudiant
        self._notes = notes
    
    @property
    def nom_etudiant(self):
        return self._nom_etudiant

    @property
    def notes(self):
        return self._notes
    
    @nom_etudiant.setter
    def nom_etudiant(self, nom_etudiant):
        self._nom_etudiant = nom_etudiant
    
    @notes.setter
    def notes(self, notes):
        self._notes = notes
    
etudiant1 = Etudiant('Audibert', [10, 12, 14])
print(etudiant1.nom_etudiant, etudiant1.notes)
etudiant1.nom_etudiant = "Agostino"
etudiant1.notes = [6, 2, 9]
print(etudiant1.nom_etudiant, etudiant1.notes)