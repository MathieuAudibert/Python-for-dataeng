import datetime

class BankAccount:
    def __init__(self, numero_compte, solde, date_ouverture, nom_du_client):
        self.numero_compte = numero_compte
        self.solde = solde
        self.date_ouverture = date_ouverture
        self.nom_du_client = nom_du_client
    
    def versement(self, compte_cible, montant):
        self.solde -= montant
        compte_cible.solde += montant

    def retrait(self, montant):
        self.solde -= montant

    def verifier_solde(self):
        print(self.solde)
    
    def __str__(self):
        return f"Numero cpt: {self.numero_compte}, Solde: {self.solde}, Date ouv: {self.date_ouverture}, Nom cli: {self.nom_du_client}"

mathieu = BankAccount(1, 20, datetime.datetime.now(), "Mathieu")
mathieu2 = BankAccount(2, 10, datetime.datetime.now(), "Mathieu2")

print(mathieu)
print(mathieu2)
print("---------------------------------------")

mathieu.versement(mathieu2, 5)

mathieu.retrait(10)

mathieu.verifier_solde()

print(mathieu)
print(mathieu2)
