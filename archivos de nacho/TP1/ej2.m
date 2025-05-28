clc; clearvars;close;
rng(1);

%% Definiciones
%Parametros de la distribucion normal 
mu = 2; %media
sigma = square(3); %desviacion estandar

%Cantidad de experimentos
N = 10000;

%% Punto a 
% P(mu-sigma < X <  mu+sigma) 
P = prob_normal(mu, sigma, mu-sigma, mu+sigma, N, 1);
fprintf("Punto a P = %f \n", P);

%% Punto b 
% P(mu-2sigma < X <  mu+2sigma) 
P = prob_normal(mu, sigma, mu-2*sigma, mu+2*sigma, N, 1);
fprintf("Punto b P = %f \n", P);

%% Punto c 
% P(mu-3sigma < X <  mu+3sigma) 
P = prob_normal(mu, sigma, mu-3*sigma, mu+3*sigma, N, 1);
fprintf("Punto c P = %f \n", P);


%% Punto d
% Recalculo inciso Punto a para distintos valores de N
disp("Punto d");
N_vect = 10.^(1:1:6);   %vector con los posibles valores de N 

for i = 1:length(N_vect)
    P = prob_normal(mu, sigma, mu-sigma, mu+sigma, N_vect(i), 1);
    fprintf("Para N = %e -> P = %f \n", N_vect(i), P);
end

%Defino el valor de referencia 
I = 0.682687273250961;

%Hago M realizaciones de la integral
M = 50;                             %veces a calcular las integrales  
MSE_vect = zeros(1, length(N_vect));  %vector donde guardar los MSE

%Calculo para cada N 
for i = 1:length(N_vect)
    I_N = prob_normal(mu, sigma, mu-sigma, mu+sigma, N_vect(i), M); %Computo las M integrales
    MSE_vect(i) = mean(power(I_N-I, 2));                            %Computo el MSE con los M resultados anteriores
end

figure;
stem((1:1:length(N_vect)), MSE_vect, "LineWidth", 3);
grid;
xlabel("Cantidad de muestras (en potencias de 10)");
ylabel("MSE");
    
%% Defino una funcion para computar las probabilidades
% P(a < X < b) 
function P = prob_normal(mu, sigma, a, b, N, M)
    U = unifrnd(a, b, N, M);    %genero M VeAs columna de N VAs uniformes(a, b)(filas) cada uno 
    fx = normpdf(U, mu, sigma); %evaluo en la funcion a integrar
    %nota: mean() calcula la media de cada columna de la si fx es matriz
    P = (b-a)*mean(fx);         %Computo la probabilidad con LGN
end
