class Restaurant:
    def __init__(self, menu_plats, reserver_table, commandes_clients):
        self.menu_plats = menu_plats
        self.reserver_table = reserver_table
        self.commandes_clients = commandes_clients

    def ajouter_plat(self, plat, prix):
        self.menu_plats[plat] = prix
    
    def reserver_tables(self, id_table):
        self.reserver_table.append(id_table)
    
    def prendre_commande(self, id_table, commande):
        self.commandes_clients.append(id_table, commande)
    
    def __str__(self):
        str_resto = ""
        for plat, prix in self.menu_plats.items():
            str_resto += f"Plat: {plat}; Prix: {prix} || "
        str_resto += f"\nTables reserves: {self.reserver_table}"
        for id_table, commande in self.commandes_clients.items():
            str_resto += f"\nTable ID: {id_table}, Commande: {commande}"
        return str_resto

restau = Restaurant({"Kebab": 8, "Café": 1},  [1, 2], {1: "Kebab"})
print(restau)

print("---------------------------")

restau.ajouter_plat("Caca", 2)
restau.reserver_tables(3)
print(restau)