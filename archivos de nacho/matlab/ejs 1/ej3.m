% Sea un sistema FIR h(n) definido en base a los siguientes coeficientes:
% h = {4, 3, 3.5, 4, 3, 2.5, 0.5, 0.3, 0.2}
% 1. Graficar la respuesta impulsiva y el módulo de la respuesta en frecuencia del
% sistema h(n). Considere una cantidad de puntos de la FFT adecuada para una
% mejor interpolación del gráfico en frecuencia.
% 2. Graficar polos y ceros de h(n).
% 3. Considere ahora una secuencia x(n) = square(2*pi*0.02*n), de largo M=100,
% como entrada del sistema LTI del punto anterior. Calcule la salida y(n) y grafique
% su respuesta en tiempo y en frecuencia. Nota: para calcular la salida utilice tanto
% conv() como filter()

clear all;
h = [4 3 3.5 4 3 2.5 0.5 0.3 0.2];
figure
stem(h)
legend('rta al impulso');

tam = 100;

Y = fft(h, tam);
n = linspace(0,2*pi,tam);

figure
plot(n,abs(Y),'o-');

% Y/X = 4 + 3Z^-1 + 3.5 Z^-2

zplane(h, 1);


%sys = tf(fliplr(h),1)
t = linspace(0,100);
x = square(2*pi*0.02*t);

y=filter(h,1,x);

figure
stem(t,y);


k=conv(x,h);
figure
stem(k)
