%% Ejercicio 1.c
% Desarrollo del ejercicio 1.c. 
close all

%%
% Definimos las varianzas y medias de cada una de las normales buscadas y
% aplicamos la transformación

% a) Xa ~ N(0,2)
varianza_a = 2;
media_a = 0;
Xa = sqrt(varianza_a)*Z1 + media_a;

subplot(3, 1, 1)
histogram(Xa,'Normalization','pdf')
hold on;
x = linspace(-5, 6, N);
f = normpdf(x, 0, sqrt(2));
plot(x, f);
title('Variable aleatoria X_a');
xlabel('x');
grid on;

% b) Xb ~ N(1, 2)
varianza_b = 2;
media_b = 1;
Xb = sqrt(varianza_b)*Z1 + media_b;

subplot(3, 1, 2)
histogram(Xb,'Normalization','pdf')
hold on;
x = linspace(-5, 7, N);
f = normpdf(x, 1, sqrt(2));
plot(x, f);
title('Variable aleatoria X_b');
xlabel('x');
grid on;

% c) Xc ~ N(1, 4)
varianza_c = 4;
media_c = 1;
Xc = sqrt(varianza_c)*Z1 + media_c;

subplot(3, 1, 3)
histogram(Xc,'Normalization','pdf')
hold on;
x = linspace(-7, 8, N);
f = normpdf(x, 1, 2);
plot(x, f);
title('Variable aleatoria X_c');
xlabel('x');
grid on;

