import tkinter as tk

class GestionNoms:
    def __init__(self, root):
        self.root = root
        root.title("GestionNoms")

        self.noms = self.charger_noms()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.btn_ajouter = tk.Button(root, text="ajout", command=self.ajouter_nom)
        self.btn_ajouter.pack()

        self.btn_afficher = tk.Button(root, text="Afficher tous", command=self.afficher_noms)
        self.btn_afficher.pack()

        self.label = tk.Label(root, text="")
        self.label.pack()

    def charger_noms(self):
        with open("noms.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]


    def ajouter_nom(self):
        nom = self.entry.get().strip()
        if nom:
            self.noms.append(nom)
            with open("noms.txt", "a") as f:
                f.write(nom + "\n")
            self.entry.delete(0, tk.END)
            self.afficher_noms()

    def afficher_noms(self):
        self.label.config(text="\n".join(self.noms))

root = tk.Tk()
app = GestionNoms(root)
root.mainloop()