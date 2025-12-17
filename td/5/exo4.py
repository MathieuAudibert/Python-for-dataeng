import tkinter as tk

root = tk.Tk()
txt = tk.Entry(root)
txt.pack()

def save():
    with open('data.txt', 'w') as f:
        f.write(txt.get())

btn = tk.Button(root, text="Sauvegarder", command=save).pack()
root.mainloop()