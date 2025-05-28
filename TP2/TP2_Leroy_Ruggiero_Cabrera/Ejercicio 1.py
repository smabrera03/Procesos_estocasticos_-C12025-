import numpy as np
import matplotlib.pyplot as plt

#cargamos las matrices generadas por Generar Matrices.py
Potencia = np.load("Potencia.npy")
Viento = np.load("Viento.npy")

t = np.linspace(start = 0, stop = 24, num = len(Potencia[0, :, 0]))
#array de tiempos


                                         ###Torre 1###
PT1_enero = Potencia[0, :, 0]
PT1_febrero = Potencia[1, :, 0]
PT1_marzo = Potencia[2, :, 0]
PT1_abril = Potencia[3, :, 0]
#Esto es, nos paramos en la primer realizacion de cada mes de la torre 1

plt.plot(t, PT1_enero, label='Enero')
plt.plot(t, PT1_febrero, label='Febrero')
plt.plot(t, PT1_marzo, label='Marzo')
plt.plot(t, PT1_abril, label='Abril')

plt.xlabel('Hora')
plt.xlim(0, 24)

plt.ylabel('Potencia[kW]')

plt.legend(loc = 'upper left')
plt.title('Potencia de la torre 1')
plt.grid(True)
#plt.show()
plt.savefig('Potencia de la torre 1')
plt.clf()
                                                  ###Torre 10###

PT10_enero = Potencia[0, :, 9]
PT10_febrero = Potencia[1, :, 9]
PT10_marzo = Potencia[2, :, 9]
PT10_abril = Potencia[3, :, 9]

plt.plot(t, PT10_enero, label='Enero')
plt.plot(t, PT10_febrero, label='Febrero')
plt.plot(t, PT10_marzo, label='Marzo')
plt.plot(t, PT10_abril, label='Abril')

plt.xlabel('Hora')
plt.xlim(0, 24)

plt.ylabel('Potencia[kW]')

plt.title('Potencia de la torre 10')
plt.legend(loc = 'upper left')
plt.grid(True)
#plt.show()
plt.savefig('Potencia de la torre 10')
plt.clf()

                                                  ###Torre 20###
PT20_enero = Potencia[0, :, 19]
PT20_febrero = Potencia[1, :, 19]
PT20_marzo = Potencia[2, :, 19]
PT20_abril = Potencia[3, :, 19]

plt.plot(t, PT20_enero, label='Enero')
plt.plot(t, PT20_febrero, label='Febrero')
plt.plot(t, PT20_marzo, label='Marzo')
plt.plot(t, PT20_abril, label='Abril')

plt.xlabel('Hora')
plt.xlim(0, 24)

plt.ylabel('Potencia[kW]')

plt.title('Potencia de la torre 20')
plt.legend(loc = 'upper left')
plt.grid(True)
#plt.show()
plt.savefig('Potencia de la torre 20')
plt.clf()
#####################################################################################################################
#####################################################################################################################


#Estimamos un alfa por cada torre

                                  ###Torre 1###
PT1 = Potencia[0:4, :, 0] #Esto forma una matriz de 4x144 con las potencias de la torre uno entre enero y abril
PT1 = np.concatenate(PT1) #esto aplana el array, quedando un array de 4*144 = 576 elementos

VT1 = Viento[0:4, :, 0]
VT1 = np.concatenate(VT1)

alfa_T1 = np.divide(PT1, VT1**3, out=np.zeros_like(PT1), where = VT1!=0)#Esta linea hace el cociente elemento a elemento
#excepto en donde el denominador se anule
alfa_T1_estimado=np.mean(alfa_T1)
print(alfa_T1_estimado)
#esto da una estimación de alfa según los datos de la torre 1
#Repetimos para las otras 2 torres


                                        ###Torre 10###
PT10 = Potencia[0:4, :, 9]
PT10 = np.concatenate(PT10)

VT10 = Viento[0:4, :, 9]
VT10 = np.concatenate(VT10)

alfa_T10 = np.divide(PT10, VT10**3, out=np.zeros_like(PT10), where = VT10!=0)
alfa_T10_estimado=np.mean(alfa_T10)
print(alfa_T10_estimado)

                                        ###Torre 20###

PT20 = Potencia[0:4, :, 19] 
PT20 = np.concatenate(PT20)

VT20 = Viento[0:4, :, 19]
VT20 = np.concatenate(VT20)

alfa_T20 = np.divide(PT20, VT20**3, out=np.zeros_like(PT20), where = VT20!=0)
alfa_T20_estimado=np.mean(alfa_T20)
print(alfa_T20_estimado)

#
#
#Para cada torre graficamos los resultados
#
#

                                        ###Torre 1###


VT1_enero = Viento[0, :, 0]
PT1_enero = Potencia[0, :, 0]
PT1_estimada = alfa_T1_estimado * VT1_enero**3

plt.plot(t, PT1_enero, label = 'Potencia')
plt.plot(t, PT1_estimada, linestyle = '--', label = 'Potencia estimada')
plt.plot(t, VT1_enero**3, label = 'Viento')

plt.xlabel('Hora')
plt.xlim(0, 24)

plt.ylabel(r'Potencia [kW], Viento [$\mathrm{(m/s)^3}$]')

plt.legend()
plt.title('Potencia, viento al cubo y potencia estimada de la Torre 1')
plt.grid(True)
#plt.show()
plt.savefig('Potencia y potencia estimada (T1)')
plt.clf()

                                           ###Torre 10###

VT10_enero = Viento[0, :, 9]
PT10_enero = Potencia[0, :, 9]
PT10_estimada = alfa_T10_estimado * VT10_enero**3

plt.plot(t, PT10_enero, label = 'Potencia')
plt.plot(t, PT10_estimada, linestyle = '--', label = 'Potencia estimada')
plt.plot(t, VT10_enero**3, label = 'Viento')

plt.xlabel('Hora')
plt.xlim(0, 24)

plt.ylabel(r'Potencia [kW], Viento [$\mathrm{(m/s)^3}$]')

plt.legend()
plt.title('Potencia, viento al cubo y potencia estimada de la torre 10')
plt.grid(True)
#plt.show()
plt.savefig('Potencia y potencia estimada (T10)')
plt.clf()

                                            ###Torre 20

VT20_enero = Viento[0, :, 19] 
PT20_enero = Potencia[0, :, 19]
PT20_estimada = alfa_T20_estimado * VT20_enero**3

plt.plot(t, PT10_enero, label = 'Potencia')
plt.plot(t, PT10_estimada, linestyle = '--', label = 'Potencia estimada')
plt.plot(t, VT10_enero**3, label = 'Viento al cubo')

plt.xlabel('Hora')
plt.xlim(0, 24)

plt.ylabel(r'Potencia [kW], Viento [$\mathrm{(m/s)^3}$]')

plt.legend()
plt.title('Potencia y potencia estimada de la torre 20')
plt.grid(True)
#plt.show()
plt.savefig('Potencia y potencia estimada (T20)')
plt.clf()