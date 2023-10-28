<h1 align="center"><b>Eliminar duplicats</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://github.com/miquelnebotaragon/eliminar_duplicats/assets/57944755/ea8ef0b1-b055-41ed-990e-8d603b84324f"></div>


# 👁️‍🗨️ Introducció

En aquesta activitat treballarem en una aplicació capaç d'eliminar duplicats d'un llistat en format CSV. Per exemplificar el cas, ho farem a partir d'un arxiu que disposa únicament de dues columnes i segueix el model següent:  
| Llinatges Nom | DNI |
|---------------| ------------|
Sanchis Torres Jaume | 18223344A
Marchante Rodríguez Antonio | 18224466B
Sánchez Romero Juana | 18227788C
Sanchis Torres Jaume | 18223344A  


# 💻 Escenari
 
Visual Studio Code Versió: 1.83.1  
SO: Linux x64 6.1.0-13-amd64  

# 0️⃣ Abans de començar

1- Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'aquest programari i la seva versió mitjançant la instrucció següent a dins el Terminal (Ctrl+Alt+T):

```console
user@debian-mnebot:~$ sudo python3 -V
```

Si no el tenim instal·lat, el podem aconseguir fàcilment teclejant:

```console
user@debian-mnebot:~$ sudo apt install python3
```

2- Per a la importació del mòdul necessari (**pandas**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent manera:

```console
user@debian-mnebot:~$ sudo apt install python3-pip
```

3- Instal·larem, finalment, el mòdul necessari:

```console
user@debian-mnebot:~$ sudo pip install pandas
```

# 👇 Descàrrega i execució

Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **eliminar_duplicats.py**).  

📝 Descàrrega de l'arxiu .py i el fitxer d'exemple des d'<a href="https://github.com/miquelnebotaragon/endevina_numero/blob/main/encerta_numero.py" target="_blank">aquí</a>.  

# 🏆 Vull saber-ne més

Desglossant el codi:

## Part 1

```python

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Miquel Nebot · @miquelnebot · Octubre 2023

# Importació de mòduls
import pandas as pd

```

Aquesta és la part inicial i més senzilla:  
Enumeram els mòduls a importar, en aquest cas només un, pandas.

```python

# Variables:
data = pd.read_csv(sample.csv)

```

Definim una primera variable "data" que serà la font on volem comprovar si existeixen duplicats.

## Part 2  

```python

# Execució

opcio = int(input('\nCom vols que t\'ajudi el programa?\nTria una de les tres opcions següents: 1 per MARCAR duplicats || 2 per TRACTAR-LOS || 3 per ELIMINAR-LOS.\n'))

```

En aquesta segona part sol·licitarem a l'usuari que triï una de les 3 opcions disponibles pel tractament de les dades: 1 = Marcar duplicats, 2 = Tractar els duplicats i 3 = Eliminar-los directament.  

Molt important no oblidar que necessitam que la petició introduïda per l'usuari sigui en format de número enter, per això, no oblidarem *int* al principi de la instrucció.  

```python

if opcio == 1:
    data['valor_duplicat'] = data.duplicated(subset='dni')
elif opcio == 2:
    mantenir = int(input('Has escollit tractar els duplicats, quin registre vols mantenir? 1 si vols mantenir el primer || 2 per mantenir el darrer.\n'))
    if mantenir == 1:
        mantenir='first'
    else:
        mantenir='last'
    data.drop_duplicates(subset = 'dni', keep=mantenir, inplace = True)
elif opcio == 3:
    data.drop_duplicates(subset = 'dni', keep=False, inplace = True)

```

A continuació engegam una sentència condicional tot tenint en compte la sol·licitud de l'usuari:  
    - Si ha escollit **opció 1**: Emprarem l'argument "duplicated" aplicat sobre la nostra variable "data" per comprovar la columna "dni" (*subset = 'dni'*) i poder afegir així una tercera columna amb la indicació "valor_duplicat" cada vegada que en trobi un.  
    - Si ha escollit **opció 2**: Niarem aquí una segona sentència condicional per tal que, novament, l'usuari triï si vol mantenir el primer o el darrer valor duplicat que aparegui al llistat. Amb l'argument "keep" sabrem de quina manera volem procedir.  
    - Si ha escollit **opció 3**: En canvi, si l'argument "keep" el marcam com a *False*, el programa esborrarà aquests valors duplicats del llistat.

## Part 3

```python

dataframe = data

dataframe.to_csv('output.csv')
print('El programa ha finalitzat amb èxit!')

```

Arribam ja al final on establirem una nova variable "dataframe" que serà el resultat de tots els canvis efectuats al llistat anterior. Per tal de tenir un resultat operatiu en format de full de dades conduirem aquesta variable cap a un nou arxiu CSV.

# ➕ Informació

1️⃣ L'arxiu **.py** ha estat comentat al detall (#) per tal de possibilitar l'anàlisi del seu funcionament.  
2️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni perjudicis que pugui provocar el seu ús.
