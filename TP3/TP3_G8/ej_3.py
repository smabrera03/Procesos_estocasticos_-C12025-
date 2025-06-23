
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Respuesta impulsiva del canal
h_primitiva = np.array([1, 0.6, 0.2, -0.2, 0.1, 0.05])
sigma_v = np.sqrt(0.005)
M = 20
N_bits = 100
h = np.pad(h_primitiva, (0, M-len(h_primitiva)), 'constant')
print(h.shape)

X = 2*np.random.binomial(1, 0.5, N_bits) - 1
V = np.random.normal(0, sigma_v, N_bits)
Y = sp.signal.lfilter(h, 1, X) + V

"""Calculamos los coeficientes óptimos de $w_o$:"""

h_mirror = h[::-1]#rta al impulso reflejada

# Convolucionar h con su espejo
conv_result_primitiva = np.convolve(h, h_mirror)
conv_result = conv_result_primitiva[M-1:] #tomamos los valores de la convolución para k positivo

# Crear la delta de magnitud 0.005 (misma longitud que conv_result)
delta = np.zeros_like(conv_result)
delta[0] = 0.005  # impulso en n=0

# Sumar la delta al resultado de la convolución
RY = conv_result + delta
RY_toeplitz = sp.linalg.toeplitz(RY)

# Invertimos RY
RY_inv = np.linalg.inv(RY_toeplitz)

# Seleccionamos la primer columna
w0 = h[0] * RY_inv[:, 0]
print(w0)

Z = sp.signal.lfilter(w0, 1, Y)
N = range(len(X))  # eje horizontal de los gráficos

# Ploteamos X
plt.figure(figsize=(10, 5), dpi=100)
plt.step(N, X, label='X(n)')
plt.xlim(0, 20)
plt.axhline(0, color='k')
plt.legend()
plt.grid(True)
#plt.savefig('plot_X.png')    # guardo figura
plt.show()

# Ploteamos X e Y
plt.figure(figsize=(10, 5), dpi=100)
plt.step(N, X, label='X(n)')
plt.step(N, Y, label='Y(n)')
plt.xlim(0, 20)
plt.axhline(0, color='k')
plt.legend()
plt.grid(True)
#plt.savefig('plot_X_Y.png')  # guardo figura
plt.show()

# Ploteamos X y Z
plt.figure(figsize=(10, 5), dpi=100)
plt.step(N, X, label='X(n)')
plt.step(N, Z, label='Z(n)')
plt.xlim(0, 20)
plt.axhline(0, color='k')
plt.legend()
plt.grid(True)
#plt.savefig('plot_X_Z.png')  # guardo figura
plt.show()

"""### $R_X(\tau)$"""

R_X = (1/len(X)) * np.correlate(X, X, mode='full')
tau = np.arange(start=-len(X) + 1, stop=len(X))
R_X_teorica = np.zeros(len(tau))
for i in range(len(tau)):
    if tau[i] == 0:
        R_X_teorica[i] = 1

plt.stem(tau, R_X, basefmt='')
plt.stem(tau, R_X_teorica, markerfmt='xr', linefmt='r', basefmt='r')
plt.xlim(-10, 10)
plt.ylim(-0.5, 1.5)
plt.xlabel(r'$k$')
plt.ylabel(r'$R_X$')
plt.legend([r'$R_X$ empírica', r'$R_X$ teórica'])

plt.grid(True)
#plt.savefig('RX.png')  # guardo la figura
plt.show()

"""### $S_X(e^{j\omega})$"""

puntos = 10000 #puntos de la fft
S_X = np.abs(np.fft.fft(R_X, n=puntos))
frecs = np.linspace(start=0, stop=2 * np.pi, num=puntos)
S_X_teorica = np.ones(puntos)

plt.figure(figsize=(10, 5), dpi=100)
plt.plot(frecs, S_X)
plt.plot(frecs, S_X_teorica, color='r')
plt.xlabel(r'$e^{j\omega}$')
plt.ylabel(r'$S_X(\omega)$')

plt.xlim(0, 2 * np.pi)
# Etiquetas del eje x en múltiplos de π
pi_ticks = np.arange(0, 2 * np.pi + 0.1, np.pi / 2)  # hasta 2π
plt.xticks(pi_ticks, [r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])

plt.legend([r'$S_X$ empírica', r'$S_X$ teórica'])
plt.grid(True)
#plt.savefig('SX.png')  # guardo figura
plt.show()

"""### $R_Y(\tau)$"""

