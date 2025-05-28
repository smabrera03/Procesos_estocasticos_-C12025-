clear console;
clear all;
close all;
% Parámetros
N = 400; % Longitud de la señal
num_realizaciones = 20; % Número de realizaciones
mu = 1; % Media de la distribución normal
sigma = sqrt(0.16); % Desviación estándar
omega_0 = 0.015 * pi; % Frecuencia angular

% Inicializar matriz para almacenar realizaciones
X = zeros(num_realizaciones, N);

% Generar realizaciones
for i = 1:num_realizaciones
    A = normrnd(mu, sigma); % Generar A de la distribución normal
    n = 0:N-1; % Vector de n
    X(i, :) = A * cos(omega_0 * n); % Calcular X(n)
end

% Graficar las realizaciones
figure;
hold on;
for i = 1:num_realizaciones
    plot(X(i, :)); % Graficar cada realización
end
hold off;

title('20 Realizaciones de X(n) = A cos(\omega_0 n)');
xlabel('n');
ylabel('X(n)');
grid on;




