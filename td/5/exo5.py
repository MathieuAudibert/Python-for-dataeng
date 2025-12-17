import tkinter as tk

root = tk.Tk()
output = tk.StringVar()
def read():
    with open('data.txt', 'r') as f:
        data = f.readlines()
    output.set(data)

tk.Label(root, textvariable=output).pack()
tk.Button(root, text="Afficher", command=read).pack()

root.mainloop()