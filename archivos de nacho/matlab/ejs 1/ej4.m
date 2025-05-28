% Sea un sistema IIR h(n) definido en base a los siguientes coeficientes:
% b = {3, 1.5, 2} a = {1 -0.6}
% 1. Graficar el módulo de la respuesta en frecuencia del sistema h(n) utilizando la
% función freqz(). Considere una cantidad de puntos de la variable ? para una mejor
% interpolación del gráfico en frecuencia.
% 2. Graficar polos y ceros de h(n).
% 3. Utilice la misma onda cuadrada de la actividad anterior para obtener la salida del
% sistema LTI).
% 4. ¿Qué ocurre si los coeficientes del denominador ahora son a = {1 -1.2}? Repita los
% puntos anteriores y obtenga conclusiones.

b = [3 1.5 2];
a = [1 -0.6];

%sys = tf(b,a);
nfft = 10000;

figure
freqz(b,a,nfft);

figure
zplane(b,a);

t = linspace(0,100);
x = square(2*pi*0.02*t);

y=filter(b,a,x);

figure
stem(t,y);

%otros coefs

b = [3 1.5 2];
a = [1 -1.2];

%sys = tf(b,a);
nfft = 10000;

figure
freqz(b,a,nfft);

figure
zplane(b,a);

t = linspace(0,100);
x = square(2*pi*0.02*t);

y=filter(b,a,x);

figure
stem(t,y);

%ahora el filtro es bilateral y no es ni causal ni anticausal
