class Voiture:
    wheels_number = 4
    vehicle_type = "Automobile"
    __color = ""

    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.__kilometrage = 0

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        if len(color) < 0:
            raise ValueError("La couleur ne peut pas etre vide")
        self.__color = color

    def rouler(self, distance):
        self.__kilometrage += distance
        return distance
    
    def afficher_info(self):
        return self.marque + " " + self.modele + " " + str(self.annee) + " " + self.__color + " " + str(self.__kilometrage)

tesla = Voiture("tesla", "model 3", 2023)
tesla.color = "blanche"
tesla.rouler(150)
tesla.color = "noir"
print(tesla.afficher_info())