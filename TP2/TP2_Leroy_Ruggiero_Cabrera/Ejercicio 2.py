import numpy as np
import matplotlib.pyplot as plt

#cargamos las matrices generadas por Generar Matrices.py
Potencia = np.load("Potencia.npy")
Viento = np.load("Viento.npy")

t = np.linspace(start = 0, stop = 24, num = len(Potencia[0, :, 0]))
#array de tiempos

#Me paro en una torre, agarro todas las realizaciones y hago el promedio a lo largo de las realizaciones. Ploteo eso
#en función del tiempo

for i in [1,10,20]:
    PTi = Potencia[:,:,i]
    PTi_media = np.mean(PTi, axis=0)

    plt.plot(t, PTi_media)
    plt.title(f'Potencia media de la torre {i}')
    
    plt.xlabel('Hora del día')
    plt.xlim(0, 24)

    plt.ylabel('Potencia [W]')

    plt.grid(True)
    plt.savefig(f'Potencia media (T{i}).png')  # Guardar imagen
    plt.show()

    VTi = Viento[:, :, i] #todas las realizaciones del viento de la torre i
    VTi_media = np.mean(VTi, axis=0)

    plt.plot(t, VTi_media, color='green')
    plt.title(f'Velocidad media del viento de la torre {i}')
    
    plt.xlabel('Hora del día')
    plt.xlim(0, 24)

    plt.ylabel('Velocidad [m/s]')

    plt.grid(True)
    plt.savefig(f'Velocidad media (T{i}).png')
    plt.show()