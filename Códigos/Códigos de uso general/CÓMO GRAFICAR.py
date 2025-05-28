#un solo grafico:
"""
instrucciones: stem se puede reemplazar por plot
plt.stem( , ) 
plt.xlabel('')
plt.ylabel('')
plt.grid(True)
plt.show()
"""

#4 gráficos en una imagen
"""
fig, ejes = plt.subplots(nrows = 2, ncols = 2, figsize = (10,10))

#primer gráfico
ejes[0,0].plot()
ejes[0,0].set_title('')
ejes[0,0].set_xlabel('')
ejes[0,0].set_ylabel('')
ejes[0,0].grid(True)

#segundo gráfico
ejes[0,1].plot()
ejes[0,1].set_title('')
ejes[0,1].set_xlabel('')
ejes[0,1].set_ylabel('')
ejes[0,1].grid(True)

#tercer gráfico
ejes[1,0].plot()
ejes[1,0].set_title('')
ejes[1,0].set_xlabel('')
ejes[1,0].set_ylabel('')
ejes[1,0].grid(True)

#cuarto gráfico
ejes[1,1].plot()
ejes[1,1].set_title('')
ejes[1,1].set_xlabel('')
ejes[1,1].set_ylabel('')
ejes[1,1].grid(True)

plt.tight_layout()
plt.show()
"""

#Personalizaciones opcionales
"""
Límites:
ejes[, ].set_xlim(xmin = , xmax = )
ejes[, ].set_ylim(ymin = , ymax = )

Ticks: 
ejes[, ].set_xticks()
ejes[, ].set_yticks()

Para leyendas preguntarle al chat

"""

#EJEMPLOS
import matplotlib.pyplot as plt
import numpy as np

#Ejemplo 1: un solo gráfico con stem()
#definí tus señales
n = np.linspace(start = 0, stop = 9, num = 10)
x = np.linspace(start = 0, stop = 9, num = 10)

plt.stem(n, x, linefmt='b-', markerfmt='ro', basefmt='k-') #agregar detalles si hiciera falta
plt.title('x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xlim(0,5)
plt.grid(True, color = 'k')
plt.show()

#Para graficar algo continuo, conviene usar plt.plot() ¿Investigar los 8 millones de argumentos que tienen estas funciones?

#
#
#
#
#

#ejemplo 2: gráficos con plt.subplots()

t = np.linspace(start=0, stop = 6, num = 100)
x = np.sin(t)
y = np.cos(t)

fig, ejes = plt.subplots(nrows = 2, ncols = 1, figsize = (6,6), tight_layout = True, sharex = True, sharey = True)
#el tight layout se puede poner acá directamente. sharex y sharey hacen q ambos gráficos tengan la misma escala

#primer gráfico
ejes[0].plot(x)
ejes[0].set_title('seno')
ejes[0].set_xlabel('t')
ejes[0].set_ylabel('x de t')
ejes[0].grid(True)

#segundo gráfico
ejes[1].plot(y)
ejes[1].set_title('coseno')
ejes[1].set_xlabel('t')
ejes[1].set_ylabel('y de t')
ejes[1].grid(True)

plt.show()

#
#
#
#
#

#Ejemplo 3: ticks y leyenda

fig, ejes = plt.subplots(tight_layout = True)

ejes.plot(t, x, label = 'seno')
ejes.plot(t, y, label = 'coseno')
ejes.set_title('lol')
ejes.set_xlabel('lol')
ejes.set_ylabel('lel')
ejes.grid(True)

ejes.set_xticks([0, 1, 2], ["cero", "uno", "dos"])
#ejes.set_xticklabels(["cero", "uno", "dos"]) #otra opción, pero la linea de arriba me parece más cómoda.

ejes.legend(loc = "upper right")
#otras opciones:
#ejes.legend(loc = "best")
#ejes.legend(loc = "lower left")
plt.show()
