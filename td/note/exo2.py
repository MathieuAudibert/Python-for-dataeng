import tkinter as tk
import os

fnt = tk.Tk()
tache = tk.Entry(fnt)
tache.pack()

taches = tk.Listbox(fnt)
taches.pack()
auto = tk.IntVar()

def ajouter():
    t = tache.get()
    if t:
        taches.insert(tk.END, t)
        tache.delete(0, tk.END)

def supprimer():
    s = taches.curselection()
    if s:
        idx = s[0]
        taches.delete(idx)

def tout_supprimer():
    taches.delete(0, tk.END)

def sauvegarder():
    with open("taches.txt", "w") as x:
        for i in taches.get(0, tk.END):
            x.write(i + "\n")

def charger():
    if os.path.exists("taches.txt"):
        taches.delete(0, tk.END)
        with open("taches.txt", "r") as x:
            for ligne in x:
                taches.insert(tk.END, ligne.strip())

def marquer():
    s = taches.curselection()
    if s:
        idx = s[0]
        t = taches.get(idx)
        nt = "[X] " + t if not t.startswith("[X]") else t.replace("[X] ", "")
        taches.delete(idx)
        taches.insert(idx, nt)

def modifier():
    s = taches.curselection()
    if s:
        idx = s[0]
    t = tache.get()
    if t:
        taches.delete(idx)
        taches.insert(idx, t)
        tache.delete(0, tk.END)

if auto.get() == 1:
    charger()

tk.Button(fnt, text="ajouter", command=ajouter).pack()
tk.Button(fnt, text="supprimer", command=supprimer).pack()
tk.Button(fnt, text="tout supprimer", command=tout_supprimer).pack()
tk.Button(fnt, text="sauveader", command=sauvegarder).pack()
tk.Button(fnt, text="charger", command=charger).pack()
tk.Button(fnt, text="terminer", command=marquer).pack()
tk.Button(fnt, text="modifieer", command=modifier).pack()

fnt.mainloop()