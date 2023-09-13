# This code is made by: Arnau Azogue Fabre - Azogue99
# This code is NOT FOR SALE
# The property of this code is from "UPC - AICHE - CHEM E CAR" and future teams 
# With the only purpouse of participating to CHEM-E-CAR competition

import tkinter as tk
from tkinter import *
import os
from os import listdir
import math


this_folder = os.path.dirname(os.path.abspath(__file__)) #use relative paths to the folder container and line below to call specifict files in the folder
#os.path.join(this_folder, 'Resources\Files')



###########################
### VARIABLES DE FORMAT ###
###########################

decimals = 4         #important! nombre de decimals

AutoExecute = True      #carregar la informacio i executar els botons automaticament al iniciar el programa

#titols

titol_finestra = 'UPC | Chem-E-Car'    #titol de la finestra
titol_app = 'UPC-AICHE | CHEM E CAR'    #titol de la finestra
titol_pila = 'PILA'
titol_mru = 'MRU'
titol_iodine = 'IODINE'

#format visual

bg_ = 'grey6' #color de fons
bg_entry ='#2e2e2e' #color dels entry
fg_ = '#ffa500' #color de lletra, buscar a google "tkinter colors" o la web http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
color_d_accent = '#00bfff' #otros colores #6A6B0B, #00bfff

tipus_lletra = 'Arial Bold' #fonts de windos i styles com (normal, bold, italic, underline and overstrike) https://effbot.org/tkinterbook/tkinter-widget-styling.htm
mida_lletra = 16
estil_ = 'normal'

cursor_ = '' #puntero del mouse default = '', sino: (crosshair, tcross, dot, diamond_cross, spider, pirate, target, right_ptr, X_cursor, ...)

relief_entry_ = 'flat' #relleu entrades
relief_buttons_ = 'flat' #relleu botons
activebackground_ = 'gold2' #color dels botons al ser polsats
bd_ = 0 #border with

marcs = 2
amplada_label = 22
amplada_entry = 10
amplada_button = 12
amplada_respostes = 7
amplada_unitats = 12
height_= 0

anchor_ = 'e' #posició dels enunciats (n, s, e, w)
anchor_unitats = 'w'



#################################
### FINAL VARIABLES DE FORMAT ###
#################################

### MAIN WINDOW ###

#columnes
pos_label = 1
pos_entry = 2
pos_button = 3
pos_respostes = 4
pos_unitats = 5

total_columnes = max(pos_label, pos_entry, pos_button, pos_respostes, pos_unitats)


#files
pos_titol = 0
pos_pila = 1 * 10
pos_mru = 2 * 10
pos_iodine = 3 * 10

total_files = max(pos_titol, pos_pila, pos_mru, pos_iodine)

#con el AutoExecute off
compost_ = '-'
ml_dissolucio_ = 0
molaritat_ = 0
densitat_solut_ = 0
percentatge_ = 0

espai_ = 0
velocitat_ = 0

temps_iodine_ = 0
ml_iodine_ = 0
temperatura_ = 0

#con el AutoExecute on
if AutoExecute:
    compost_ = 'H2SO4'       #preestablerts
    ml_dissolucio_ = 300
    molaritat_ = 3
    densitat_solut_ = 1.83
    percentatge_ = 98

    espai_ = 15
    velocitat_ = 0.2
    
    temps_iodine_ = 60+30
    ml_iodine_ = 250
    temperatura_ = 25





font_ = (tipus_lletra, mida_lletra, estil_)




####################################################################################################

my_window = tk.Tk()
my_window.title(titol_finestra)
try:
    my_window.iconbitmap(os.path.join(this_folder, r'Resources\Pictures\upc.ico'))
except:
    pass

my_window.configure(background=bg_, borderwidth=marcs, cursor=cursor_)

#fes la finestra responisve
n_rows = total_files +1
n_columns = total_columnes +1
for i in range(n_rows):
    my_window.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    my_window.grid_columnconfigure(i,  weight =1)


#########################
## Funcions principals ##
#########################

