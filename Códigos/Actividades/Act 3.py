
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg

b = np.array([3, 1.5, 2]) #numerador
a = np.array([1, -0.6]) #denominador
#a = np.array([1, -1.2]) #==>con esto esplota todo
w, H = sg.freqz(b, a, whole = True)
#computa la rta en frecuencia de la transferencia a partir de los coeficientes de la misma
#w es un vector con los valores para los cuales se computa la rta en frec. H es un vector con los valores de la misma
#normalmente, whole es False, y la transformada se computa solo de 0 a pi. Pero está la propiedad de simetría conjugada, que dice
# F[h*] = [H(-w)]*. Si h es real, queda H(-w) = H(w)* .Así que para omega entre -pi y 0 basta con conjugar los valores 
#de H entre 0 y pi. Alto choclo, más fácil poner whole = True y listo.

plt.plot(w, np.abs(H))
plt.grid(True)
plt.show()

z, p, k = sg.tf2zpk(b, a)

plt.scatter(z.real, z.imag, marker = 'o')
plt.scatter(p.real, p.imag, marker = 'x', color = 'r')
circulo = plt.Circle([0,0], radius = 1, fill = False, color = 'b', linewidth = 2)
plt.gca().add_patch(circulo)
plt.axis('equal')
plt.grid(True)
plt.show()

#como antes, entra una cuadrada

n = np.linspace(start = 0, stop = 100)
x = sg.square(2 * np.pi * 0.02 * n)

X = np.fft.fft(x, n = len(x) * 10)

#el filtro es IIR, ya no puedo hacer la convolución. Usar la función sg.lfilter(b, a, x)

y = sg.lfilter(b, a, x)
Y = np.fft.fft(y, n = len(y)*10)

#grafico X, H, y e Y
fig, ejes = plt.subplots(nrows = 2, ncols = 2, figsize = (10,10))

ejes[0,0].plot(np.abs(X)) #TF de la entrada
ejes[0,0].set_title('$|X(\Omega)|$')
ejes[0,0].grid(True)

ejes[0,1].plot(np.abs(H))
ejes[0,1].set_title('$|H(\Omega)|$')
ejes[0,1].grid(True)

ejes[1,0].stem(np.linspace(start = 0, stop = len(y)), y)
ejes[1,0].set_title('y[n]')
ejes[1,0].grid(True)

ejes[1,1].plot(np.abs(Y))
ejes[1,1].set_title('$|Y(\Omega)|$')
ejes[1,1].grid(True)

plt.tight_layout()
plt.show()