class Vehicule:
    def __init__(self, vitesse_max, kilometrage, nom):
        self.nom = nom
        self.vitesse_max = vitesse_max
        self.kilometrage = kilometrage

class Bus(Vehicule):
    def nombre_de_place(self, capacite=50):
        return f"La capacité de {self.nom}, {capacite}"
bus = Bus(120, 120000, "bus")
