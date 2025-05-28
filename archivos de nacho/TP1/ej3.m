%% Ejercicio 3
% Simulaci´on de lanzamiento de Dados
% Suponga un juego que consiste en el lanzamiento de dos dados en simult´aneo. Cuando los
% n´umeros de ambos dados sumen 7 u 11, se considera un punto. El objetivo es realizar un total
% de n lanzamientos, llam´emoslo turno, y contabilizar la cantidad puntos acumulados por turno.
% En este ejercicio estudiaremos la estad´?stica de esta jugada aplicando Monte Carlo para emular
% m´ultiples lanzamientos.
% (a) Suponiendo que tenemos dos dados no pesados (es decir que cada cara tiene la misma
% probabilidad de salir que las demas) considerando que un evento de ´exito ser´a cuando la
% suma de ambos dados d´e 7 u 11. Determine la probabilidad de ocurrencia de ese evento e
% indique qu´e tipo de distribuci´on lo modela adecuadamente.
% (b) Genere 10000 realizaciones que simulen un lanzamiento de dos dados con el que se eval´ue el
% evento de ´exito. Realice un histograma y comp´arelo con la funci´on de probabilidad te´orica
% de acuerdo a la distribuci´on propuesta en el ejercicio anterior.
% (c) Suponga que ahora deseamos saber el puntaje total en n lanzamientos (es decir, la cantidad
% de ´exitos por turno). Determine qu´e distribuci´on es adecuada para modelar el puntaje
% obtenido por turno y defina la expresi´on de su funci´on de probabilidad.
% (d) Genere 10000 realizaciones simulando en cada una n = 20 lanzamientos para contabilizar el
% puntaje en cada turno (de acuerdo a la variable aleatoria propuesta en el punto anterior).
% Realice un histograma y comp´arelo con la funci´on de probabilidad te´orica para dicha
% variable