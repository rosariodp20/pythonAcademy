import numpy as np
import random
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def stampaMatrice(m,turno):
    if controlloVittoria(m):
        if (turno%2==0):
            print(f"{bcolors.OKGREEN}ORA TOCCA A GIOCATORE 1 (X): {bcolors.ENDC}")
        else:
            print(f"{bcolors.OKBLUE}ORA TOCCA A GIOCATORE 2 (O): {bcolors.ENDC}")
        print(m[0][0],"|",m[0][1],"|",m[0][2])
        print("---------")
        print(m[1][0],"|",m[1][1],"|",m[1][2])
        print("---------")
        print(m[2][0],"|",m[2][1],"|",m[2][2])
        print("\n")
        print("\n")
    else:
        print("\n")
        print("\n")
        print(f"{bcolors.OKCYAN}PARTITA FINITA{bcolors.ENDC}")
        print(m[0][0],"|",m[0][1],"|",m[0][2])
        print("---------")
        print(m[1][0],"|",m[1][1],"|",m[1][2])
        print("---------")
        print(m[2][0],"|",m[2][1],"|",m[2][2])

    

def controlloVittoria(m):  
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
    elif m[0][0]!=' ' and m[0][1]!=' ' and m[0][2]!=' ' and m[1][0]!=' ' and m[1][1]!=' ' and m[1][2]!=' ' and m[2][0]!=' ' and m[2][1]!=' ' and m[2][2]!=' ':
        return False
    else:
        return True


def inseriscePC(m,turno):
    ran=random.randint(0,8)
    scelta=""
    if ran==0:
        scelta="00"
    elif ran==1:
        scelta="01"
    elif ran==2:
        scelta="02"
    elif ran==3:
        scelta="10"
    elif ran==4:
        scelta="11"
    elif ran==5:
        scelta="12"
    elif ran==6:
        scelta="20"
    elif ran==7:
        scelta="21"
    elif ran==8:
        scelta="22"    
    if controllaOccupato(scelta, m):
        inseriscePC(m,turno)
    else:
        if scelta=="00":
            m[0][0]="O"
        elif scelta=="01":
            m[0][1]="O"
        elif scelta=="02":
            m[0][2]="O"
        elif scelta=="10":
            m[1][0]="O"
        elif scelta=="11":
            m[1][1]="O"
        elif scelta=="12":
            m[1][2]="O"
        elif scelta=="20":
            m[2][0]="O"
        elif scelta=="21":
            m[2][1]="O"
        elif scelta=="22":
            m[2][2]="O"

    


def inserisciSimbolo(m, turno):
    scelta= input("IN CHE POSIZIONE VUOI INSERIRE IL SIMBOLO (FORMATTAZIONE 00,01,02,11 ecc...): ")
    if scelta!="00" and scelta!="01" and scelta!="02" and scelta!="10" and scelta!="11" and scelta!="12" and scelta!="20" and scelta!="21" and scelta!="22":
        print(f"{bcolors.FAIL}POSIZIONE INESISTENTE{bcolors.ENDC}")
        inserisciSimbolo(m,turno)
    else:
        if controllaOccupato(scelta, m):
            print(f"{bcolors.WARNING}POSIZIONE OCCUPATA{bcolors.ENDC}")
            inserisciSimbolo(m,turno)
        else:
            if scelta=="00":
                m[0][0]="X"
            elif scelta=="01":
                m[0][1]="X"
            elif scelta=="02":
                m[0][2]="X"
            elif scelta=="10":
                m[1][0]="X"
            elif scelta=="11":
                m[1][1]="X"
            elif scelta=="12":
                m[1][2]="X"
            elif scelta=="20":
                m[2][0]="X"
            elif scelta=="21":
                m[2][1]="X"
            elif scelta=="22":
                m[2][2]="X"





def controllaOccupato(pos,m):
    if pos=="00":
        if m[0][0]!=" ":
            return True
        else:
            return False
    elif pos=="01":
        if m[0][1]!=" ":
            return True
        else:
            return False
    elif pos=="02":
        if m[0][2]!=" ":
            return True
        else:
            return False
    elif pos=="10":
        if m[1][0]!=" ":
            return True
        else:
            return False
    elif pos=="11":
        if m[1][1]!=" ":
            return True
        else:
            return False
    elif pos=="12":
        if m[1][2]!=" ":
            return True
        else:
            return False
    elif pos=="20":
        if m[2][0]!=" ":
            return True
        else:
            return False
    elif pos=="21":
        if m[2][1]!=" ":
            return True
        else:
            return False
    elif pos=="22":
        if m[2][2]!=" ":
            return True
        else:
            return False



############################## MAIN ############################################


m=np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
turno=0
print(f"{bcolors.OKCYAN}BENVENUTO IN TRIS{bcolors.ENDC}")
stampaMatrice(m,turno)

while controlloVittoria(m):
    if turno%2==0:
        inserisciSimbolo(m,turno)
    else:
        time.sleep(2)
        inseriscePC(m,turno)
    turno +=1    
    controlloVittoria(m)
    stampaMatrice(m,turno)

if m[0][0]!=' ' and m[0][1]!=' ' and m[0][2]!=' ' and m[1][0]!=' ' and m[1][1]!=' ' and m[1][2]!=' ' and m[2][0]!=' ' and m[2][1]!=' ' and m[2][2]!=' ':
        print(f"{bcolors.WARNING}PAREGGIO{bcolors.ENDC}")
else: 
    if(turno-1)%2==0:
        print(f"{bcolors.OKGREEN}VITTORIA GIOCATORE 1{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKBLUE}VITTORIA GIOCATORE 2{bcolors.ENDC}")


