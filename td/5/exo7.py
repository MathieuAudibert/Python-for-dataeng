import tkinter as tk

root = tk.Tk()

nom = tk.Entry(root, text="Nom")
age = tk.Entry(root, text="age")
msg = tk.StringVar()

def valide():
    if (len(nom.get()) == 0) or (int(age.get()) <= 0):
        msg.set("nom vide ou age negatif")
    else:
        msg.set("NOM: " + nom.get() + "AGE: " + age.get())

nom.pack()
age.pack()
tk.Button(root, text="valider", command=valide).pack()
tk.Label(root, textvariable=msg).pack()
root.mainloop()