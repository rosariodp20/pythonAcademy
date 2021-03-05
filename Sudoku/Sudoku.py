import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import random
import copy


##################################################### FUNZIONE PER INSERIMENTO DI UN NUMERO #####################################################

def inserisci(n:str):
    if n=="00":
        if sudoku[0][0]==" ":
            sudoku[0][0]=1
            b00.configure(text=sudoku[0][0])
            controllaVittoria()
        elif sudoku[0][0]==9:
            sudoku[0][0]=" "
            b00.configure(text=sudoku[0][0])
        else:
            sudoku[0][0]+=1
            b00.configure(text=sudoku[0][0])
            controllaVittoria()
    elif n=="01":
        if sudoku[0][1]==" ":
            sudoku[0][1]=1
            b01.configure(text=sudoku[0][1])
            controllaVittoria()
        elif sudoku[0][1]==9:
            sudoku[0][1]=" "
            b01.configure(text=sudoku[0][1])
        else:
            sudoku[0][1]+=1
            b01.configure(text=sudoku[0][1])
            controllaVittoria()
    elif n=="02":
        if sudoku[0][2]==" ":
            sudoku[0][2]=1
            b02.configure(text=sudoku[0][2])
            controllaVittoria()
        elif sudoku[0][2]==9:
            sudoku[0][2]=" "
            b02.configure(text=sudoku[0][2])
        else:
            sudoku[0][2]+=1
            b02.configure(text=sudoku[0][2])
            controllaVittoria()
    elif n=="03":
        if sudoku[0][3]==" ":
            sudoku[0][3]=1
            b03.configure(text=sudoku[0][3])
            controllaVittoria()
        elif sudoku[0][3]==9:
            sudoku[0][3]=" "
            b03.configure(text=sudoku[0][3])
        else:
            sudoku[0][3]+=1
            b03.configure(text=sudoku[0][3])
            controllaVittoria()
    elif n=="04":
        if sudoku[0][4]==" ":
            sudoku[0][4]=1
            b04.configure(text=sudoku[0][4])
            controllaVittoria()
        elif sudoku[0][4]==9:
            sudoku[0][4]=" "
            b04.configure(text=sudoku[0][4])
        else:
            sudoku[0][4]+=1
            b04.configure(text=sudoku[0][4])
            controllaVittoria()
    elif n=="05":
        if sudoku[0][5]==" ":
            sudoku[0][5]=1
            b05.configure(text=sudoku[0][5])
            controllaVittoria()
        elif sudoku[0][5]==9:
            sudoku[0][5]=" "
            b05.configure(text=sudoku[0][5])
        else:
            sudoku[0][5]+=1
            b05.configure(text=sudoku[0][5])
            controllaVittoria()
    elif n=="06":
        if sudoku[0][6]==" ":
            sudoku[0][6]=1
            b06.configure(text=sudoku[0][6])
            controllaVittoria()
        elif sudoku[0][6]==9:
            sudoku[0][6]=" "
            b06.configure(text=sudoku[0][6])
        else:
            sudoku[0][6]+=1
            b06.configure(text=sudoku[0][6])
            controllaVittoria()
    elif n=="07":
        if sudoku[0][7]==" ":
            sudoku[0][7]=1
            b07.configure(text=sudoku[0][7])
            controllaVittoria()
        elif sudoku[0][7]==9:
            sudoku[0][7]=" "
            b07.configure(text=sudoku[0][7])
        else:
            sudoku[0][7]+=1
            b07.configure(text=sudoku[0][7])
            controllaVittoria()
    elif n=="08":
        if sudoku[0][8]==" ":
            sudoku[0][8]=1
            b08.configure(text=sudoku[0][8])
            controllaVittoria()
        elif sudoku[0][8]==9:
            sudoku[0][8]=" "
            b08.configure(text=sudoku[0][8])
        else:
            sudoku[0][8]+=1
            b08.configure(text=sudoku[0][8])
            controllaVittoria()
    elif n=="10":
        if sudoku[1][0]==" ":
            sudoku[1][0]=1
            b10.configure(text=sudoku[1][0])
            controllaVittoria()
        elif sudoku[1][0]==9:
            sudoku[1][0]=" "
            b10.configure(text=sudoku[1][0])
        else:
            sudoku[1][0]+=1
            b10.configure(text=sudoku[1][0])
            controllaVittoria()
    elif n=="11":
        if sudoku[1][1]==" ":
            sudoku[1][1]=1
            b11.configure(text=sudoku[1][1])
            controllaVittoria()
        elif sudoku[1][1]==9:
            sudoku[1][1]=" "
            b11.configure(text=sudoku[1][1])
        else:
            sudoku[1][1]+=1
            b11.configure(text=sudoku[1][1])
            controllaVittoria()
    elif n=="12":
        if sudoku[1][2]==" ":
            sudoku[1][2]=1
            b12.configure(text=sudoku[1][2])
            controllaVittoria()
        elif sudoku[1][2]==9:
            sudoku[1][2]=" "
            b12.configure(text=sudoku[1][2])
        else:
            sudoku[1][2]+=1
            b12.configure(text=sudoku[1][2])
            controllaVittoria()
    elif n=="13":
        if sudoku[1][3]==" ":
            sudoku[1][3]=1
            b13.configure(text=sudoku[1][3])
            controllaVittoria()
        elif sudoku[1][3]==9:
            sudoku[1][3]=" "
            b13.configure(text=sudoku[1][3])
        else:
            sudoku[1][3]+=1
            b13.configure(text=sudoku[1][3])
            controllaVittoria()
    elif n=="14":
        if sudoku[1][4]==" ":
            sudoku[1][4]=1
            b14.configure(text=sudoku[1][4])
            controllaVittoria()
        elif sudoku[1][4]==9:
            sudoku[1][4]=" "
            b14.configure(text=sudoku[1][4])
        else:
            sudoku[1][4]+=1
            b14.configure(text=sudoku[1][4])
            controllaVittoria()
    elif n=="15":
        if sudoku[1][5]==" ":
            sudoku[1][5]=1
            b15.configure(text=sudoku[1][5])
            controllaVittoria()
        elif sudoku[1][5]==9:
            sudoku[1][5]=" "
            b15.configure(text=sudoku[1][5])
        else:
            sudoku[1][5]+=1
            b15.configure(text=sudoku[1][5])
            controllaVittoria()
    elif n=="16":
        if sudoku[1][6]==" ":
            sudoku[1][6]=1
            b16.configure(text=sudoku[1][6])
            controllaVittoria()
        elif sudoku[1][6]==9:
            sudoku[1][6]=" "
            b16.configure(text=sudoku[1][6])
        else:
            sudoku[1][6]+=1
            b16.configure(text=sudoku[1][6])
            controllaVittoria()
    elif n=="17":
        if sudoku[1][7]==" ":
            sudoku[1][7]=1
            b17.configure(text=sudoku[1][7])
            controllaVittoria()
        elif sudoku[1][7]==9:
            sudoku[1][7]=" "
            b17.configure(text=sudoku[1][7])
        else:
            sudoku[1][7]+=1
            b17.configure(text=sudoku[1][7])
            controllaVittoria()
    elif n=="18":
        if sudoku[1][8]==" ":
            sudoku[1][8]=1
            b18.configure(text=sudoku[1][8])
            controllaVittoria()
        elif sudoku[1][8]==9:
            sudoku[1][8]=" "
            b18.configure(text=sudoku[1][8])
        else:
            sudoku[1][8]+=1
            b18.configure(text=sudoku[1][8])
            controllaVittoria()
    elif n=="20":
        if sudoku[2][0]==" ":
            sudoku[2][0]=1
            b20.configure(text=sudoku[2][0])
            controllaVittoria()
        elif sudoku[2][0]==9:
            sudoku[2][0]=" "
            b20.configure(text=sudoku[2][0])
        else:
            sudoku[2][0]+=1
            b20.configure(text=sudoku[2][0])
            controllaVittoria()
    elif n=="21":
        if sudoku[2][1]==" ":
            sudoku[2][1]=1
            b21.configure(text=sudoku[2][1])
            controllaVittoria()
        elif sudoku[2][1]==9:
            sudoku[2][1]=" "
            b21.configure(text=sudoku[2][1])
        else:
            sudoku[2][1]+=1
            b21.configure(text=sudoku[2][1])
            controllaVittoria()
    elif n=="22":
        if sudoku[2][2]==" ":
            sudoku[2][2]=1
            b22.configure(text=sudoku[2][2])
            controllaVittoria()
        elif sudoku[2][2]==9:
            sudoku[2][2]=" "
            b22.configure(text=sudoku[2][2])
        else:
            sudoku[2][2]+=1
            b22.configure(text=sudoku[2][2])
            controllaVittoria()
    elif n=="23":
        if sudoku[2][3]==" ":
            sudoku[2][3]=1
            b23.configure(text=sudoku[2][3])
            controllaVittoria()
        elif sudoku[2][3]==9:
            sudoku[2][3]=" "
            b23.configure(text=sudoku[2][3])
        else:
            sudoku[2][3]+=1
            b23.configure(text=sudoku[2][3])
            controllaVittoria()
    elif n=="24":
        if sudoku[2][4]==" ":
            sudoku[2][4]=1
            b24.configure(text=sudoku[2][4])
            controllaVittoria()
        elif sudoku[2][4]==9:
            sudoku[2][4]=" "
            b24.configure(text=sudoku[2][4])
        else:
            sudoku[2][4]+=1
            b24.configure(text=sudoku[2][4])
            controllaVittoria()
    elif n=="25":
        if sudoku[2][5]==" ":
            sudoku[2][5]=1
            b25.configure(text=sudoku[2][5])
            controllaVittoria()
        elif sudoku[2][5]==9:
            sudoku[2][5]=" "
            b25.configure(text=sudoku[2][5])
        else:
            sudoku[2][5]+=1
            b25.configure(text=sudoku[2][5])
            controllaVittoria()
    elif n=="26":
        if sudoku[2][6]==" ":
            sudoku[2][6]=1
            b26.configure(text=sudoku[2][6])
            controllaVittoria()
        elif sudoku[2][6]==9:
            sudoku[2][6]=" "
            b26.configure(text=sudoku[2][6])
        else:
            sudoku[2][6]+=1
            b26.configure(text=sudoku[2][6])
            controllaVittoria()
    elif n=="27":
        if sudoku[2][7]==" ":
            sudoku[2][7]=1
            b27.configure(text=sudoku[2][7])
            controllaVittoria()
        elif sudoku[2][7]==9:
            sudoku[2][7]=" "
            b27.configure(text=sudoku[2][7])
        else:
            sudoku[2][7]+=1
            b27.configure(text=sudoku[2][7])
            controllaVittoria()
    elif n=="28":
        if sudoku[2][8]==" ":
            sudoku[2][8]=1
            b28.configure(text=sudoku[2][8])
            controllaVittoria()
        elif sudoku[2][8]==9:
            sudoku[2][8]=" "
            b28.configure(text=sudoku[2][8])
        else:
            sudoku[2][8]+=1
            b28.configure(text=sudoku[2][8])
            controllaVittoria()
    elif n=="30":
        if sudoku[3][0]==" ":
            sudoku[3][0]=1
            b30.configure(text=sudoku[3][0])
            controllaVittoria()
        elif sudoku[3][0]==9:
            sudoku[3][0]=" "
            b30.configure(text=sudoku[3][0])
        else:
            sudoku[3][0]+=1
            b30.configure(text=sudoku[3][0])
            controllaVittoria()
    elif n=="31":
        if sudoku[3][1]==" ":
            sudoku[3][1]=1
            b31.configure(text=sudoku[3][1])
            controllaVittoria()
        elif sudoku[3][1]==9:
            sudoku[3][1]=" "
            b31.configure(text=sudoku[3][1])
        else:
            sudoku[3][1]+=1
            b31.configure(text=sudoku[3][1])
            controllaVittoria()
    elif n=="32":
        if sudoku[3][2]==" ":
            sudoku[3][2]=1
            b32.configure(text=sudoku[3][2])
            controllaVittoria()
        elif sudoku[3][2]==9:
            sudoku[3][2]=" "
            b32.configure(text=sudoku[3][2])
        else:
            sudoku[3][2]+=1
            b32.configure(text=sudoku[3][2])
            controllaVittoria()
    elif n=="33":
        if sudoku[3][3]==" ":
            sudoku[3][3]=1
            b33.configure(text=sudoku[3][3])
            controllaVittoria()
        elif sudoku[3][3]==9:
            sudoku[3][3]=" "
            b33.configure(text=sudoku[3][3])
        else:
            sudoku[3][3]+=1
            b33.configure(text=sudoku[3][3])
            controllaVittoria()
    elif n=="34":
        if sudoku[3][4]==" ":
            sudoku[3][4]=1
            b34.configure(text=sudoku[3][4])
            controllaVittoria()
        elif sudoku[3][4]==9:
            sudoku[3][4]=" "
            b34.configure(text=sudoku[3][4])
        else:
            sudoku[3][4]+=1
            b34.configure(text=sudoku[3][4])
            controllaVittoria()
    elif n=="35":
        if sudoku[3][5]==" ":
            sudoku[3][5]=1
            b35.configure(text=sudoku[3][5])
            controllaVittoria()
        elif sudoku[3][5]==9:
            sudoku[3][5]=" "
            b35.configure(text=sudoku[3][5])
        else:
            sudoku[3][5]+=1
            b35.configure(text=sudoku[3][5])
            controllaVittoria()
    elif n=="36":
        if sudoku[3][6]==" ":
            sudoku[3][6]=1
            b36.configure(text=sudoku[3][6])
            controllaVittoria()
        elif sudoku[3][6]==9:
            sudoku[3][6]=" "
            b36.configure(text=sudoku[3][6])
        else:
            sudoku[3][6]+=1
            b36.configure(text=sudoku[3][6])
            controllaVittoria()
    elif n=="37":
        if sudoku[3][7]==" ":
            sudoku[3][7]=1
            b37.configure(text=sudoku[3][7])
            controllaVittoria()
        elif sudoku[3][7]==9:
            sudoku[3][7]=" "
            b37.configure(text=sudoku[3][7])
        else:
            sudoku[3][7]+=1
            b37.configure(text=sudoku[3][7])
            controllaVittoria()
    elif n=="38":
        if sudoku[3][8]==" ":
            sudoku[3][8]=1
            b38.configure(text=sudoku[3][8])
            controllaVittoria()
        elif sudoku[3][8]==9:
            sudoku[3][8]=" "
            b38.configure(text=sudoku[3][8])
        else:
            sudoku[3][8]+=1
            b38.configure(text=sudoku[3][8])
            controllaVittoria()
    elif n=="40":
        if sudoku[4][0]==" ":
            sudoku[4][0]=1
            b40.configure(text=sudoku[4][0])
            controllaVittoria()
        elif sudoku[4][0]==9:
            sudoku[4][0]=" "
            b40.configure(text=sudoku[4][0])
        else:
            sudoku[4][0]+=1
            b40.configure(text=sudoku[4][0])
            controllaVittoria()
    elif n=="41":
        if sudoku[4][1]==" ":
            sudoku[4][1]=1
            b41.configure(text=sudoku[4][1])
            controllaVittoria()
        elif sudoku[4][1]==9:
            sudoku[4][1]=" "
            b41.configure(text=sudoku[4][1])
        else:
            sudoku[4][1]+=1
            b41.configure(text=sudoku[4][1])
            controllaVittoria()
    elif n=="42":
        if sudoku[4][2]==" ":
            sudoku[4][2]=1
            b42.configure(text=sudoku[4][2])
            controllaVittoria()
        elif sudoku[4][2]==9:
            sudoku[4][2]=" "
            b42.configure(text=sudoku[4][2])
        else:
            sudoku[4][2]+=1
            b42.configure(text=sudoku[4][2])
            controllaVittoria()
    elif n=="43":
        if sudoku[4][3]==" ":
            sudoku[4][3]=1
            b43.configure(text=sudoku[4][3])
            controllaVittoria()
        elif sudoku[4][3]==9:
            sudoku[4][3]=" "
            b43.configure(text=sudoku[4][3])
        else:
            sudoku[4][3]+=1
            b43.configure(text=sudoku[4][3])
            controllaVittoria()
    elif n=="44":
        if sudoku[4][4]==" ":
            sudoku[4][4]=1
            b44.configure(text=sudoku[4][4])
            controllaVittoria()
        elif sudoku[4][4]==9:
            sudoku[4][4]=" "
            b44.configure(text=sudoku[4][4])
        else:
            sudoku[4][4]+=1
            b44.configure(text=sudoku[4][4])
            controllaVittoria()
    elif n=="45":
        if sudoku[4][5]==" ":
            sudoku[4][5]=1
            b45.configure(text=sudoku[4][5])
            controllaVittoria()
        elif sudoku[4][5]==9:
            sudoku[4][5]=" "
            b45.configure(text=sudoku[4][5])
        else:
            sudoku[4][5]+=1
            b45.configure(text=sudoku[4][5])
            controllaVittoria()
    elif n=="46":
        if sudoku[4][6]==" ":
            sudoku[4][6]=1
            b46.configure(text=sudoku[4][6])
            controllaVittoria()
        elif sudoku[4][6]==9:
            sudoku[4][6]=" "
            b46.configure(text=sudoku[4][6])
        else:
            sudoku[4][6]+=1
            b46.configure(text=sudoku[4][6])
            controllaVittoria()
    elif n=="47":
        if sudoku[4][7]==" ":
            sudoku[4][7]=1
            b47.configure(text=sudoku[4][7])
            controllaVittoria()
        elif sudoku[4][7]==9:
            sudoku[4][7]=" "
            b47.configure(text=sudoku[4][7])
        else:
            sudoku[4][7]+=1
            b47.configure(text=sudoku[4][7])
            controllaVittoria()
    elif n=="48":
        if sudoku[4][8]==" ":
            sudoku[4][8]=1
            b48.configure(text=sudoku[4][8])
            controllaVittoria()
        elif sudoku[4][8]==9:
            sudoku[4][8]=" "
            b48.configure(text=sudoku[4][8])
        else:
            sudoku[4][8]+=1
            b48.configure(text=sudoku[4][8])
            controllaVittoria()
    elif n=="50":
        if sudoku[5][0]==" ":
            sudoku[5][0]=1
            b50.configure(text=sudoku[5][0])
            controllaVittoria()
        elif sudoku[5][0]==9:
            sudoku[5][0]=" "
            b50.configure(text=sudoku[5][0])
        else:
            sudoku[5][0]+=1
            b50.configure(text=sudoku[5][0])
            controllaVittoria()
    elif n=="51":
        if sudoku[5][1]==" ":
            sudoku[5][1]=1
            b51.configure(text=sudoku[5][1])
            controllaVittoria()
        elif sudoku[5][1]==9:
            sudoku[5][1]=" "
            b51.configure(text=sudoku[5][1])
        else:
            sudoku[5][1]+=1
            b51.configure(text=sudoku[5][1])
            controllaVittoria()
    elif n=="52":
        if sudoku[5][2]==" ":
            sudoku[5][2]=1
            b52.configure(text=sudoku[5][2])
            controllaVittoria()
        elif sudoku[5][2]==9:
            sudoku[5][2]=" "
            b52.configure(text=sudoku[5][2])
        else:
            sudoku[5][2]+=1
            b52.configure(text=sudoku[5][2])
            controllaVittoria()
    elif n=="53":
        if sudoku[5][3]==" ":
            sudoku[5][3]=1
            b53.configure(text=sudoku[5][3])
            controllaVittoria()
        elif sudoku[5][3]==9:
            sudoku[5][3]=" "
            b53.configure(text=sudoku[5][3])
        else:
            sudoku[5][3]+=1
            b53.configure(text=sudoku[5][3])
            controllaVittoria()
    elif n=="54":
        if sudoku[5][4]==" ":
            sudoku[5][4]=1
            b54.configure(text=sudoku[5][4])
            controllaVittoria()
        elif sudoku[5][4]==9:
            sudoku[5][4]=" "
            b54.configure(text=sudoku[5][4])
        else:
            sudoku[5][4]+=1
            b54.configure(text=sudoku[5][4])
            controllaVittoria()
    elif n=="55":
        if sudoku[5][5]==" ":
            sudoku[5][5]=1
            b55.configure(text=sudoku[5][5])
            controllaVittoria()
        elif sudoku[5][5]==9:
            sudoku[5][5]=" "
            b55.configure(text=sudoku[5][5])
        else:
            sudoku[5][5]+=1
            b55.configure(text=sudoku[5][5])
            controllaVittoria()
    elif n=="56":
        if sudoku[5][6]==" ":
            sudoku[5][6]=1
            b56.configure(text=sudoku[5][6])
            controllaVittoria()
        elif sudoku[5][6]==9:
            sudoku[5][6]=" "
            b56.configure(text=sudoku[5][6])
        else:
            sudoku[5][6]+=1
            b56.configure(text=sudoku[5][6])
            controllaVittoria()
    elif n=="57":
        if sudoku[5][7]==" ":
            sudoku[5][7]=1
            b57.configure(text=sudoku[5][7])
            controllaVittoria()
        elif sudoku[5][7]==9:
            sudoku[5][7]=" "
            b57.configure(text=sudoku[5][7])
        else:
            sudoku[5][7]+=1
            b57.configure(text=sudoku[5][7])
            controllaVittoria()
    elif n=="58":
        if sudoku[5][8]==" ":
            sudoku[5][8]=1
            b58.configure(text=sudoku[5][8])
            controllaVittoria()
        elif sudoku[5][8]==9:
            sudoku[5][8]=" "
            b58.configure(text=sudoku[5][8])
        else:
            sudoku[5][8]+=1
            b58.configure(text=sudoku[5][8])
            controllaVittoria()
    elif n=="60":
        if sudoku[6][0]==" ":
            sudoku[6][0]=1
            b60.configure(text=sudoku[6][0])
            controllaVittoria()
        elif sudoku[6][0]==9:
            sudoku[6][0]=" "
            b60.configure(text=sudoku[6][0])
        else:
            sudoku[6][0]+=1
            b60.configure(text=sudoku[6][0])
            controllaVittoria()
    elif n=="61":
        if sudoku[6][1]==" ":
            sudoku[6][1]=1
            b61.configure(text=sudoku[6][1])
            controllaVittoria()
        elif sudoku[6][1]==9:
            sudoku[6][1]=" "
            b61.configure(text=sudoku[6][1])
        else:
            sudoku[6][1]+=1
            b61.configure(text=sudoku[6][1])
            controllaVittoria()
    elif n=="62":
        if sudoku[6][2]==" ":
            sudoku[6][2]=1
            b62.configure(text=sudoku[6][2])
            controllaVittoria()
        elif sudoku[6][2]==9:
            sudoku[6][2]=" "
            b62.configure(text=sudoku[6][2])
        else:
            sudoku[6][2]+=1
            b62.configure(text=sudoku[6][2])
            controllaVittoria()
    elif n=="63":
        if sudoku[6][3]==" ":
            sudoku[6][3]=1
            b63.configure(text=sudoku[6][3])
            controllaVittoria()
        elif sudoku[6][3]==9:
            sudoku[6][3]=" "
            b63.configure(text=sudoku[6][3])
        else:
            sudoku[6][3]+=1
            b63.configure(text=sudoku[6][3])
            controllaVittoria()
    elif n=="64":
        if sudoku[6][4]==" ":
            sudoku[6][4]=1
            b64.configure(text=sudoku[6][4])
            controllaVittoria()
        elif sudoku[6][4]==9:
            sudoku[6][4]=" "
            b64.configure(text=sudoku[6][4])
        else:
            sudoku[6][4]+=1
            b64.configure(text=sudoku[6][4])
            controllaVittoria()
    elif n=="65":
        if sudoku[6][5]==" ":
            sudoku[6][5]=1
            b65.configure(text=sudoku[6][5])
            controllaVittoria()
        elif sudoku[6][5]==9:
            sudoku[6][5]=" "
            b65.configure(text=sudoku[6][5])
        else:
            sudoku[6][5]+=1
            b65.configure(text=sudoku[6][5])
            controllaVittoria()
    elif n=="66":
        if sudoku[6][6]==" ":
            sudoku[6][6]=1
            b66.configure(text=sudoku[6][6])
            controllaVittoria()
        elif sudoku[6][6]==9:
            sudoku[6][6]=" "
            b66.configure(text=sudoku[6][6])
        else:
            sudoku[6][6]+=1
            b66.configure(text=sudoku[6][6])
            controllaVittoria()
    elif n=="67":
        if sudoku[6][7]==" ":
            sudoku[6][7]=1
            b67.configure(text=sudoku[6][7])
            controllaVittoria()
        elif sudoku[6][7]==9:
            sudoku[6][7]=" "
            b67.configure(text=sudoku[6][7])
        else:
            sudoku[6][7]+=1
            b67.configure(text=sudoku[6][7])
            controllaVittoria()
    elif n=="68":
        if sudoku[6][8]==" ":
            sudoku[6][8]=1
            b68.configure(text=sudoku[6][8])
            controllaVittoria()
        elif sudoku[6][8]==9:
            sudoku[6][8]=" "
            b68.configure(text=sudoku[6][8])
        else:
            sudoku[6][8]+=1
            b68.configure(text=sudoku[6][8])
            controllaVittoria()
    elif n=="70":
        if sudoku[7][0]==" ":
            sudoku[7][0]=1
            b70.configure(text=sudoku[7][0])
            controllaVittoria()
        elif sudoku[7][0]==9:
            sudoku[7][0]=" "
            b70.configure(text=sudoku[7][0])
        else:
            sudoku[7][0]+=1
            b70.configure(text=sudoku[7][0])
            controllaVittoria()
    elif n=="71":
        if sudoku[7][1]==" ":
            sudoku[7][1]=1
            b71.configure(text=sudoku[7][1])
            controllaVittoria()
        elif sudoku[7][1]==9:
            sudoku[7][1]=" "
            b71.configure(text=sudoku[7][1])
        else:
            sudoku[7][1]+=1
            b71.configure(text=sudoku[7][1])
            controllaVittoria()
    elif n=="72":
        if sudoku[7][2]==" ":
            sudoku[7][2]=1
            b72.configure(text=sudoku[7][2])
            controllaVittoria()
        elif sudoku[7][2]==9:
            sudoku[7][2]=" "
            b72.configure(text=sudoku[7][2])
        else:
            sudoku[7][2]+=1
            b72.configure(text=sudoku[7][2])
            controllaVittoria()
    elif n=="73":
        if sudoku[7][3]==" ":
            sudoku[7][3]=1
            b73.configure(text=sudoku[7][3])
            controllaVittoria()
        elif sudoku[7][3]==9:
            sudoku[7][3]=" "
            b73.configure(text=sudoku[7][3])
        else:
            sudoku[7][3]+=1
            b73.configure(text=sudoku[7][3])
            controllaVittoria()
    elif n=="74":
        if sudoku[7][4]==" ":
            sudoku[7][4]=1
            b74.configure(text=sudoku[7][4])
            controllaVittoria()
        elif sudoku[7][4]==9:
            sudoku[7][4]=" "
            b74.configure(text=sudoku[7][4])
        else:
            sudoku[7][4]+=1
            b74.configure(text=sudoku[7][4])
            controllaVittoria()
    elif n=="75":
        if sudoku[7][5]==" ":
            sudoku[7][5]=1
            b75.configure(text=sudoku[7][5])
            controllaVittoria()
        elif sudoku[7][5]==9:
            sudoku[7][5]=" "
            b75.configure(text=sudoku[7][5])
        else:
            sudoku[7][5]+=1
            b75.configure(text=sudoku[7][5])
            controllaVittoria()
    elif n=="76":
        if sudoku[7][6]==" ":
            sudoku[7][6]=1
            b76.configure(text=sudoku[7][6])
            controllaVittoria()
        elif sudoku[7][6]==9:
            sudoku[7][6]=" "
            b76.configure(text=sudoku[7][6])
        else:
            sudoku[7][6]+=1
            b76.configure(text=sudoku[7][6])
            controllaVittoria()
    elif n=="77":
        if sudoku[7][7]==" ":
            sudoku[7][7]=1
            b77.configure(text=sudoku[7][7])
            controllaVittoria()
        elif sudoku[7][7]==9:
            sudoku[7][7]=" "
            b77.configure(text=sudoku[7][7])
        else:
            sudoku[7][7]+=1
            b77.configure(text=sudoku[7][7])
            controllaVittoria()
    elif n=="78":
        if sudoku[7][8]==" ":
            sudoku[7][8]=1
            b78.configure(text=sudoku[7][8])
            controllaVittoria()
        elif sudoku[7][8]==9:
            sudoku[7][8]=" "
            b78.configure(text=sudoku[7][8])
        else:
            sudoku[7][8]+=1
            b78.configure(text=sudoku[7][8])
            controllaVittoria()
    elif n=="80":
        if sudoku[8][0]==" ":
            sudoku[8][0]=1
            b80.configure(text=sudoku[8][0])
            controllaVittoria()
        elif sudoku[8][0]==9:
            sudoku[8][0]=" "
            b80.configure(text=sudoku[8][0])
        else:
            sudoku[8][0]+=1
            b80.configure(text=sudoku[8][0])
            controllaVittoria()
    elif n=="81":
        if sudoku[8][1]==" ":
            sudoku[8][1]=1
            b81.configure(text=sudoku[8][1])
            controllaVittoria()
        elif sudoku[8][1]==9:
            sudoku[8][1]=" "
            b81.configure(text=sudoku[8][1])
        else:
            sudoku[8][1]+=1
            b81.configure(text=sudoku[8][1])
            controllaVittoria()
    elif n=="82":
        if sudoku[8][2]==" ":
            sudoku[8][2]=1
            b82.configure(text=sudoku[8][2])
            controllaVittoria()
        elif sudoku[8][2]==9:
            sudoku[8][2]=" "
            b82.configure(text=sudoku[8][2])
        else:
            sudoku[8][2]+=1
            b82.configure(text=sudoku[8][2])
            controllaVittoria()
    elif n=="83":
        if sudoku[8][3]==" ":
            sudoku[8][3]=1
            b83.configure(text=sudoku[8][3])
            controllaVittoria()
        elif sudoku[8][3]==9:
            sudoku[8][3]=" "
            b83.configure(text=sudoku[8][3])
        else:
            sudoku[8][3]+=1
            b83.configure(text=sudoku[8][3])
            controllaVittoria()
    elif n=="84":
        if sudoku[8][4]==" ":
            sudoku[8][4]=1
            b84.configure(text=sudoku[8][4])
            controllaVittoria()
        elif sudoku[8][4]==9:
            sudoku[8][4]=" "
            b84.configure(text=sudoku[8][4])
        else:
            sudoku[8][4]+=1
            b84.configure(text=sudoku[8][4])
            controllaVittoria()
    elif n=="85":
        if sudoku[8][5]==" ":
            sudoku[8][5]=1
            b85.configure(text=sudoku[8][5])
            controllaVittoria()
        elif sudoku[8][5]==9:
            sudoku[8][5]=" "
            b85.configure(text=sudoku[8][5])
        else:
            sudoku[8][5]+=1
            b85.configure(text=sudoku[8][5])
            controllaVittoria()
    elif n=="86":
        if sudoku[8][6]==" ":
            sudoku[8][6]=1
            b86.configure(text=sudoku[8][6])
            controllaVittoria()
        elif sudoku[8][6]==9:
            sudoku[8][6]=" "
            b86.configure(text=sudoku[8][6])
        else:
            sudoku[8][6]+=1
            b86.configure(text=sudoku[8][6])
            controllaVittoria()
    elif n=="87":
        if sudoku[8][7]==" ":
            sudoku[8][7]=1
            b87.configure(text=sudoku[8][7])
            controllaVittoria()
        elif sudoku[8][7]==9:
            sudoku[8][7]=" "
            b87.configure(text=sudoku[8][7])
        else:
            sudoku[8][7]+=1
            b87.configure(text=sudoku[8][7])
            controllaVittoria()
    elif n=="88":
        if sudoku[8][8]==" ":
            sudoku[8][8]=1
            b88.configure(text=sudoku[8][8])
            controllaVittoria()
        elif sudoku[8][8]==9:
            sudoku[8][8]=" "
            b88.configure(text=sudoku[8][8])
        else:
            sudoku[8][8]+=1
            b88.configure(text=sudoku[8][8])
            controllaVittoria()

