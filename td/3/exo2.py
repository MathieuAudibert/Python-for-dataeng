class Vehicule:
    def __init__(self, vitesse_max, kilometrage):
        self.vitesse_max = vitesse_max
        self.kilometrage = kilometrage

vehicule1 = Vehicule(100, 10)
print(vehicule1.vitesse_max, vehicule1.kilometrage)