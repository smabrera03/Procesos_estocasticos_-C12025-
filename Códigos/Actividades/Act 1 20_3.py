import numpy as np
import matplotlib.pyplot as plt

N = 100 #cantidad de muestras
bins = 10 #cantidad de divisiones
sigma = 0.5 #parámetro de la rayleigh
P
x = np.random.rayleigh(scale = sigma, size = N)
#scale se llama en inglés al parámetro de la rayleigh. 

plt.hist(x = x, bins = bins, density = True)
#con density = True, el área abajo del histograma integra 1, dando una aproximación de la PDF

#ya que estamos, grafico la PDF:

t = np.linspace(start = 0, stop = np.max(x), num = 1000)
pdf = (t/sigma**2)*np.exp(-t**2/(2*sigma**2))

plt.plot(t, pdf)
plt.grid(True)

plt.show()
#obs: el histogramam y la pdf son más o menos parecidos

#cambio los parámetros
N = 100
bins = 30
x = np.random.rayleigh(scale = sigma, size = N)
plt.hist(x = x, bins = bins, density = True)
t = np.linspace(start = 0, stop = np.max(x), num = 1000)
pdf = (t/sigma**2)*np.exp(-t**2/(2*sigma**2))
plt.plot(t, pdf)
plt.grid(True)
plt.show()
#obs: el histograma y la pdf no tienen nada que ver. Hay muchos bins y pocas muestras, x lo que el histograma aparece
#todor roto


N = 10000
bins = 30
x = np.random.rayleigh(scale = sigma, size = N)
plt.hist(x = x, bins = bins, density = True)
t = np.linspace(start = 0, stop = np.max(x), num = 1000)
pdf = (t/sigma**2)*np.exp(-t**2/(2*sigma**2))
plt.plot(t, pdf)
plt.grid(True)
plt.show()
#obs: ahora sí, obvio
#conclusión: No basta con subir las bins.

#y si tengo muchas muestras y pocas bins?



N = 10000
bins = 10
x = np.random.rayleigh(scale = sigma, size = N)
plt.hist(x = x, bins = bins, density = True)
t = np.linspace(start = 0, stop = np.max(x), num = 1000)
pdf = (t/sigma**2)*np.exp(-t**2/(2*sigma**2))
plt.plot(t, pdf)
plt.grid(True)
plt.show()
#no se ve taaan mal. Es mejor tener muchas muestras y pocas bins que tener muchas bins y pocas muestras