####################################################### CREAZIONE SUDOKU INIZIALE ################################################################

sudoku=[[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,1,6,4,5,8,9,7],[5,6,4,9,7,8,2,3,1],[8,9,7,3,1,2,5,6,4],[3,1,2,5,6,4,9,7,8],[6,4,5,8,9,7,3,1,2],[9,7,8,2,3,1,6,4,5]]


####################################################### MISCHIA SUDOKU ############################################################################

for i in range(40):
    num1=random.randint(1,9)
    num2=random.randint(1,9)

    for i in range(0,9):
        for e in range(0,9):
            if sudoku[i][e]==num1:
                sudoku[i][e]=num2
            elif sudoku[i][e]==num2:
                sudoku[i][e]=num1

################################################# COPIA SUDOKU E TOLGO CASELLE ###################################################################
sudokuCopy = copy.deepcopy(sudoku)

cont=0
while cont<30:
    for i in range(0,9):
        for e in range(0,9):
            tolgo=random.randint(0,1)
            if tolgo==0 and cont<30 and sudoku[i][e]!=" ":
                sudoku[i][e]=" "
                cont+=1

################################################# DISATTIVO PULSANTI PIENI ######################################################################
def disattivaPulsanti():
    for i in range(0,9):
            for e in range(0,9):
                if sudoku[i][e]!=" ":
                    if i==0 and e==0:
                        b00['state'] = tk.DISABLED
                    elif i==0 and e==1:
                        b01['state'] = tk.DISABLED
                    elif i==0 and e==2:
                        b02['state'] = tk.DISABLED
                    elif i==0 and e==3:
                        b03['state'] = tk.DISABLED
                    elif i==0 and e==4:
                        b04['state'] = tk.DISABLED
                    elif i==0 and e==5:
                        b05['state'] = tk.DISABLED
                    elif i==0 and e==6:
                        b06['state'] = tk.DISABLED
                    elif i==0 and e==7:
                        b07['state'] = tk.DISABLED
                    elif i==0 and e==8:
                        b08['state'] = tk.DISABLED
                    elif i==1 and e==0:
                        b10['state'] = tk.DISABLED
                    elif i==1 and e==1:
                        b11['state'] = tk.DISABLED
                    elif i==1 and e==2:
                        b12['state'] = tk.DISABLED
                    elif i==1 and e==3:
                        b13['state'] = tk.DISABLED
                    elif i==1 and e==4:
                        b14['state'] = tk.DISABLED
                    elif i==1 and e==5:
                        b15['state'] = tk.DISABLED
                    elif i==1 and e==6:
                        b16['state'] = tk.DISABLED
                    elif i==1 and e==7:
                        b17['state'] = tk.DISABLED
                    elif i==1 and e==8:
                        b18['state'] = tk.DISABLED
                    elif i==2 and e==0:
                        b20['state'] = tk.DISABLED
                    elif i==2 and e==1:
                        b21['state'] = tk.DISABLED
                    elif i==2 and e==2:
                        b22['state'] = tk.DISABLED
                    elif i==2 and e==3:
                        b23['state'] = tk.DISABLED
                    elif i==2 and e==4:
                        b24['state'] = tk.DISABLED
                    elif i==2 and e==5:
                        b25['state'] = tk.DISABLED
                    elif i==2 and e==6:
                        b26['state'] = tk.DISABLED
                    elif i==2 and e==7:
                        b27['state'] = tk.DISABLED
                    elif i==2 and e==8:
                        b28['state'] = tk.DISABLED 
                    elif i==3 and e==0:
                        b30['state'] = tk.DISABLED
                    elif i==3 and e==1:
                        b31['state'] = tk.DISABLED
                    elif i==3 and e==2:
                        b32['state'] = tk.DISABLED
                    elif i==3 and e==3:
                        b33['state'] = tk.DISABLED
                    elif i==3 and e==4:
                        b34['state'] = tk.DISABLED
                    elif i==3 and e==5:
                        b35['state'] = tk.DISABLED
                    elif i==3 and e==6:
                        b36['state'] = tk.DISABLED
                    elif i==3 and e==7:
                        b37['state'] = tk.DISABLED
                    elif i==3 and e==8:
                        b38['state'] = tk.DISABLED 
                    elif i==4 and e==0:
                        b40['state'] = tk.DISABLED
                    elif i==4 and e==1:
                        b41['state'] = tk.DISABLED
                    elif i==4 and e==2:
                        b42['state'] = tk.DISABLED
                    elif i==4 and e==3:
                        b43['state'] = tk.DISABLED
                    elif i==4 and e==4:
                        b44['state'] = tk.DISABLED
                    elif i==4 and e==5:
                        b45['state'] = tk.DISABLED
                    elif i==4 and e==6:
                        b46['state'] = tk.DISABLED
                    elif i==4 and e==7:
                        b47['state'] = tk.DISABLED
                    elif i==4 and e==8:
                        b48['state'] = tk.DISABLED 
                    elif i==5 and e==0:
                        b50['state'] = tk.DISABLED
                    elif i==5 and e==1:
                        b51['state'] = tk.DISABLED
                    elif i==5 and e==2:
                        b52['state'] = tk.DISABLED
                    elif i==5 and e==3:
                        b53['state'] = tk.DISABLED
                    elif i==5 and e==4:
                        b54['state'] = tk.DISABLED
                    elif i==5 and e==5:
                        b55['state'] = tk.DISABLED
                    elif i==5 and e==6:
                        b56['state'] = tk.DISABLED
                    elif i==5 and e==7:
                        b57['state'] = tk.DISABLED
                    elif i==5 and e==8:
                        b58['state'] = tk.DISABLED 
                    elif i==6 and e==0:
                        b60['state'] = tk.DISABLED
                    elif i==6 and e==1:
                        b61['state'] = tk.DISABLED
                    elif i==6 and e==2:
                        b62['state'] = tk.DISABLED
                    elif i==6 and e==3:
                        b63['state'] = tk.DISABLED
                    elif i==6 and e==4:
                        b64['state'] = tk.DISABLED
                    elif i==6 and e==5:
                        b65['state'] = tk.DISABLED
                    elif i==6 and e==6:
                        b66['state'] = tk.DISABLED
                    elif i==6 and e==7:
                        b67['state'] = tk.DISABLED
                    elif i==6 and e==8:
                        b68['state'] = tk.DISABLED 
                    elif i==7 and e==0:
                        b70['state'] = tk.DISABLED
                    elif i==7 and e==1:
                        b71['state'] = tk.DISABLED
                    elif i==7 and e==2:
                        b72['state'] = tk.DISABLED
                    elif i==7 and e==3:
                        b73['state'] = tk.DISABLED
                    elif i==7 and e==4:
                        b74['state'] = tk.DISABLED
                    elif i==7 and e==5:
                        b75['state'] = tk.DISABLED
                    elif i==7 and e==6:
                        b76['state'] = tk.DISABLED
                    elif i==7 and e==7:
                        b77['state'] = tk.DISABLED
                    elif i==7 and e==8:
                        b78['state'] = tk.DISABLED 
                    elif i==8 and e==0:
                        b80['state'] = tk.DISABLED
                    elif i==8 and e==1:
                        b81['state'] = tk.DISABLED
                    elif i==8 and e==2:
                        b82['state'] = tk.DISABLED
                    elif i==8 and e==3:
                        b83['state'] = tk.DISABLED
                    elif i==8 and e==4:
                        b84['state'] = tk.DISABLED
                    elif i==8 and e==5:
                        b85['state'] = tk.DISABLED
                    elif i==8 and e==6:
                        b86['state'] = tk.DISABLED
                    elif i==8 and e==7:
                        b87['state'] = tk.DISABLED
                    elif i==8 and e==8:
                        b88['state'] = tk.DISABLED

