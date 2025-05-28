clear console;
clear all;
close all;
p=0.5;
realizaciones= 200;
long=200;
a=rand(realizaciones, long);
z = a < p;

x= 2*z-1;
y = cumsum( x ,2); % p= 0.5

media = mean(y);
varianza= var(y);


n=linspace(0,long,long+1);
media_teo = n*(2*p - 1);

var_teo=4*n*p*(1-p);

figure;
hold on;
plot(media_teo,'LineWidth', 2);
plot(transpose(y));
legend('media te�rica','caminata');
hold off;

figure;
hold on;
plot(media_teo,'LineWidth', 2);
plot(media);
legend('media te�rica','media estimada');
hold off;


figure;
hold on;
plot(var_teo,'LineWidth', 2);
plot(varianza);
legend('var te�rica','var estimada');
hold off;
