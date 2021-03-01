import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import numpy as np


turno=0

def controlloVittoria(m):  
    if m[0][0]!=' ' and m[0][1]!=' ' and m[0][2]!=' ' and m[1][0]!=' ' and m[1][1]!=' ' and m[1][2]!=' ' and m[2][0]!=' ' and m[2][1]!=' ' and m[2][2]!=' ':
        print("ciaoo")
        return False
    elif m[0][0]==m[0][1] and m[0][0]==m[0][2] and m[0][0]!=" ":
        return False
    elif m[1][0]==m[1][1] and m[1][0]==m[1][2] and m[1][0]!=" ":
        return False
    elif m[2][0]==m[2][1] and m[2][0]==m[2][2] and m[2][0]!=" ":
        return False
    elif m[0][0]==m[1][1] and m[0][0]==m[2][2] and m[0][0]!=" ":
        return False    
    elif m[0][2]==m[1][1] and m[0][2]==m[2][0] and m[0][2]!=" ":
        return False
    elif m[0][0]==m[1][0] and m[0][0]==m[2][0] and m[0][0]!=" ":
        return False
    elif m[0][1]==m[1][1] and m[0][1]==m[2][1] and m[0][1]!=" ":
        return False
    elif m[0][2]==m[1][2] and m[0][2]==m[2][2] and m[0][2]!=" ":
        return False
    
    else:
        return True

def controlloVittoriaSenzaPareggio(m):  
    if m[0][0]==m[0][1] and m[0][0]==m[0][2] and m[0][0]!=" ":
        return False
    elif m[1][0]==m[1][1] and m[1][0]==m[1][2] and m[1][0]!=" ":
        return False
    elif m[2][0]==m[2][1] and m[2][0]==m[2][2] and m[2][0]!=" ":
        return False
    elif m[0][0]==m[1][1] and m[0][0]==m[2][2] and m[0][0]!=" ":
        return False    
    elif m[0][2]==m[1][1] and m[0][2]==m[2][0] and m[0][2]!=" ":
        return False
    elif m[0][0]==m[1][0] and m[0][0]==m[2][0] and m[0][0]!=" ":
        return False
    elif m[0][1]==m[1][1] and m[0][1]==m[2][1] and m[0][1]!=" ":
        return False
    elif m[0][2]==m[1][2] and m[0][2]==m[2][2] and m[0][2]!=" ":
        return False
    
    else:
        return True


def inserisciSimbolo(scelta):
        if scelta=="00":
            if (turno%2==0):
                m[0][0]="X"
                b00.configure(text="X")
            else:
                m[0][0]="O"
                b00.configure(text="O")
        elif scelta=="01":
            if (turno%2==0):
                m[0][1]="X"
                b01.configure(text="X")
            else:
                m[0][1]="O"
                b01.configure(text="O")
        elif scelta=="02":
            if (turno%2==0):
                m[0][2]="X"
                b02.configure(text="X")
            else:
                m[0][2]="O"
                b02.configure(text="O")
        elif scelta=="10":
            if (turno%2==0):
                m[1][0]="X"
                b10.configure(text="X")
            else:
                m[1][0]="O"
                b10.configure(text="O")
        elif scelta=="11":
            if (turno%2==0):
                m[1][1]="X"
                b11.configure(text="X")
            else:
                m[1][1]="O"
                b11.configure(text="O")
        elif scelta=="12":
            if (turno%2==0):
                m[1][2]="X"
                b12.configure(text="X")
            else:
                m[1][2]="O"
                b12.configure(text="O")
        elif scelta=="20":
            if (turno%2==0):
                m[2][0]="X"
                b20.configure(text="X")
            else:
                m[2][0]="O"
                b20.configure(text="O")
        elif scelta=="21":
            if (turno%2==0):
                m[2][1]="X"
                b21.configure(text="X")
            else:
                m[2][1]="O"
                b21.configure(text="O")
        elif scelta=="22":
            if (turno%2==0):
                m[2][2]="X"
                b22.configure(text="X")
            else:
                m[2][2]="O"
                b22.configure(text="O")



