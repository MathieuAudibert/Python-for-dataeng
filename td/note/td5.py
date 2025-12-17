import tkinter as tk
import math

fnt = tk.Tk()

nb1 = tk.Entry(fnt)
nb1.pack()
nb2 = tk.Entry(fnt)
nb2.pack()

res = tk.StringVar()
histo = tk.Listbox(fnt)
histo.pack()

last = None

def get():
    if not nb1.get() or not nb2.get():
        histo.insert(tk.END, "nb1 or nb2 vide")
        return None
    try:
        return int(nb1.get()), int(nb2.get())
    except:
        histo.insert(tk.END, "nb pas int")
        return None

def add():
    global last
    v=get()
    if v:
        a,b=v
        r=a+b
        res.set(r)
        histo.insert(tk.END,f"{a}+{b}={r}")
        last=add

def sub():
    global last
    v=get()
    if v:
        a,b=v
        r=a-b
        res.set(r)
        histo.insert(tk.END,f"{a}-{b}={r}")
        last=sub

def mul():
    global last
    v=get()
    if v:
        a,b=v
        r=a*b
        res.set(r)
        histo.insert(tk.END,f"{a}*{b}={r}")
        last=mul

def div():
    global last
    v=get()
    if v:
        a,b=v
        if b==0:
            histo.insert(tk.END, "div 0 impossible")
        r=a/b
        res.set(r)
        histo.insert(tk.END,f"{a}/{b}={r}")
        last=div

def powr():
    global last
    v=get()
    if v:
        a,b=v
        r=a**b
        res.set(r)
        histo.insert(tk.END,f"{a}^{b}={r}")
        last=powr
    
def sqr():
    global last
    v=get()
    if v:
        a = v
        r=math.sqrt(int(a))
        res.set(r)
        histo.insert(tk.END,f"sqr{a}={r}")
        last=sqr

def refaire():
    if last:
        last()

def vider():
    histo.delete(0,tk.END)

def sauvegarder():
    with open('result.txt', 'w') as f:
        for i in histo.get(0, tk.END):
            f.write(i + "\n")

tk.Label(fnt,textvariable=res).pack()

tk.Button(fnt,text="+",command=add).pack()
tk.Button(fnt,text="-",command=sub).pack()
tk.Button(fnt,text="*",command=mul).pack()
tk.Button(fnt,text="/",command=div).pack()
tk.Button(fnt,text="^",command=powr).pack()
tk.Button(fnt, text="sqr", command=sqr).pack()
tk.Button(fnt,text="refaire",command=refaire).pack()
tk.Button(fnt,text="effacer",command=vider).pack()
tk.Button(fnt,text="sauvegarder",command=sauvegarder).pack()

fnt.mainloop()
