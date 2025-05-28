import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg

h = np.array([4.0, 3.5, 3.3, 3.2, 3.0, 2.5, 1.5, 0.5, 0.2]) # rta al imp

n = np.linspace(start = 0, stop = len(h) - 1, num = len(h)) #eje de tiempo

plt.stem(n, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid(True)
plt.show()

H = np.fft.fft(h, n = 100)
plt.plot(np.abs(H), 'x-')
plt.xlabel('$k$')
plt.ylabel('$h|H[k]|$')
plt.grid(True)
plt.show()


den = np.zeros(h.shape)
#den = np.zeros(len(h)) es equivalente. O también np.zeros(h.size)
den[0] = 1
z, p, k = sg.tf2zpk(h, den)
#esta función tan simpática toma los coeficientes del numerador y denominador de la transferencia del sistema y te da los ceros, polos y ganancia
#el nombre es raro, pero significa transfer function to zeros, poles and gain. ¿De dónde cuernos salió la k?
#los coeficientes del numerador son los 9 coeficientes de h. Los coeficientes del denominador son todos cero, menos el primero

plt.scatter(z.real, z.imag, marker = 'o')
plt.scatter(p.real, p.imag, marker = 'x', c = 'r')

#agrego un círculo unitario para tener una referencia
circulo = plt.Circle((0, 0), radius=1, color='r', fill=False, linewidth=2)
ax = plt.gca() #get current axes
ax.add_patch(circulo) #sobre los ejes agrega el parche
#alternatica más compacta: plt.gca().add_patch(circulo)

plt.axis('equal') #para mantener la proporción
plt.grid(True)
plt.show()

#ahora entra una cuadrada a mi sistema ¿Cuál es la salida?
#tengo que graficar 1) la señal de entrada, 2) su transformada, 3)la señal de salida 4) su transformada
#defino la cuadrada con sg.square

n = np.arange(0, 100) #redefino el eje de tiempos
x = sg.square(2 * np.pi * 0.02 * n)

X = np.fft.fft(x, n = len(x*10))

y = np.convolve(h, x, mode = 'full')

Y = np.fft.fft(y, n = len(y)*10)
#estas son todas las cuentas. Ahora grafico

fig, ejes = plt.subplots(nrows = 2, ncols = 2, figsize = (10, 8))

ejes[0, 0].stem(n, x)
ejes[0, 0].grid(True)

ejes[0, 1].plot(np.abs(X))
ejes[0, 1].grid(True)

ejes[1, 0].stem(np.arange(0, len(y)), y)
ejes[1, 0].grid(True)

ejes[1, 1].plot(np.abs(Y))
ejes[1, 1].grid(True)

plt.tight_layout()
plt.show()