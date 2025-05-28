import numpy as np
import matplotlib.pyplot as plt

#cargamos las matrices generadas por Generar Matrices.py
Potencia = np.load("Potencia.npy")
Viento = np.load("Viento.npy")

#
#
#                                    Potencia
#
#

t = np.linspace(start = 0, stop = 24, num = len(Potencia[0, :, 0]))
#array de tiempo

L = 3
realizacion = np.mean(Potencia[:, :, 0], axis = 0)
cantidad_ventanas = len(realizacion) - L + 1  # 142

# Preparamos la matriz de autocorrelaciones
# La autocorrelación de una señal de 10 puntos tiene 2*10 - 1 = 19 valores (lags de -9 a +9)
R = np.zeros((cantidad_ventanas, 2 * L - 1))

lags = np.arange(-(L-1), L)
for n in range(cantidad_ventanas):
    ventana = realizacion[n:n + L]
    autocorr = np.correlate(ventana, ventana, mode='full')

    autocorr = autocorr / (L - np.abs(lags))
    #autocorr = autocorr / L

    R[n, :] = autocorr

# Visualización
plt.imshow(R, aspect='auto', origin='lower', interpolation = 'none', extent=[-(L-1), L-1, 0, cantidad_ventanas])
plt.colorbar(label='Autocorrelación')

plt.xlabel(r'$\tau$')

plt.ylabel(r'$n$')

plt.title(f'$RP(n, \\tau)$ para L = {L}')
#plt.show()
plt.savefig('RP1 (L = 3)')
plt.clf()

S = np.fft.fft(R, n = 10000, axis = 1)
S = np.abs(S)

plt.imshow(S, aspect='auto', origin='lower', extent=[0, 2*np.pi, 0, cantidad_ventanas])  # Límite inferior y superior del colormap
plt.colorbar(label='Magnitud espectral')

plt.xlabel('$\\omega$')

plt.ylabel(r'$n$')

plt.title(f'$FP_1(n, \\omega)$ para L = {L}')
#plt.show()
plt.savefig('FP1 (L = 3)')
plt.clf()

#
#
#                                                    Viento
#
#


realizacion = np.mean(Viento[:, :, 0], axis = 0)

RV1 = np.zeros((cantidad_ventanas, 2 * L - 1))#función de autocorrelación para el viento de la torre 1

for n in range(cantidad_ventanas):
    ventana = realizacion[n:n + L] #ventaneo
    autocorr =  np.correlate(ventana, ventana, mode='full')

    autocorr = autocorr/(L - np.abs(lags))
    #autocorr = autocorr / L

    RV1[n, :] = autocorr

plt.imshow(RV1, aspect='auto', origin='lower', interpolation = 'none',extent=[-(L-1), L-1, 0, cantidad_ventanas - 1])
plt.colorbar(label='Autocorrelación')

plt.xlabel(r'$\tau$')

plt.ylabel(r'$n$')

plt.title(f'$RV_1(n, \\tau)$ para L = {L}')
#plt.show()
plt.savefig('RV1 (L = 3)')
plt.clf()

FV1 = np.fft.fft(RV1, n = 1000, axis = 1)
FV1 = np.abs(FV1)

plt.imshow(FV1, aspect='auto', origin='lower', extent=[0, 2*np.pi, 0, cantidad_ventanas - 1])  # Límite inferior y superior del colormap
plt.colorbar(label='Magnitud espectral')

plt.xlabel('$\omega$')
plt.ylabel('n')

plt.title(f'$FV_1(n, \\omega)$ para L = {L}')
#plt.show()
plt.savefig('FV1 (L = 3)')
plt.clf()

#
#
#                                           Medias
#
#
#==> Potencia

realizacion = np.mean(Potencia[:, :, 0], axis = 0)

media = np.zeros((cantidad_ventanas, L)) #en esta matriz guardo la media en función del tiempo dentro de cada ventana

for n in range(cantidad_ventanas):
  media_en_ventana = realizacion[n: n + L]
  media[n] = media_en_ventana

for i in [0, 60, 134]:
  plt.plot(media[i], label = f'ventana {i}')


plt.xlabel('tiempo')
plt.xticks(ticks = [0, 1, 2], labels = ['n', 'n + 1', 'n + 2'])
plt.xlim([0, 2])

plt.ylabel(f'$E[P_1(n)]$ para L = {L}')
plt.title('Media para distintas ventanas')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('Medias de la potencia para distintas ventanas (L = 3)')
plt.clf()

#==> Vientos

realizacion = np.mean(Viento[:, :, 0], axis = 0)
media = np.zeros((cantidad_ventanas, L)) #en esta matriz guardo la media en función del tiempo dentro de cada ventana

for n in range(cantidad_ventanas):
  media_en_ventana = realizacion[n: n + L]
  media[n] = media_en_ventana

for i in [0, 60, 134]:
  plt.plot(media[i], label = f'ventana {i}')


plt.xlabel('tiempo')
plt.xticks(ticks = [0, 1, 2], labels = ['n', 'n + 1', 'n + 2'])
plt.xlim([0, 2])

plt.ylabel(f'$E[V_1(n)]$ para L = {L}')
plt.title('Media para distintas ventanas')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('Meidas del viento para distintas ventanas (L = 3)')