import tkinter as tk

root = tk.Tk()
mot = tk.Entry(root)
mot.pack()
msg = tk.StringVar()

def ajouter():
    with open('liste.txt', 'a') as f:
        f.write(mot.get() + "\n")

def afficher():
    with open('liste.txt', 'r') as f:
        msg.set(f.readlines())
    
def vider():
    open('liste.txt', 'w').close()

tk.Button(root, text="afficher", command=afficher).pack()
tk.Label(root, textvariable=msg).pack()
tk.Button(root, text="ajouter", command=ajouter).pack()
tk.Button(root, text="vider", command=vider).pack()

root.mainloop()