R_Y = (1/len(Y)) * np.correlate(Y, Y, mode='full')
tau = np.arange(start=-len(Y) + 1, stop=len(Y))
R_Y_teorica = np.zeros(len(tau))

# Buscar el índice en tau donde τ = 0
i_0 = np.where(tau == 0)[0][0]
start = i_0 - len(conv_result_primitiva) // 2
end = start + len(conv_result_primitiva)

# Insertar conv_result centrado en τ = 0
R_Y_teorica[start:end] = conv_result_primitiva

plt.figure(figsize=(10, 5), dpi=100)
plt.stem(tau, R_Y, basefmt='')
plt.stem(tau, R_Y_teorica, markerfmt='xr', linefmt='r', basefmt='r')
plt.xlim(-20, 20)
plt.ylim(-0.5, 1.5)
plt.xlabel(r'$k$')
plt.ylabel(r'$R_Y$')
plt.legend([r'$R_Y$ empírica', r'$R_Y$ teórica'])

plt.grid(True)
#plt.savefig('RY.png')  # guardo figura
plt.show()

"""### $S_Y(e^{j\omega})$"""

puntos = 10000
S_Y = np.abs(np.fft.fft(R_Y, n = puntos))
frecs = np.linspace(start = 0, stop = 2 * np.pi, num = puntos)
S_Y_teorica = np.abs(np.fft.fft(R_Y_teorica, n = puntos))

plt.figure(figsize=(10, 5), dpi=100)
plt.plot(frecs, S_Y)
plt.plot(frecs, S_Y_teorica)
plt.xlabel(r'$e^{j\omega}$')
plt.ylabel(r'$S_Y(e^{j\omega})$')

plt.xlim(0, 2 * np.pi)
# Etiquetas del eje x en múltiplos de π
pi_ticks = np.arange(0, 2 * np.pi + 0.1, np.pi / 2)  # hasta 2π
plt.xticks(pi_ticks, [r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])

plt.legend([r'$S_Y$ empírica', r'$S_Y$ teórica'])
plt.grid(True)
#plt.savefig('SY.png')  # guardo figura
plt.show()

"""### $R_Z(k)$"""

R_Z = (1/len(Z)) * np.correlate(Z, Z, mode = 'full')
tau = np.arange(start = -len(Z) + 1, stop = len(Z))

plt.figure(figsize=(10, 5), dpi=100)
plt.stem(tau, R_Z, basefmt = '')
markerline, stemline, baseline = plt.stem(
    tau, R_X,
    linefmt='orange',       # línea vertical de los stems
    markerfmt='o',          # marcador circular
    basefmt='--'      # línea base punteada naranja
)

plt.setp(stemline, alpha=0.6)
plt.setp(markerline, markersize=5, alpha=0.6)
plt.setp(baseline, alpha=0.6, color='orange')

plt.xlim(-20, 20)
plt.ylim(-0.5, 1.5)
plt.xlabel(r'$k$')
plt.ylabel(r'$R_Z$')
plt.legend([r'$R_Z$ empírica', r'$R_X$ empírica'])

plt.grid(True)
#plt.savefig('RZ.png')  # guardo figura
plt.show()

"""### $S_Z(e^{j\omega})$"""

puntos = 10000
S_Z = np.abs(np.fft.fft(R_Z, n = puntos))
frecs = np.linspace(start = 0, stop = 2 * np.pi, num = puntos)

plt.figure(figsize=(15, 5), dpi=100)
plt.plot(frecs, S_Z)
plt.plot(frecs, S_X, linestyle = '--')
plt.xlabel(r'$e^{j\omega}$')
plt.ylabel(r'$S_YZ(e^{j\omega})$')

plt.xlim(0, 2 * np.pi)
# Etiquetas del eje x en múltiplos de π
pi_ticks = np.arange(0, 2 * np.pi + 0.1, np.pi / 2)  # hasta 2π
plt.xticks(pi_ticks, [r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])

plt.legend([r'$S_Z$ empírica', r'$S_X$ empírica'])
plt.grid(True)
#plt.savefig('SZ.png')  # guardo figura
plt.show()

"""###Coeficientes del canal y del ecualizador"""

plt.stem(h, label = 'h(n)', basefmt = 'k')

plt.stem(w0, markerfmt = 'xr', linefmt = 'r', basefmt = 'k', label = 'coeficientes del EC.')

plt.xlim(-1, 20)

plt.legend()
plt.grid(True)
#plt.savefig('coef_h_wo.png')  # guardo figura
plt.show()

