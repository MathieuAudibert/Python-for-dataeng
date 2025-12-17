import tkinter as tk

fenetre = tk.Tk()

input = tk.Entry(fenetre)
output = tk.StringVar()

def afficher():
    input2 = input.get()
    output.set(input2)

lbl = tk.Label(fenetre, textvariable=output).pack()
input.pack()
tk.Button(fenetre,text="afficher", command=afficher).pack()
fenetre.mainloop()