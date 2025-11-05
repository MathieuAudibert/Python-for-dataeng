class Vehicule:
    def __init__(self, vitesse_max, kilometrage):
        self.vitesse_max = vitesse_max
        self.kilometrage = kilometrage

class Bus(Vehicule):
    def __str__(self):
        return f"Vitesse max: {self.vitesse_max}, Kilometrage: {self.kilometrage}"

bus = Bus(120, 120000)
print(bus)