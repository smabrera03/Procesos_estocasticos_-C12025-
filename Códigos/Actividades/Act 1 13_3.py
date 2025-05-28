import matplotlib.pyplot as plt
import numpy as np
import math as mat

N = 10 #largo
n = np.linspace(start=0, stop=N - 1, num=N) #eje de tiempo

x = np.sin(2*np.pi*0.2*n)

plt.stem(n, x)

plt.title('x(n)') #agregar título
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()

#me costó más de lo que me gustaría admitir
factor = 8 #este factor controla cuántas bochas agergo
X = np.fft.fft(x, factor*N)

plt.plot(np.abs(X), 'o-')
plt.xlabel('$k$')
plt.ylabel('$|X[k]|$')
plt.grid(True)
plt.show()

