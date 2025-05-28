clear all; close all; clc;
%% Ejercicio 1
%Pseudo-codigo:
% 1- Extraemos los tiempos entre arribos del archivo csv y damos formato.
% 2- Generamos un vector desplazado en una posicision Arribos_corrido.
% 3- Hacemos la diferencia entre ambos vectores para obtener un vector con
% el tiempo entre arribos Tiempo_entre_arribos y pasamos el tiempo a
% segundos.
% 4- Computamos la media y varianza muestral del vector
% Tiempo_entre_arribos.
% 5- Generamos el histograma del tiempo entre arribos a partir del vector
% y lo normalizamos a area unitaria.
% 6- Con las estimaciones de la media generamos la pdf teorica de la
% exponencial y la superponemos junto al histograma.


disp("Ejercicio 1");
% Obtencion y formateo de datos
A = readtable("geiger.csv"); %tiempo en microsegundos de cada arribo
Arribos = A.T; % los tiempos de arribos como vector fila
ArribosT = transpose(Arribos); % vector columna

Arribos_corrido = transpose([ 0 , ArribosT(1:end-1)]); % movemos uno para abajo y sacamos el último

%buscamos el tiempo entre cada arribo por lo que hacemos la diferencia
Tiempo_entre_arribos =(Arribos - Arribos_corrido)*10^-6; %el tiempo entre arribos en microsegundos, lo escalamos * 10^-6

%libero memoria
clear B; 

% a. media y varianza
media_tiempos_exp = mean(Tiempo_entre_arribos); % media muestral
varianza_tiempos_exp = var(Tiempo_entre_arribos); % varianza muestral
disp("Media muestral tiempo entre arribos = ");
disp(media_tiempos_exp);
disp("Varianza muestral tiempo entre arribos = ");
disp(varianza_tiempos_exp);

% b. Histograma
figure;
histogram(Tiempo_entre_arribos, 100, "normalization","pdf"); 
hold on;

% Generamos la pdf teorica exponencial
t = linspace(0, max(Tiempo_entre_arribos)+1, 1000); %Vector de tiempos
E = exppdf(t, media_tiempos_exp); % la función usa la media directamente, no lambda
plot(t, E, 'LineWidth', 1.5);
ylim([0, 1.25]); 
xlim([-0.55, 8]);  
ax = gca; % Get current axes
ax.YAxisLocation = 'origin'; % Set y-axis location to right
legend('Histograma','PDF teórica')
xlabel('Tiempo [s]');  % Label for the x-axis
%print(gcf, 'figExp.png','-dpng', '-r300');
hold off;

%libero memoria
clear t; 
clear E;
clear ax;
clear ArribosT;

%% Ejercicio 2
%Pseudo-codigo:
% 1- Pasamos el tiempo de cada arribo a segundos.
% 2- Definimos un segmento de tiempo de 2 segundos y creamos intervalos de
% 2 en 2 segundos para contar la cantidad de eventos contenida en cada
% intervalo.
% 3- Contabilizamos la cantidad de eventos por intervalo
% para obtener realizaciones de la variable aleatoria de la cantidad de
% eventos en un intervalo de 2 segundos (Vector_arribos).
% 4- Calculamos la media y varianza muestrales de los experimentos
% obtenidos.
% 5- Generamos el histograma de la cantidad de eventos por intervalo de 2
% segundos y lo normalizamos a area unitaria
% 6- Con las estimaciones de la media generamos la pmf teorica de la
% poisson y la superponemos junto al histograma.

disp("Ejercicio 2");

t = Arribos*10^-6; %tiempo de cada arribo en segundos

% Definir la duración del segmento
duracion_segmento = 2; % 2 segundos
% Generamos intervalos de tiempo de 2 en 2 segundos de 0 hasta 
% el tiempo maximo
limites = 0:duracion_segmento:max(t); % Intervalos de 2 en 2 de 0 a 10

% Contabilizamos la cantidad de elementos en cada intervalo
Vector_arribos = histcounts(t, limites);

%cada columna del vector Vector_arribos debería contener una realización de
%la variable aleatoria que cuenta los arribos en 2 segundos. 

%Libero memoria
clear A;
clear count;
clear duracion_segmento
clear index;
clear t;
clear tiempo;
clear Tiempo_entre_arribos;
clear x;

% Calculo de media y varianza de las realizaciones
media_arribos_poiss = mean(Vector_arribos);
varianza_arribos_poiss = var(Vector_arribos);
disp("Media muestral cantidad de arribos = ");
disp(media_arribos_poiss);
disp("Varianza muestral cantidad de arribos = ");
disp(varianza_arribos_poiss);

% histograma
figure;
hold on;
histogram(Vector_arribos,'BinMethod', 'integers',"normalization", "pdf"); % O ajusta el número de bins

% Generamos la pmf teorica poisson
T = 0:1:9;
E = poisspdf(T, media_arribos_poiss);
stem(T,E,'LineWidth',1.5);
legend('Histograma','PDF teórica')
xlabel('Cantidad de eventos');  
%print(gcf, 'figPoiss.png','-dpng', '-r300');
hold off;


