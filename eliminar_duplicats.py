#!/usr/bin/python
# _*_ coding: utf-8 _*_
# Miquel Nebot · @miquelnebot · Octubre 2023

# Importació de mòduls i creació d'àlies
import pandas as pd 


# Variables
data = pd.read_csv('sample.csv') # Pandas llegirà la informació del full de càlcul.

# Execució
opcio = int(input('\nCom vols que t\'ajudi el programa?\nTria una de les tres opcions següents: 1 per MARCAR duplicats || 2 per TRACTAR-LOS || 3 per ELIMINAR-LOS.\n'))

if opcio == 1:
    data['valor_duplicat'] = data.duplicated(subset='dni') # Afegirà l'etiqueta "valor duplicat" als valors repetits a la columna "dni"
elif opcio == 2:
    mantenir = int(input('Has escollit tractar els duplicats, quin registre vols mantenir? 1 si vols mantenir el primer || 2 per mantenir el darrer.\n'))
    if mantenir == 1:
        mantenir='first'
    else:
        mantenir='last'
    data.drop_duplicates(subset = 'dni', keep=mantenir, inplace = True) # Amb "keep" mantindrem (a decisió de l'usari) el primer o el darrer valor.
elif opcio == 3:
    data.drop_duplicates(subset = 'dni', keep=False, inplace = True) # Amb "keep = False" esborrarem els duplicats.

dataframe = data

dataframe.to_csv('output.csv') # Copiarem la nova informació en format de dataframe a un nou arxiu CSV.
#print('El programa ha finalitzat amb èxit!')