#################################################### CONTROLLA VITTORIA ########################################################################

def controllaVittoria():
    if sudokuCopy==sudoku:
        messagebox.showinfo("HAI VINTO")



####################################################### CREAZIONE FINESTRA E BOTTONI #############################################################
win=tk.Tk()
win.title("SUDOKU ROSARIO")
for i in sudokuCopy:
    print(i)
b00=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][0]), command=lambda : inserisci("00"))
b00.grid(column=0, row=0)
b01=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][1]), command=lambda : inserisci("01"))
b01.grid(column=1, row=0)
b02=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][2]), command=lambda : inserisci("02"))
b02.grid(column=2, row=0)
b03=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][3]), command=lambda : inserisci("03"))
b03.grid(column=3, row=0)
b04=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][4]), command=lambda : inserisci("04"))
b04.grid(column=4, row=0)
b05=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][5]), command=lambda : inserisci("05"))
b05.grid(column=5, row=0)
b06=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][6]), command=lambda : inserisci("06"))
b06.grid(column=6, row=0)
b07=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][7]), command=lambda : inserisci("07"))
b07.grid(column=7, row=0)
b08=tk.Button(win, height = 3, width = 6, text=str(sudoku[0][8]), command=lambda : inserisci("08"))
b08.grid(column=8, row=0)
b10=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][0]), command=lambda : inserisci("10"))
b10.grid(column=0, row=1)
b11=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][1]), command=lambda : inserisci("11"))
b11.grid(column=1, row=1)
b12=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][2]), command=lambda : inserisci("12"))
b12.grid(column=2, row=1)
b13=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][3]), command=lambda : inserisci("13"))
b13.grid(column=3, row=1)
b14=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][4]), command=lambda : inserisci("14"))
b14.grid(column=4, row=1)
b15=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][5]), command=lambda : inserisci("15"))
b15.grid(column=5, row=1)
b16=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][6]), command=lambda : inserisci("16"))
b16.grid(column=6, row=1)
b17=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][7]), command=lambda : inserisci("17"))
b17.grid(column=7, row=1)
b18=tk.Button(win, height = 3, width = 6, text=str(sudoku[1][8]), command=lambda : inserisci("18"))
b18.grid(column=8, row=1)
b20=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][0]), command=lambda : inserisci("20"))
b20.grid(column=0, row=2)
b21=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][1]), command=lambda : inserisci("21"))
b21.grid(column=1, row=2)
b22=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][2]), command=lambda : inserisci("22"))
b22.grid(column=2, row=2)
b23=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][3]), command=lambda : inserisci("23"))
b23.grid(column=3, row=2)
b24=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][4]), command=lambda : inserisci("24"))
b24.grid(column=4, row=2)
b25=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][5]), command=lambda : inserisci("25"))
b25.grid(column=5, row=2)
b26=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][6]), command=lambda : inserisci("26"))
b26.grid(column=6, row=2)
b27=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][7]), command=lambda : inserisci("27"))
b27.grid(column=7, row=2)
b28=tk.Button(win, height = 3, width = 6, text=str(sudoku[2][8]), command=lambda : inserisci("28"))
b28.grid(column=8, row=2)
b30=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][0]), command=lambda : inserisci("30"))
b30.grid(column=0, row=3)
b31=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][1]), command=lambda : inserisci("31"))
b31.grid(column=1, row=3)
b32=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][2]), command=lambda : inserisci("32"))
b32.grid(column=2, row=3)
b33=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][3]), command=lambda : inserisci("33"))
b33.grid(column=3, row=3)
b34=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][4]), command=lambda : inserisci("34"))
b34.grid(column=4, row=3)
b35=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][5]), command=lambda : inserisci("35"))
b35.grid(column=5, row=3)
b36=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][6]), command=lambda : inserisci("36"))
b36.grid(column=6, row=3)
b37=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][7]), command=lambda : inserisci("37"))
b37.grid(column=7, row=3)
b38=tk.Button(win, height = 3, width = 6, text=str(sudoku[3][8]), command=lambda : inserisci("38"))
b38.grid(column=8, row=3)
b40=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][0]), command=lambda : inserisci("40"))
b40.grid(column=0, row=4)
b41=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][1]), command=lambda : inserisci("41"))
b41.grid(column=1, row=4)
b42=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][2]), command=lambda : inserisci("42"))
b42.grid(column=2, row=4)
b43=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][3]), command=lambda : inserisci("43"))
b43.grid(column=3, row=4)
b44=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][4]), command=lambda : inserisci("44"))
b44.grid(column=4, row=4)
b45=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][5]), command=lambda : inserisci("45"))
b45.grid(column=5, row=4)
b46=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][6]), command=lambda : inserisci("46"))
b46.grid(column=6, row=4)
b47=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][7]), command=lambda : inserisci("47"))
b47.grid(column=7, row=4)
b48=tk.Button(win, height = 3, width = 6, text=str(sudoku[4][8]), command=lambda : inserisci("48"))
b48.grid(column=8, row=4)
b50=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][0]), command=lambda : inserisci("50"))
b50.grid(column=0, row=5)
b51=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][1]), command=lambda : inserisci("51"))
b51.grid(column=1, row=5)
b52=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][2]), command=lambda : inserisci("52"))
b52.grid(column=2, row=5)
b53=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][3]), command=lambda : inserisci("53"))
b53.grid(column=3, row=5)
b54=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][4]), command=lambda : inserisci("54"))
b54.grid(column=4, row=5)
b55=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][5]), command=lambda : inserisci("55"))
b55.grid(column=5, row=5)
b56=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][6]), command=lambda : inserisci("56"))
b56.grid(column=6, row=5)
b57=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][7]), command=lambda : inserisci("57"))
b57.grid(column=7, row=5)
b58=tk.Button(win, height = 3, width = 6, text=str(sudoku[5][8]), command=lambda : inserisci("58"))
b58.grid(column=8, row=5)
b60=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][0]), command=lambda : inserisci("60"))
b60.grid(column=0, row=6)
b61=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][1]), command=lambda : inserisci("61"))
b61.grid(column=1, row=6)
b62=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][2]), command=lambda : inserisci("62"))
b62.grid(column=2, row=6)
b63=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][3]), command=lambda : inserisci("63"))
b63.grid(column=3, row=6)
b64=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][4]), command=lambda : inserisci("64"))
b64.grid(column=4, row=6)
b65=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][5]), command=lambda : inserisci("65"))
b65.grid(column=5, row=6)
b66=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][6]), command=lambda : inserisci("66"))
b66.grid(column=6, row=6)
b67=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][7]), command=lambda : inserisci("67"))
b67.grid(column=7, row=6)
b68=tk.Button(win, height = 3, width = 6, text=str(sudoku[6][8]), command=lambda : inserisci("68"))
b68.grid(column=8, row=6)
b70=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][0]), command=lambda : inserisci("70"))
b70.grid(column=0, row=7)
b71=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][1]), command=lambda : inserisci("71"))
b71.grid(column=1, row=7)
b72=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][2]), command=lambda : inserisci("72"))
b72.grid(column=2, row=7)
b73=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][3]), command=lambda : inserisci("73"))
b73.grid(column=3, row=7)
b74=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][4]), command=lambda : inserisci("74"))
b74.grid(column=4, row=7)
b75=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][5]), command=lambda : inserisci("75"))
b75.grid(column=5, row=7)
b76=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][6]), command=lambda : inserisci("76"))
b76.grid(column=6, row=7)
b77=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][7]), command=lambda : inserisci("77"))
b77.grid(column=7, row=7)
b78=tk.Button(win, height = 3, width = 6, text=str(sudoku[7][8]), command=lambda : inserisci("78"))
b78.grid(column=8, row=7)
b80=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][0]), command=lambda : inserisci("80"))
b80.grid(column=0, row=8)
b81=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][1]), command=lambda : inserisci("81"))
b81.grid(column=1, row=8)
b82=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][2]), command=lambda : inserisci("82"))
b82.grid(column=2, row=8)
b83=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][3]), command=lambda : inserisci("83"))
b83.grid(column=3, row=8)
b84=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][4]), command=lambda : inserisci("84"))
b84.grid(column=4, row=8)
b85=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][5]), command=lambda : inserisci("85"))
b85.grid(column=5, row=8)
b86=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][6]), command=lambda : inserisci("86"))
b86.grid(column=6, row=8)
b87=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][7]), command=lambda : inserisci("87"))
b87.grid(column=7, row=8)
b88=tk.Button(win, height = 3, width = 6, text=str(sudoku[8][8]), command=lambda : inserisci("88"))
b88.grid(column=8, row=8)
disattivaPulsanti()


win.mainloop()