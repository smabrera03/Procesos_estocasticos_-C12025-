import numpy as np
import matplotlib.pyplot as plt

#cargamos las matrices generadas por Generar Matrices.py
Potencia = np.load("Potencia.npy")
Viento = np.load("Viento.npy")

t = np.linspace(start = 0, stop = 24, num = len(Potencia[0, :, 0]))
#array de tiempo

#
#
#                                                     Potencia
#
#


realizacion = np.mean(Potencia[:, :, 0], axis = 0) #Como realizacion de nuestro proceso aleatorio consideramos la media de las 12 realizaciones
#para hacer las estimaciones de la función de autocorr.


#Parámetros
L = 10
cantidad_ventanas = len(realizacion) - (L - 1)  # 135 valores posibles para n

#La autocorrelación de una señal de 10 puntos tiene 2*10 - 1 = 19 valores (lags de -9 a +9)
R = np.zeros((cantidad_ventanas, 2 * L - 1))


lags = np.arange(-(L-1), L) #vector de largo 2L - 1 = 19

for n in range(cantidad_ventanas):
    ventana = realizacion[n:n + L]
    autocorr = np.correlate(ventana, ventana, mode='full')

    autocorr = autocorr / (L - np.abs(lags)) #división elemento a elemento #Autocorrelación insesgada
    #autocorr = autocorr / L #Autocorrelación sesgada (ventaneada)
    #comentar y descomentar en función de lo que quieras
    R[n, :] = autocorr

#De esta forma, R es una matriz de 134 filas y 19 columnas.
#Cada fila es una función de autocorrelación para una ventana distinta
#El eje de las filas representa el eje de tau.

#grafico un par de autocorrelaciones
tau = np.arange(start = - (L-1), stop = L)#eje tau

lineas = ['r-', 'b-', 'k-'] #formato de las lineas
j = 0 #esta variable la uso para iterar el vector lineas
for i in [0, 60, 134]:
  plt.stem(tau, R[i], label = f'R({i}, $\\tau$)', linefmt = lineas[j], basefmt = ' ')
  j = j + 1


plt.title('Autocorrelaciones para distintos valores de n')

plt.xlabel(r'$\tau$')

plt.ylabel('$RP_1(n, \\tau$)')
plt.ylim(0)

plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('Algunas autocorrelaciones (L = 10)')
plt.clf()

#Podemos graficar todas las autocorrelaciones juntas en un grafico de colores

#en el eje vertical veo el valor de n, es decir, la primera de las 10 bochas que agarro.

plt.imshow(R, aspect='auto', origin='lower', interpolation = 'none',extent=[-(L-1), L-1, 0, cantidad_ventanas])
#extent = [xmin, xmax, ymin, ymax] Esto significa extent
plt.colorbar(label='Autocorrelación')

plt.xlabel(r'$\tau$')

plt.ylabel(r'$n$')

plt.title(f'Función $RP_1(n, \\tau)$ para L = {L}')
#plt.show()
plt.savefig('RP1 (L = 10)')
plt.clf()

                                          ###PSD###
S = np.fft.fft(R, n = 10000, axis = 1)
S = np.abs(S)
#S por si sola no da real positiva, pero es porque las autocorrelaciones de R estan desplazadas en el tiempo. Eso
#en Fourier introduce un desfasaje. Sin embargo, ese desfasaje no afecta al valor absoluto, por lo que para corregir
#ese efecto le tomamos el modulo y listo.

#de esta forma, S es una matriz de 135x1000. La fila i representa la DFT de R[i, tau]
w = np.linspace(start = 0, stop = 2*np.pi, num = len(S[0]))#eje de frecuencias

for i in [0, 60, 134]:
  plt.plot(w, S[i], label = f'S({i}, $\\omega$)')

plt.xlim(w[0], w[-1])
plt.xlabel('$\\omega$')

plt.ylabel('S($\\omega$)')

plt.title('$FP_1(n, \\omega)$ para distintos valores de n')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('Algunas PSD (L = 10)')
plt.clf()