def descompon_en_atoms(s):              ### Fes una llista amb els atoms de l'element
    llista = list(s)
    for i in range(len(llista)):
        if i == 0:
            pass
        elif llista[i].isupper():
            llista[i] = '$'+llista[i]
    nova_string = ''.join(llista)
    lis = nova_string.split('$')
    atoms_dic = {}
    for atoms in lis:
        atoms = list(atoms)
        number = 1
        memory = []
        for item in atoms:
            if item.isdigit():
                memory.append(item)
        for item in memory:
            atoms.remove(item)
        if len(memory) != 0:
            number = int(''.join(memory))
        if ''.join(atoms) in atoms_dic:
            atoms_dic[''.join(atoms)] = number + atoms_dic[''.join(atoms)]
        else:
            atoms_dic[''.join(atoms)] = number
    llistat = []
    for x, y in atoms_dic.items():
        for i in range(y):
            llistat.append(x)
    return llistat


def massa_atomica(llista_atoms):                ### Retorna la massa atomica sumada d'una llista d'atoms
    tabla = {'H': 1.00784,
             'He': 4.0026, 
             'Li': 6.941, 
             'Be': 9.0122, 
             'B': 10.811, 
             'C': 12.0107, 
             'N': 14.0067, 
             'O': 15.999, 
             'F': 18.9984, 
             'Ne': 20.1797, 
             'Na': 22.9897, 
             'Mg': 24.305, 
             'Al': 26.9815, 
             'Si': 28.0855, 
             'P': 30.9738, 
             'S': 32.065, 
             'Cl': 35.453, 
             'K': 39.0983, 
             'Ar': 39.948, 
             'Ca': 40.078, 
             'Sc': 44.9559, 
             'Ti': 47.867, 
             'V': 50.9415, 
             'Cr': 51.9961, 
             'Mn': 54.938, 
             'Fe': 55.845, 
             'Ni': 58.6934, 
             'Co': 58.9332, 
             'Cu': 63.546, 
             'Zn': 65.39, 
             'Ga': 69.723, 
             'Ge': 72.64, 
             'As': 74.9216, 
             'Se': 78.96, 
             'Br': 79.904, 
             'Kr': 83.8,
             'Rb': 85.4678,
             'Sr': 87.62,
             'Y': 88.9059,
             'Zr': 91.224,
             'Nb': 92.9064,
             'Mo': 95.94,
             'Tc': 98,
             'Ru': 101.07,
             'Rh': 102.9055,
             'Pd': 106.42,
             'Ag': 107.8682,
             'Cd': 112.411,
             'In': 114.818,
             'Sn': 118.71,
             'Sb': 121.76,
             'I': 126.9045,
             'Te': 127.6,
             'Xe': 131.293,
             'Cs': 132.9055,
             'Ba': 137.327,
             'La': 138.9055,
             'Ce': 140.116,
             'Pr': 140.9077,
             'Nd': 144.24,
             'Pe': 145,
             'Sm': 150.36,
             'Eu': 151.964,
             'Gd': 157.25,
             'Tb': 158.9253,
             'Dy': 162.5,
             'Ho': 164.9303,
             'Er': 167.259,
             'Tm': 168.9342,
             'Yb': 173.04,
             'Lu': 174.967,
             'Hf': 178.49,
             'Ta': 180.9479,
             'W': 183.84,
             'Re': 186.207,
             'Os': 190.23,
             'Ir': 192.217,
             'Pt': 195.078,
             'Au': 196.9665,
             'Hg': 200.59,
             'Tl': 204.3833,
             'Pb': 207.2,
             'Bi': 208.9804,
             'Po': 209,
             'At': 210,
             'Rn': 222,
             'Fr': 223,
             'Ra': 226,
             'Ac': 227,
             'Pa': 231.0359,
             'Th': 232.0381,
             'Np': 237,
             'U': 238.0289,
             'Am': 243,
             'Pu': 244,
             'Cm': 247,
             'Bk': 227,
             'Cf': 251,
             'Es': 252,
             'Fm': 257,
             'Mv': 258,
             'No': 259,
             'Rf': 261,
             'Lr': 227,
             'Db': 262,
             'Bh': 264,
             'Sg': 266,
             'Mt': 268,
             'Hs': 277,
             'Ds': 281,
             'Uuu': 272,
             'Cn': 285, 'Uub': 285,     #nomenclatura nova + antiga
             'Nh': 286, 'Uut': 286,     #nomenclatura nova + antiga
             'Fl': 289, 'Uuq': 289,     #nomenclatura nova + antiga
             'Mc': 288, 'Uup': 288,     #nomenclatura nova + antiga
             'Lv': 292, 'Uuh': 292,     #nomenclatura nova + antiga
             'Ts': 292.2076, 'Uus': 292.2076,     #nomenclatura nova + antiga
             'Og': 294, 'Uuo': 294     #nomenclatura nova + antiga
             }
    
    sumatori = 0
    for i in llista_atoms:
        sumatori += tabla[i]
    return sumatori


