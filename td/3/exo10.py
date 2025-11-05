class CompteBancaire:
    def __init__(self, numero, titulaire, solde):
        self.__numero = numero
        self.__titulaire = titulaire
        self.__solde = solde

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titulaire(self):
        return self.__titulaire

    @property
    def solde(self):
        return self.__solde
    
    @numero.setter
    def numero(self, n):
        self.__numero = n
    
    @titulaire.setter
    def titulaire(self, t):
        self.__titulaire = t

    @solde.setter
    def solde(self, s):
        if s < 0:
            raise ValueError("Solde negatif")
        self.__solde = s
    

    def verser(self, montant):
        self.__solde += montant

    def __str__(self):
        return f"Titu: {self.__titulaire}, solde: {self.__solde}, compte id: {self.__numero}"
    
mathieu = CompteBancaire(1, "Mathieu", 10)
print(mathieu)

mathieu.solde = 100
mathieu.verser(50)

print(mathieu)

mathieu.solde = -100