#En este archivo extraemos los datos de las hojas de datos y generamos las matrices de potencia y viento reescribiendo
#las mediciones inválidas.
#Puede tardar varios minutos en terminar

#Cargamos los datos de la potencia
import pandas as pd
import numpy as np


#Cargar el archivo
archivo_excel = 'PotenciaDia1.ods'

#Leer los nombres de las hojas
hojas = pd.ExcelFile(archivo_excel).sheet_names

#Inicializar lista para acumular los datos
datos = []

for hoja in hojas:
    #Leer cada hoja como DataFrame
    df = pd.read_excel(archivo_excel, sheet_name=hoja, header=None)  #header=None si no hay nombres de columnas
    datos.append(df.values)  #convertimos a array de numpy

#Convertimos a array 3D: (12, 144, 25)
Potencia = np.stack(datos)

print(Potencia.shape)  #Debería ser (12, 144, 25)


#Cargamos los datos del viento
archivo_excel = 'VientosDia1.ods'

hojas = pd.ExcelFile(archivo_excel).sheet_names

datos = []

for hoja in hojas:
    df = pd.read_excel(archivo_excel, sheet_name=hoja, header=None)
    datos.append(df.values)

Viento = np.stack(datos)

print(Viento.shape)

Viento[Viento < 0] = 0
Potencia[Potencia < 0] = 0
#reescribimos los valores menores a 0 como 0.

np.save("Potencia.npy", Potencia)
np.save("Viento.npy", Viento)