def massa_molecula(s):                  ### torna la massa total d'un compost (funcio de funcions)
    return(massa_atomica(descompon_en_atoms(str(s))))


def ml_solut_necessaris(ml_diss, massa_atomica, molaritat, dens_solut, percent):    ### Calcula els mililitres de solut necessaris
    p = percent/100
    d = dens_solut/0.001

    v0 = ml_diss / 1000     #litres
    c0 = molaritat
    c1 = (d*p)/massa_atomica
    
    v1 = (c0*v0)/c1     #de la formula: v1*c1 = c0*v0

    resposta_en_ml = v1*1000       #mililitres

    #idees: resposta = ((molaritat*(ml_diss/1000))/((dens_solut/0.001)*(percent/100))/massa_atomica))*1000

    return resposta_en_ml


def taules_csv():
    ruta = os.path.join(this_folder, 'Resources\Files')

    tipus = '.csv'
    arxius = []
    for item in listdir(ruta):
        if item.endswith(tipus):
            f = open(os.path.join(ruta, item), "r")#cal canviar a opencsv i a partir de aqui treballar amb arxius
            print(f.readline())





############################
### UPC AICHE CHEM E CAR ###
############################

linea1 = tk.Label(my_window, text = ' ', bg=bg_, fg=color_d_accent, font=font_)
linea1.grid(row=pos_titol+1, column=pos_label, columnspan=5)

titol = tk.Label(my_window, text = titol_app, bg=bg_, fg=color_d_accent, font=(tipus_lletra, 24, 'bold'))
titol.grid(row=pos_titol+2, column=pos_label, columnspan=5)

linea2 = tk.Label(my_window, text = ' ', bg=bg_, fg=color_d_accent, font=font_)
linea2.grid(row=pos_titol+3, column=pos_label, columnspan=5)



#mirar moduls PIL, Image i ImageTK
#img = tk.PhotoImage(r'C:\Users\Azogue\Desktop\Arnau\ChemECar\ChemECar App\Resources\Pictures\upc.png')
#label_img = tk.Label(my_window, image = img)
#label_img.place(x = 0, y = 0)



############
### PILA ###
############


            ### TITOL ###

label_quimica = tk.Label(my_window, text = titol_pila, bg=bg_, fg=color_d_accent, font=font_)
label_quimica.grid(row=pos_pila, column=pos_label, columnspan=2)


            ### LABEL ###

