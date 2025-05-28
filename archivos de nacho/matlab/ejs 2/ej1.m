%Genere N experimentos de una variable aleatoria Rayleigh con parámetro b = 0.5.
%Grafique su histograma para los siguientes parámetros:
%1. N = 100, bins = 10
%2. N = 100, bins = 30
%3. N = 10000, bins = 30

clear all;

bins = 10;
N=100;
b=0.5;
x = raylrnd(b, 1, N); % Rayleigh por tiradas

xmin = min(x);
xmax=max(x);

linea = linspace(xmin, xmax, N); % Dominio de la función
f = raylpdf(linea, b); % Función de densidad

figure;
histogram(x,bins,"normalization","pdf"); %histograma
hold on;
plot(linea, f); % Grafica la rayleigh real encima?


bins = 30;
N=100;
b=0.5;
x = raylrnd(b, 1, N); % Rayleigh por tiradas

xmin = min(x);
xmax=max(x);

linea = linspace(xmin, xmax, N); % Dominio de la función
f = raylpdf(linea, b); % Función de densidad

figure;
histogram(x,bins,"normalization","pdf"); %histograma
hold on;
plot(linea, f); % Grafica la rayleigh real encima?


bins = 30;
N=10000;
x = raylrnd(b, 1, N); % Rayleigh por tiradas

xmin = min(x);
xmax=max(x);

linea = linspace(xmin, xmax, N); % Dominio de la función
f = raylpdf(linea, b); % Función de densidad

figure;
histogram(x,bins,"normalization","pdf"); %histograma
hold on;
plot(linea, f); % Grafica la rayleigh real encima?


% con la uniforme
%1 - e^(-x^2 / 2b^2) donde despejamos x
% x = sqrrt(- ln(1-u)/2)

clear all;

%generemos var aleatoria con la uniforme
N=1000000;
b=0.5;
bins=10000;
u = rand(1,N);%la uniforme
x=sqrt(abs(-0.5*log(1-u)));%simu de rayleig
xmin = min(x);
xmax=max(x);

linea = linspace(xmin, xmax, N); % Dominio de la función
f = raylpdf(linea, b); % Función de densidad

figure;
histogram(x,bins,"normalization","pdf"); %histograma
hold on;
plot(linea, f); % Grafica la rayleigh real encima?
 