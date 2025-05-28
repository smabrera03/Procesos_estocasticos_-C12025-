% 1. Genere las siguientes secuencias para un largo de M=20
% x1
% (n) = sin(2? 0.1 n);
% x2
% (n) = sin(2? 0.05 n);
% x3
% (n) = sin(2? 0.02 n);
% x4
% (n) = x1
% (n) + x2
% (n) + x3
% (n)
% 2. Grafique todos los casos anteriores usando plot() y stem()


n=0:19;

x=sin(2*pi*0.1*n);
y=sin(2*pi*0.05*n);
z=sin(2*pi*0.02*n);
a=x+y+z;

figure
plot(n,x);

figure
plot(n,y);

figure
plot(n,a);

figure
stem(n,x);

figure
stem(n,y);

figure
stem(n,z);

figure
stem(n,a);