#Mapa de colores de la PSD
plt.imshow(S, aspect='auto', origin='lower', extent=[0, 2*np.pi, 0, cantidad_ventanas])  # Límite inferior y superior del colormap
plt.colorbar(label='Magnitud espectral')

plt.xlabel('$\omega$')

plt.ylabel('n')

plt.title('$FP_1(n, \\omega)$')
#plt.show()
plt.savefig('FP1 (L = 10)')
plt.clf()


#
#
#                                                    Viento
#
#


realizacion = np.mean(Viento[:, :, 0], axis = 0) #como antes, para hacer las estimaciones consideramos la media de las 12 realizaciones
#del proceso V1(n)

cantidad_ventanas = len(realizacion) - (L - 1)#135 para L=10 (n va de 0 a 134)
RV1 = np.zeros((cantidad_ventanas, 2 * L - 1))#función de autocorrelación para el viento de la torre 1

lags = np.arange(-(L-1), L)
for n in range(cantidad_ventanas):
    ventana = realizacion[n:n + L] #ventaneo
    autocorr = np.correlate(ventana, ventana, mode='full')

    autocorr = autocorr/(L - np.abs(lags))
    #autocorr = autocorr / L

    RV1[n, :] = autocorr

plt.imshow(RV1, aspect='auto', origin='lower', interpolation = 'none',extent=[-(L-1), L-1, 0, cantidad_ventanas - 1])
plt.colorbar(label='Autocorrelación')

plt.xlabel(r'$\tau$')

plt.ylabel(r'$n$')

plt.title(f'Función $RV_1(n, \\tau)$ para L = {L}')
#plt.show()
plt.savefig('RV1 (L = 10)')
plt.clf()


#                                                  PSD


FV1 = np.fft.fft(RV1, n = 1000, axis = 1)
FV1 = np.abs(FV1)

plt.imshow(FV1, aspect='auto', origin='lower', extent=[0, 2*np.pi, 0, cantidad_ventanas - 1])  # Límite inferior y superior del colormap
plt.colorbar(label='Magnitud espectral')

plt.xlabel('$\omega$')
plt.ylabel('n')

plt.title(f'$FV_1(n, \\omega)$ para L = {L}')
#plt.show()
plt.savefig('FV1 (L = 10)')
plt.clf()

#                                               Medias
#==> Potencia
realizacion = np.mean(Potencia[:, :, 0], axis = 0)
media = np.zeros((cantidad_ventanas, L)) #en esta matriz guardo la media en función del tiempo dentro de cada ventana

for n in range(cantidad_ventanas):
  media_en_ventana = realizacion[n: n + L]
  media[n] = media_en_ventana

for i in [0, 60, 134]:
  plt.plot(media[i], label = f'ventana {i}')


plt.xlabel('tiempo')
plt.xticks(ticks = [0, 4, 9], labels = ['n', 'n + 4', 'n + 9'])
plt.xlim([0, 9])

plt.ylabel(f'$E[P_1(n)]$ para L = {L}')

plt.title('Media para distintas ventanas')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('Medias de la potencia para distintas ventanas (L = 10)')
plt.clf()

#==> Viento
realizacion = np.mean(Viento[:, :, 0], axis = 0)

media = np.zeros((cantidad_ventanas, L)) #en esta matriz guardo la media en función del tiempo dentro de cada ventana

for n in range(cantidad_ventanas):
  media_en_ventana = realizacion[n: n + L]
  media[n] = media_en_ventana

for i in [0, 60, 134]:
  plt.plot(media[i], label = f'ventana {i}')


plt.xlabel('tiempo')
plt.xticks(ticks = [0, 4, 9], labels = ['n', 'n + 4', 'n + 9'])
plt.xlim([0, 9])

plt.ylabel(f'$E[V_1(n)]$ para L = {L}')
plt.title('Media para distintas ventanas')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('Medias del viento para distintas ventanas (L = 10)')
plt.clf()