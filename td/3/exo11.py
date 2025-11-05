class Employe:
    def __init__(self, __id, __nom, __salaire):
        self.__id = __id
        self.__nom = __nom 
        self.__salaire = __salaire

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, i):
        self.__id = i

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, n):
        self.__nom = n
    
    @property
    def salaire(self):
        return self.__salaire
    @salaire.setter
    def salaire(self, s):
        if s >= 0:
            self.__salaire = s
        else:
            raise ValueError("Salaire negatif")
        
    def __str__(self):
        return f"Id: {self.__id}, Nom: {self.__nom}, Salaire: {self.__salaire}"

class Manager(Employe):
    def __init__(self, __id, __nom, __salaire, __prime):
        super().__init__(__id, __nom, __salaire)
        self.__prime = __prime

    def calculer_salaire_total(self):
        self.salaire += self.prime

    def __str__(self):
        return f"Id: {self.id}, Nom: {self.nom}, Salaire: {self.salaire}, Prime: {self.prime}"
    
    @property
    def prime(self):
        return self.__prime
    @prime.setter
    def prime(self, p):
        self.__prime = p

class Technicien(Employe):
    def __init__(self, __id, __nom, __salaire, __specialite):
        super().__init__(__id, __nom, __salaire)
        self.__specialite = __specialite
    
    @property
    def specialite(self):
        return self.__specialite
    @specialite.setter
    def specialite(self, sp):
        self.__specialite = sp
    
    def __str__(self):
        return f"Id: {self.id}, Nom: {self.nom}, Salaire: {self.salaire}, Specialite: {self.specialite}"

employe = Employe(1, "Employe", 1200)

manager = Manager(2, "Manager", 3000, 200)
manager.calculer_salaire_total()

technicien = Technicien(3, "Technicien", 1400, "Electricité")

employees = [manager, technicien]

for emp in employees:
    print(emp)