%% Ejercicio 3.a
clc; clearvars;close;
rng(42)
%% Parametros Generales. 
N = 10000;
p = 2/9;
n_bins =50;

%% Simulacion lanzamiento de 2 dados

d_1 = randi([1 6],1,N);
d_2 = randi([1 6],1,N);

sum = d_1 + d_2;
%if sum == 4 

r = binornd(ones(1,N),p);

%figure;
%histogram(r,n_bins,'Normalization','probability');
%% Funcion de probabilidad teorica
x = 0:1
b = binopdf(0:1, 1, p);
%figure;
%plot(x,b)
%bar(x,b)

%% 3.d
% 
y = binornd(20,p,[1 1000])
figure;
histogram(y,n_bins,'Normalization','pdf');

%% Funcion de probabilidad teorica
a = 0:20
c = binopdf(0:20, 20, p);
figure;
plot(a,c)
%bar(x,b)