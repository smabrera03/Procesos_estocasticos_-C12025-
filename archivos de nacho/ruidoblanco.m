clear console;
clear all;
close all;
% Par�metros
N = 100; % Longitud de cada realizaci�n
num_realizaciones = 2000; % N�mero de realizaciones
mu = 0; % Media de la distribuci�n normal
sigma = sqrt(2); % Desviaci�n est�ndar (ra�z de la varianza)

% Inicializar la matriz para X(n)
X = normrnd(mu, sigma, [num_realizaciones, N]); % Muestras de X(n)

% Inicializar la matriz para Y(n)
Y = zeros(num_realizaciones, N); % Crear matriz para Y(n)

% Calcular Y(n) para cada realizaci�n
for r = 1:num_realizaciones
    for n = 2:N
        Y(r, n) = 0.5 * X(r, n) + 0.75 * X(r, n-1); % F�rmula para Y(n)
    end
end

% Mostrar resultados de una realizaci�n
disp('Una realizaci�n del proceso Y(n):');
disp(Y(1, :));

% Opcional: Graficar la primera realizaci�n de Y(n)
figure;
plot(Y(1, :), 'r-o');
title('Primera Realizaci�n del Proceso Y(n)');
xlabel('n');
ylabel('Y(n)');
grid on;

% la media anl�tica es cero por simple inspecci�n, es Comb lineal de cosas
% de media cero aparte.

% la varianza va a ser (0.5*0.5+0.75*0.75 )* 2 = 13/8 = 1.6250

%Es ESA

My=mean(Y)
Vy=var(Y)

correl = xcorr(Y);
mean(correl)

figure;
hold on;
plot(correl);
plot(mean(correl));
hold off;


