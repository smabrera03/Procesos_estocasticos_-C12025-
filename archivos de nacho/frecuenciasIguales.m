clear console;
clear all;
close all;
% Par�metros
N = 400; % Longitud de la se�al
num_realizaciones = 20; % N�mero de realizaciones
mu = 1; % Media de la distribuci�n normal
sigma = sqrt(0.16); % Desviaci�n est�ndar
omega_0 = 0.015 * pi; % Frecuencia angular

% Inicializar matriz para almacenar realizaciones
X = zeros(num_realizaciones, N);

% Generar realizaciones
for i = 1:num_realizaciones
    A = normrnd(mu, sigma); % Generar A de la distribuci�n normal
    n = 0:N-1; % Vector de n
    X(i, :) = A * cos(omega_0 * n); % Calcular X(n)
end

% Graficar las realizaciones
figure;
hold on;
for i = 1:num_realizaciones
    plot(X(i, :)); % Graficar cada realizaci�n
end
hold off;

title('20 Realizaciones de X(n) = A cos(\omega_0 n)');
xlabel('n');
ylabel('X(n)');
grid on;