m=np.array([[" "," "," "],[" "," "," "],[" "," "," "]])


def inserisci00():
    global turno
    global m
    inserisciSimbolo("00")
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    turno+=1
    b00['state'] = tk.DISABLED
    print(m)
    print(turno)
def inserisci01():
    global turno
    global m
    inserisciSimbolo("01")
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    turno+=1
    b01['state'] = tk.DISABLED
    print(m)
    print(turno)
def inserisci02():
    global turno
    global m
    inserisciSimbolo("02")
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    turno+=1
    b02['state'] = tk.DISABLED
    print(m)
    print(turno)
def inserisci10():
    global turno
    global m
    inserisciSimbolo("10")
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    
    turno+=1
    b10['state'] = tk.DISABLED
    print(m)
    print(turno)
def inserisci11():
    global turno
    global m
    inserisciSimbolo("11")
   
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    
    turno+=1
    b11['state'] = tk.DISABLED
    print(m)
    print(turno)
def inserisci12():
    global turno
    global m
    inserisciSimbolo("12")
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    
    turno+=1
    b12['state'] = tk.DISABLED
    print(m)
    print(turno)
def inserisci20():
    global turno
    global m
    inserisciSimbolo("20")
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    
    turno+=1
    b20['state'] = tk.DISABLED
    print(m)
    print(turno)
def inserisci21():
    global turno
    global m
    inserisciSimbolo("21")
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    
    turno+=1
    b21['state'] = tk.DISABLED
    print(m)
    print(turno)
def inserisci22():
    global turno
    global m
    inserisciSimbolo("22")
    if turno==8 and controlloVittoria(m)==False:
            if controlloVittoriaSenzaPareggio(m)==False:
                if turno%2==0:
                     messagebox.showinfo("Partita finita", "Vince giocatore 1")
                else:
                    messagebox.showinfo("Partita finita", "Vince giocatore 2")
            else:
                messagebox.showinfo("Partita finita", "PAREGGIO")
    elif controlloVittoria(m)==False:
        b00['state'] = tk.DISABLED
        b01['state'] = tk.DISABLED
        b02['state'] = tk.DISABLED
        b10['state'] = tk.DISABLED
        b11['state'] = tk.DISABLED
        b12['state'] = tk.DISABLED
        b20['state'] = tk.DISABLED
        b21['state'] = tk.DISABLED
        b22['state'] = tk.DISABLED
        if turno%2==0:
            messagebox.showinfo("Partita finita", "Vince giocatore 1")
        else:
            messagebox.showinfo("Partita finita", "Vince giocatore 2")
    turno+=1
    b22['state'] = tk.DISABLED
    print(m)
    print(turno)

win=tk.Tk()
win.title("TRIS")


b00=ttk.Button(win, text=" ", command=inserisci00)
b00.grid(column=0, row=0)
b01=ttk.Button(win, text=" ", command=inserisci01)
b01.grid(column=1, row=0)
b02=ttk.Button(win, text=" ", command=inserisci02)
b02.grid(column=2, row=0)
b10=ttk.Button(win, text=" ", command=inserisci10)
b10.grid(column=0, row=1)
b11=ttk.Button(win, text=" ", command=inserisci11)
b11.grid(column=1, row=1)
b12=ttk.Button(win, text=" ", command=inserisci12)
b12.grid(column=2, row=1)
b20=ttk.Button(win, text=" ", command=inserisci20)
b20.grid(column=0, row=2)
b21=ttk.Button(win, text=" ", command=inserisci21)
b21.grid(column=1, row=2)
b22=ttk.Button(win, text=" ", command=inserisci22)
b22.grid(column=2, row=2)


win.mainloop()