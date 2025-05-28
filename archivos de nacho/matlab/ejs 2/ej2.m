% Sea x una variable aleatoria exponencial, X ? Exp(?), de par�metro ? = 0.5 
% 1. Genere N = 104 muestras de X (usando el m�todo de transformaci�n inversa). 
% 2. Estime la media y la varianza muestrales de X y comparelas con las te�ricas (? = 1/?, ?2 = 1/?2).
% 3. Construya el histograma de las muestras de X. Normalice el histograma
% para que tenga �rea 1. Compare la funci�n obtenida con la funci�n de
% densidad de probabilidad te�rica.
clear all;
lambda=0.5;
bins=50;
num=10000;
%x_real = exprnd(0.5,1,num);%exponencial real, 104 tiradas (mu,1,N)

u = rand(1,num);%uniforme

x_simu = - log(1-u)/lambda;


% figure;
% histogram(x_simu,bins,"normalization","pdf");

disp("var teo = 4");
disp("med teo = 2");

disp("med ="+  mean(x_simu));
disp("var ="+ var(x_simu));


lin = linspace(min(x_simu),max(x_simu),num);
f = exppdf(lin, 1/lambda);

figure;
histogram(x_simu,bins,"normalization","pdf");
hold on;
plot(lin, f); % Grafica la real encima