import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#Calculamos h * h~ para M = 30. Dentro del for filtramos los datos que necesitemos
M_MAX = 30 #máximo valor de M
h = np.array([1, 0.6, 0.2, -0.2, 0.1, 0.05])
h = np.pad(h, (0, M_MAX - len(h)), 'constant') #Llenamos con 0

h_mirror = h[::-1]

# Convolucionar h con su espejo
conv_result = np.convolve(h, h_mirror)
conv_result = conv_result[M_MAX - 1:] #nos quedamos solo con los tau positivos

# Crear la delta de magnitud 0.005 (misma longitud que conv_result)
delta = np.zeros_like(conv_result)
delta[0] = 0.005  # impulso en n=0

# Sumar la delta al resultado de la convolución
RY = conv_result + delta

puntos = 1024 #puntos para las dft´s
frecs = np.linspace(start = 0, stop = 2 * np.pi, num = puntos)#eje de frecuencias

for M in [2, 5, 10, 30]:


  #Cálculo de los coeficientes


  RY_0 = RY[0: M] #coeficientes de interés para distintos M
  RY_toeplitz = sp.linalg.toeplitz(RY_0)
  #Invertimos RY
  RY_inv = np.linalg.inv(RY_toeplitz)

  # Seleccionamos la primer columna
  w0 = h[0] * RY_inv[:, 0]


  #Graficamos los coeficientes
  plt.stem(w0, basefmt= 'k', markerfmt = 'ok', linefmt = 'k--')

  plt.xlim(-1, M)
  plt.xlabel('k')

  plt.ylabel(r'$w(k)$')

  plt.title(f'Coeficientes para M = {M}')

  plt.grid(True)

  plt.show()


  #Convolución con h(n)

  conv = np.convolve(w0, h, mode = 'full')

  k = np.arange(start = 0, stop = len(h) + M - 1) #eje horizontal

  plt.stem(k, conv, basefmt= 'k', markerfmt = 'ok', linefmt = 'k--')

  plt.xlim(-1, 6 + M - 1) #6 es la cantidad de coeficientes no nulos de h.
  #la convolución entre h y w va de 0 a 6 + M - 2, tiene 6 + M - 1 elementos

  plt.xlabel('k')

  plt.ylabel(r'$(h \ast w)(k)$')

  plt.title(f'Convolución entre h y w para M = {M}')

  plt.grid(True)
  plt.show()


  #Análisis en frecuencia

  W = np.abs(np.fft.fft(w0, n = puntos))

  H = np.abs(np.fft.fft(h, n = puntos))

  plt.plot(frecs, W, label = r'|$W(\omega)|$')
  plt.plot(frecs, H, label = r'$|H(\omega)|$')

  plt.xlim(0, 2 * np.pi)
  plt.xlabel(r'$\omega$')

  plt.ylabel(r'$|W(\omega)|$ y $|W(\omega)|$')

  plt.title(f'Análisis en frecuencia para M = {M}')

  plt.legend()
  plt.grid(True)
  plt.show()

  prod = W * H

  plt.plot(frecs, prod)

  plt.xlim(0, 2 * np.pi)
  plt.xlabel(r'$\omega$')

  plt.ylabel(r'$|W(\omega)|\cdot|W(\omega)|$')

  plt.title(f'$|H(\omega)|\cdot|W(\omega)|$ para M = {M}')

  plt.grid(True)
  plt.show()

"""Calculamos Z (señal ecualizada) para cada M"""

N_bits = 100
sigma_v = np.sqrt(0.005)
X = 2*np.random.binomial(1, 0.5, N_bits) - 1
V = np.random.normal(0, sigma_v, N_bits)
Y = sp.signal.lfilter(h, 1, X) + V

N = range(len(X)) #eje horizontal de los gráficos

for M in [2, 5, 10, 30]:

  #Cálculo de los coeficientes


  RY_0 = RY[0: M] #coeficientes de interés para distintos M
  RY_toeplitz = sp.linalg.toeplitz(RY_0)
  #Invertimos RY
  RY_inv = np.linalg.inv(RY_toeplitz)

  # Seleccionamos la primer columna
  w0 = h[0] * RY_inv[:, 0]

  #pasamos Y por el ecualizador
  Z = sp.signal.lfilter(w0, 1, Y)

  #ploteamos X y Z:

  plt.step(N, X, label='X(n)')
  plt.step(N, Z, label = f'Z(n) para M = {M}')

  plt.xlim(0, 20)
  plt.xlabel('n')

  plt.ylabel(r'$X(n)$ y $Z(n)$')

  plt.title(f'X(n) y Z(n) para M = {M}')

  plt.legend()
  plt.grid(True)
  plt.show()

