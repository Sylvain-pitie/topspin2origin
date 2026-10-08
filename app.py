from tkinter import * 
from tkinter.filedialog import *
from tkinter.scrolledtext import *
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import math as m
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
# creer une premier fenetre
global filepath
filepath = 'None'
master = Tk()

# personnaliser cette fenetre
master.title("topspin2origin")
master.geometry("1180x820")
master.minsize(480,360)
img = PhotoImage(file='logo.png')
master.tk.call('wm', 'iconphoto', master._w, img)
master.config(background='skyblue')
#creer la frame
frame1 = Frame(master, bg='white', width=1080, height=820)
#creer progressbar
pb = Progressbar(frame1,orient='horizontal',mode='determinate',length=1000)
pb.pack(side='bottom',pady = 10, fill=X) 

# ajouter un premier texte
label_title = Label(frame1, text="Bienvenue sur Topspin2Origin", font=("Courrier",40), bg='white', fg='black')
label_title.pack(side='top', padx=10,pady=5,expand=True)
# ajouter un second texte
label_subtitle = Label(frame1, text="Choisir le fichier .txt à convertir", font=("Courrier",25), bg='white', fg='black')
label_subtitle.pack(side='top', padx=10,pady=5,expand=True)


#ajouter la frame
frame1.pack(side='left', fill='both', padx=10, pady=5,expand=YES)
#ajouter une ouverture de fichier
def fileopen_txt () :
    filepath= askopenfilename(title="Ouvrir un fichier txt", filetypes=[('txt file','.txt'),('all files','.*')])
    fichier = open(filepath, "r")
    content = fichier.read()
    fichier.close()
    #creer la fenetre xyz
    xyzframe = Tk()
    v = Scrollbar(xyzframe) 
    v.pack(side=RIGHT, fill=Y)
    h = Scrollbar(xyzframe, orient= HORIZONTAL)
    h.pack(side=BOTTOM, fill=X)
    editArea = Text(xyzframe, width=60, height=40, wrap=WORD, xscrollcommand=h.set, yscrollcommand=v.set)
    editArea.pack()
    v.config(command=editArea.yview)
    h.config(command=editArea.xview)
    editArea.place(x=10,y=10)
    #personalisation
    xyzframe.title("TXT file ")
    xyzframe.geometry("460x460")
    xyzframe.minsize(360,360)
    xyzframe.config(background='white')                               
    #Label(xyzframe, text=content, font=("Courrier",8), bg='white', fg='black').pack(padx=10, pady=10)
    editArea.insert(INSERT, content)
    xyzframe.mainloop()
#ajouter un convertir un fichier txt en dat
def convertor():
    filepath= askopenfilename(title="Ouvrir un fichier txt", filetypes=[('txt file','.txt'),('all files','.*')])
    geometry = open(filepath, "r")
    pb['value'] = 0
    frame1.update_idletasks()
    ppmwindows = geometry.readlines()[3]
    geometry.close
    geometry = open(filepath, "r")
    stepligne = geometry.readlines()[5]
    geometry.close
    res = ppmwindows.split()
    beginspec = float(res[3])
    endspec = float(res[7])
    res = stepligne.split()
    step = int(res[3])
    allppm = endspec-beginspec
    ppmstep= allppm/step
    step25 = int(step*0.25)
    step50 = int(step*0.5)
    step75 = int(step*0.75)
#    print(step25)
    geometry = open(filepath, "r")
    lignes = geometry.readlines()[10:]
    geometry.close
    tab=[]
    yppm=[]
    for chn in lignes:
        tab.append(chn.split())
        for lst in tab:
            lst[0] = float(lst[0])
            if lst == tab[-1]:
                yppm.append(lst[0])
    xppm=[None]*step
    for i in range(step):
        if i < 1:
            xppm[i] = beginspec
        else:
           xppm[i] = xppm[i-1] + ppmstep
        if yppm[i] < 0:
            yppm[i] = 0.
        if i == step25:
            pb['value'] = 25
            frame1.update_idletasks()
        elif i == step50:
            pb['value'] = 50
            frame1.update_idletasks()
        elif i == step75:
            pb['value'] = 75
            frame1.update_idletasks()
    output = filepath.split('.')
    fileout = str(output[0])+'.dat'
    fichier =open(fileout, "w")
    for i in range(step):
        x = xppm[i]
        y = yppm[i]
        fichier.write(f"{x:5.6f}   {y:5.6f}\n")
    fichier.close()
    pb['value'] = 100
    frame1.update_idletasks()

#ajouter une barre de menu
menu_bar = Menu(master)

#creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Ouvrir", command=fileopen_txt)
file_menu.add_command(label="Convertir", command=convertor)
file_menu.add_command(label="Quitter", command=master.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#ajouter un premier bouton
fichier_button = Button(frame1, text="Convertir fichier", font=("Courrier", 25), bg='gray', fg="black", command=convertor)
fichier_button.pack(pady=25, fill=X)

#configurer notre fenetre pour ajouter cette menu bar
master.config(menu=menu_bar)
# afficher la fenetre master
master.mainloop()
