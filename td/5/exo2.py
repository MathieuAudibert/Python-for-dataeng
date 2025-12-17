import tkinter as tk

fenetre = tk.Tk()
titre = tk.StringVar()
titre.set("Text inital")

def afficher_saisie():
    text = champ.get()
    print(text)
    titre.set("champ modifie")

tk.Label(fenetre, textvariable=titre).pack()

champ = tk.Entry(fenetre)
champ.pack()
btn = tk.Button(fenetre, text="changer le texte", command=afficher_saisie).pack()
fenetre.mainloop()