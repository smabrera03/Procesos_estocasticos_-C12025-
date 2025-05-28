clear console;
clear all;
close all;
% Parámetros
N = 400; % Longitud de la señal
num_realizaciones = 2000; % Número de realizaciones
A = 1; % Amplitud
omega_0 = 0.015 * pi; % Frecuencia angular

% Inicializar matriz para almacenar realizaciones
X = zeros(num_realizaciones, N);

% Generar realizaciones
for i = 1:num_realizaciones
    Theta = unifrnd(0, 2*pi); % Generar Theta de la distribución uniforme
    n = 0:N-1; % Vector de n
    X(i, :) = A * cos(omega_0 * n + Theta); % Calcular X(n)
end

% Graficar las realizaciones
figure;
hold on;
for i = 1:num_realizaciones
    plot(X(i, :)); % Graficar cada realización
end
hold off;

title('20 Realizaciones de X(n) = A cos(\omega_0 n + \Theta)');
xlabel('n');
ylabel('X(n)');
grid on;



figure;hold on;
plot(mean(X), 'LineWidth', 2);
plot(var(X),'LineWidth', 2);hold off;

