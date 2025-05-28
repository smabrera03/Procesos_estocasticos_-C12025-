import numpy as np
import matplotlib.pyplot as plt
import random


# Crear el array mazo y mezclaro. Sacar la carta inicial
def crear_mazo(carta_inicial):
    numeros = np.arange(2, 11).astype(str)  # ['2', ..., '10']
    figuras = np.array(['J', 'Q', 'K', 'A'])
    valores = np.concatenate((numeros, figuras))
    mazo = list(valores) * 4  # 4 palos por carta
    mazo.remove(carta_inicial)
    random.shuffle(mazo) # Mezclo el mazo
    return mazo # Devuelvo el mazo sin la primer carta fijada y mezclado

# Convertir carta a valor numérico
def valor_carta(carta):
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'A':
        return 11  # inicialmente tratamos el As como 11
    else:
        return int(carta)
    
#Simular una ronda de la banca
def ronda_banca(carta_inicial):

    puntos = valor_carta(carta_inicial) #esta variable lleva la cuenta de los puntos de la ronda. En principio vale
    #lo que valga carta_inicial
    mazo = crear_mazo(carta_inicial) #se crea el mazo sin la carta inicial
    ases_once = 0 #esta variable lleva la cuenta de cuántos ases de valor 11 hay en la mano. Así, si la banca se excede
    #se puede cambiar el valor del as.

    while(1):

        carta_sacada = mazo.pop() #se saca una carta
        if(carta_sacada == 'A'):
            ases_once+=1 #si salió un as, se suma a ases_once

        puntos += valor_carta(carta_sacada) #se suman los puntos

        if(puntos > 21 and ases_once > 0): #si la banca se excedió y tenía un as de valor 11, es as pasa a valer 1 (se restan 10 puntos
            ases_once-=1
            puntos -= 10

        if(puntos > 21): #si la banca se excedió, devuelve True
            return True

        if(puntos >= 17): #si 17 <= puntos <= 21 la banca se planta
            return False

# Simular M rondas de la banca dada una carta inicial. Estimar la probabilidad de que la banca se exceda dada esa carta
def montecarlo_banca(M, carta_inicial):
  pasados = 0 #esta variable lleva la cuenta de cuántas veces se excedió la banca
  for i in range(M):
    if(ronda_banca(carta_inicial)):
      pasados += 1
  return pasados/M #se estima la probabilidad


realizaciones = [1,10,100,1000,10000,100000,1000000] #un array con los valores que va a tomar M
carta_inicial = '6' 
P_E = []
for i in range(len(realizaciones)):
  P_E.append(montecarlo_banca(realizaciones[i], carta_inicial))
print(P_E)

##############################
#Nota: el programama puede tardar un poco en finalizar
#############################

plt.stem(realizaciones, P_E)
plt.semilogx()
plt.xlabel('Realizaciones')
plt.ylabel('Probabilidad de que la banca se exceda')
plt.grid(True)
plt.show()