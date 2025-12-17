import tkinter as tk

fenetre = tk.Tk()
cadre = tk.Frame(fenetre, borderwidth=2, relief=tk.GROOVE)
cadre.pack(padx=10, pady=10)
tk.Label(cadre, text="Dans le cadre").pack()
tk.Label(cadre, text="OK").pack()
fenetre.mainloop()