### Solut
label_compost = tk.Label(my_window, text = 'Solut (Formula): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_compost.grid(row=pos_pila+1, column=pos_label)


### ml_dissolucio
label_ml_dissolucio = tk.Label(my_window, text = 'Dissolucio a preparar (ml): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_ml_dissolucio.grid(row=pos_pila+2, column=pos_label)


### Molaritat (Mols Solut)/(L dissolucio)
label_molaritat = tk.Label(my_window, text = 'Molaritat: ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_molaritat.grid(row=pos_pila+3, column=pos_label)


### densitat
label_densitat_solut = tk.Label(my_window, text = 'Densitat del Solut (g/ml): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_densitat_solut.grid(row=pos_pila+4, column=pos_label)


### percentatge
label_percentatge = tk.Label(my_window, text = 'Percentatge del Solut (%): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_percentatge.grid(row=pos_pila+5, column=pos_label)


### respostes ( no estaran en la columna dels labels, sino dels bottons )
label_percentatge = tk.Label(my_window, text = 'Solut: ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_button)
label_percentatge.grid(row=pos_pila+4, column=pos_button)
label_percentatge = tk.Label(my_window, text = 'Dissolvent: ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_button)
label_percentatge.grid(row=pos_pila+5, column=pos_button)


            ### ENTRY ###

### Solut
compost = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
compost.grid(row=pos_pila+1, column=pos_entry, sticky='nesw')
compost.insert(INSERT, compost_)

### ml_dissolucio
ml_dissolucio = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
ml_dissolucio.grid(row=pos_pila+2, column=pos_entry, sticky='nesw')
ml_dissolucio.insert(INSERT, ml_dissolucio_)

### Molaritat (Mols Solut)/(L dissolucio)
molaritat = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
molaritat.grid(row=pos_pila+3, column=pos_entry, sticky='nesw')
molaritat.insert(INSERT, molaritat_)

### densitat
densitat_solut = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
densitat_solut.grid(row=pos_pila+4, column=pos_entry, sticky='nesw')
densitat_solut.insert(INSERT, densitat_solut_)

### percentatge
percentatge = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
percentatge.grid(row=pos_pila+5, column=pos_entry, sticky='nesw')
percentatge.insert(INSERT, percentatge_)




            ### BUTTON ###

### Button masa atomica
def func_button_massa_molecula():
    global pos_pila
    row_ = pos_pila+1
    
    comp = compost.get()
    massa_mol = massa_molecula(comp)
    
    global decimals
    label_massa_atomica = tk.Label(my_window, text = '                   ', bg=bg_, fg=fg_, font=font_, width=amplada_respostes)           #esborra la resposta anterior
    label_massa_atomica.grid(row=row_, column=pos_respostes)
    
    label_massa_atomica = tk.Label(my_window, text = (round(massa_mol, decimals)), bg=bg_, fg=fg_, font=font_, width=amplada_respostes)
    label_massa_atomica.grid(row=row_, column=pos_respostes)

    label_massa_atomica_unitats = tk.Label(my_window, text = ('g/mol'), bg=bg_, fg=fg_, font=font_, width=amplada_unitats, anchor_ = anchor_unitats)
    label_massa_atomica_unitats.grid(row=row_, column=pos_unitats)
    

button_massa_atomica = tk.Button(my_window, text = 'Massa Atomica', command = func_button_massa_molecula, bg=fg_, fg=bg_, font=font_, relief=relief_buttons_, activebackground=activebackground_, bd=0)
button_massa_atomica.grid(row=pos_pila+1, column=pos_button, sticky='nesw')


### Button Calcula Pila
def func_button_calcula_pila():
    global pos_pila
    global decimals
    row_ = pos_pila+4
    
    ml_diss = float(ml_dissolucio.get())
    comp = compost.get()
    massa_atomica = float(massa_molecula(comp))
    M = float(molaritat.get())
    densitat = float(densitat_solut.get())
    percent = float(percentatge.get())

    error_a_la_divisio = bool(M == 0 or densitat == 0 or percent == 0)

    if error_a_la_divisio:
        resposta_solut = 'Error en divisió: ZERO'
        resposta_dissolvent = 'Error en divisió: ZERO'
    
    else:
        resposta_solut = (round(ml_solut_necessaris(ml_diss, massa_atomica, M, densitat, percent), decimals))
        resposta_dissolvent = (round(ml_diss - ml_solut_necessaris(ml_diss, massa_atomica, M, densitat, percent), decimals))
    

    
    label_solut = tk.Label(my_window, text = '                        ', bg=bg_, fg=fg_, font=font_, width=amplada_respostes)           #esborra la resposta anterior
    label_solut.grid(row=row_, column=pos_respostes)

    massa_atomica = tk.Label(my_window, text = '                        ', bg=bg_, fg=fg_, font=font_, width=amplada_respostes)           #esborra la resposta anterior
    massa_atomica.grid(row=row_+1, column=pos_respostes)

    massa_atomica = tk.Label(my_window, text = resposta_solut, bg=bg_, fg=fg_, font=font_, width=amplada_respostes)
    massa_atomica.grid(row=row_, column=pos_respostes)
    
    massa_atomica = tk.Label(my_window, text = resposta_dissolvent, bg=bg_, fg=fg_, font=font_, width=amplada_respostes)
    massa_atomica.grid(row=row_+1, column=pos_respostes)

    label_unitats = tk.Label(my_window, text = ('ml'), bg=bg_, fg=fg_, font=font_, width=amplada_unitats, anchor_ = anchor_unitats)
    label_unitats.grid(row=row_, column=pos_unitats)

    label_unitats = tk.Label(my_window, text = ('ml'), bg=bg_, fg=fg_, font=font_, width=amplada_unitats, anchor_ = anchor_unitats)
    label_unitats.grid(row=row_+1, column=pos_unitats)

button_calcula_pila = tk.Button(my_window, text = 'Calcula', command = func_button_calcula_pila, bg=fg_, fg=bg_, font=font_, width=amplada_button, relief=relief_buttons_, activebackground=activebackground_, bd=0)
button_calcula_pila.grid(row=pos_pila+3, column=pos_button, sticky='nesw')














##############
### IODINE ###          #s'ha de fer
##############

            ### TITOL ###

linea3 = tk.Label(my_window, text = ' ', bg=bg_, fg=color_d_accent, font=font_)
linea3.grid(row=pos_iodine, column=pos_label, columnspan=4)

label_iodine = tk.Label(my_window, text = titol_iodine, bg=bg_, fg=color_d_accent, font=font_)
label_iodine.grid(row=pos_iodine+1, column=pos_label, columnspan=2)


            ### LABEL ###

### Temps
label_temps_iodine = tk.Label(my_window, text = 'Temps (s): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_temps_iodine.grid(row=pos_iodine+2, column=pos_label)

### Temperatura
label_temperatura = tk.Label(my_window, text = 'Temperatura (ºC): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_temperatura.grid(row=pos_iodine+3, column=pos_label)

### ml
label_ml_iodine = tk.Label(my_window, text = 'Dissolucio a preparar (ml): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_ml_iodine.grid(row=pos_iodine+4, column=pos_label)








            ### ENTRY ###

### Temps
temps_iodine = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
temps_iodine.grid(row=pos_iodine+2, column=pos_entry, sticky='nesw')
temps_iodine.insert(INSERT, temps_iodine_)

### Temperatura
temperatura = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
temperatura.grid(row=pos_iodine+3, column=pos_entry, sticky='nesw')
temperatura.insert(INSERT, temperatura_)

### pH
ml_iodine = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
ml_iodine.grid(row=pos_iodine+4, column=pos_entry, sticky='nesw')
ml_iodine.insert(INSERT, ml_iodine_)





            ### BUTTON ###


### Button masa atomica
def button_calcula_iodine():
    global pos_iodine
    row_ = pos_iodine+2
    
    
    
    global decimals
    KIO3 = tk.Label(my_window, text = (round(214.0, decimals)), bg=bg_, fg=fg_, font=font_, width=amplada_respostes)
    KIO3.grid(row=row_, column=pos_respostes)
    label_unitats = tk.Label(my_window, text = ('KIO3', 'g/mol'), bg=bg_, fg=fg_, font=font_, width=amplada_unitats, anchor_ = anchor_unitats)
    label_unitats.grid(row=row_, column=pos_unitats)
    
    NaHSO3 = tk.Label(my_window, text = (round(103.90, decimals)), bg=bg_, fg=fg_, font=font_, width=amplada_respostes)
    NaHSO3.grid(row=row_+1, column=pos_respostes)
    label_unitats = tk.Label(my_window, text = ('NaHSO3', 'g/mol'), bg=bg_, fg=fg_, font=font_, width=amplada_unitats, anchor_ = anchor_unitats)
    label_unitats.grid(row=row_+1, column=pos_unitats)
    
    H2SO4 = tk.Label(my_window, text = (round(98.0, decimals)), bg=bg_, fg=fg_, font=font_, width=amplada_respostes)
    H2SO4.grid(row=row_+2, column=pos_respostes)
    label_unitats = tk.Label(my_window, text = ('H2SO4', 'g/mol'), bg=bg_, fg=fg_, font=font_, width=amplada_unitats, anchor_ = anchor_unitats)
    label_unitats.grid(row=row_+2, column=pos_unitats)

    #math.exp((124.17-temps)/74.43)
    relacio = math.exp((124.17-float(temps_iodine.get()))/74.43)
    mido = tk.Label(my_window, text = (round(relacio, decimals)), bg=bg_, fg=fg_, font=font_, width=amplada_respostes)
    mido.grid(row=row_+3, column=pos_respostes)
    label_unitats = tk.Label(my_window, text = ('Na2S2O3 / KI'), bg=bg_, fg=fg_, font=font_, width=amplada_unitats, anchor_ = anchor_unitats)
    label_unitats.grid(row=row_+3, column=pos_unitats)
    

button_calcula_iodine = tk.Button(my_window, text = 'Calcula', command = button_calcula_iodine, bg=fg_, fg=bg_, font=font_, width=amplada_button, relief=relief_buttons_, activebackground=activebackground_, bd=0)
button_calcula_iodine.grid(row=pos_iodine+2, column=pos_button, sticky='nesw')









###########
### MRU ###
###########

            ### TITOL ###
linea3 = tk.Label(my_window, text = ' ', bg=bg_, fg=color_d_accent, font=font_)
linea3.grid(row=pos_mru, column=pos_label, columnspan=4)

label_mru = tk.Label(my_window, text = titol_mru, bg=bg_, fg=color_d_accent, font=font_)
label_mru.grid(row=pos_mru+1, column=pos_label, columnspan=2)


            ### LABEL ###

### Espai
label_espai = tk.Label(my_window, text = 'Espai (m): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_espai.grid(row=pos_mru+2, column=pos_label)


### Velocitat
label_velocitat = tk.Label(my_window, text = 'Velocitat estandard (m/s): ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_label)
label_velocitat.grid(row=pos_mru+3, column=pos_label)


### respostes ( no estaran en la columna dels labels, sino dels bottons )
label_temps = tk.Label(my_window, text = 'Temps: ', bg=bg_, fg=fg_, font=font_, anchor=anchor_, width=amplada_button)
label_temps.grid(row=pos_mru+3, column=pos_button)





            ### ENTRY ###

### Espai
espai = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
espai.grid(row=pos_mru+2, column=pos_entry, sticky='nesw')
espai.insert(INSERT, espai_)


### Velocitat
velocitat = tk.Entry(my_window, bg=bg_entry, fg=fg_, font=font_, width=amplada_entry, relief=relief_entry_)
velocitat.grid(row=pos_mru+3, column=pos_entry, sticky='nesw')
velocitat.insert(INSERT, velocitat_)






            ### BUTTON ###

### Button masa atomica
def button_calcula_temps():
    global pos_mru
    row_ = pos_mru+2
    
    x = float(espai.get())
    v = float(velocitat.get())



    global decimals
    temps = tk.Label(my_window, text = '                        ', bg=bg_, fg=fg_, font=font_, width=amplada_respostes)           #esborra la resposta anterior
    temps.grid(row=row_+1, column=pos_respostes)

    if v == 0:
        t = 'Error en divisió: ZERO'
        temps = tk.Label(my_window, text = (t), bg=bg_, fg=fg_, font=font_)
    else:
        t = x / v
        temps = tk.Label(my_window, text = (round(t, decimals)), bg=bg_, fg=fg_, font=font_, width=amplada_respostes)
        temps_iodine.delete(0, END)
        temps_iodine.insert(INSERT, t)
    temps.grid(row=row_+1, column=pos_respostes)

    label_unitats = tk.Label(my_window, text = ('s'), bg=bg_, fg=fg_, font=font_, width=amplada_unitats, anchor_ = anchor_unitats)
    label_unitats.grid(row=row_+1, column=pos_unitats)
    

button_calcula_temps = tk.Button(my_window, text = 'Calcula', command = button_calcula_temps, bg=fg_, fg=bg_, font=font_, width=amplada_button, relief=relief_buttons_, activebackground=activebackground_, bd=0)
button_calcula_temps.grid(row=pos_mru+2, column=pos_button, sticky='nesw')



####################################################################################################


### EJECUTA MAIN WINDOW o PREM ENTER ###


if AutoExecute:
    button_massa_atomica.invoke()
    button_calcula_pila.invoke()
    button_calcula_temps.invoke()
    button_calcula_iodine.invoke()

def enter_prem_botons(xd):
    button_massa_atomica.invoke()
    button_calcula_pila.invoke()
    button_calcula_temps.invoke()
    button_calcula_iodine.invoke()
my_window.bind('<Return>', enter_prem_botons) # prem enter per calcular

my_window.mainloop()


