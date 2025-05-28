% Genere N = 200 muestras para definir los siguientes vectores aleatorios.:
% 1. Para el vector U = [U1;U2]T , genere dos variables Rayleigh, U1~ U(0;2) y U2~ U(0;3).
% 
% 2. Para el vector X = [X1 X2]T genere muestras de las variables X1 y X2 a partir de U1 y U2, 
% tal que X1 = 0.5 U1– 0.3 U2 y X2 = 0.7 U1+ 0.2 U2
% 
% 
% 3. Para el vector Y = [Y1 Y2]T , genere muestras de las variables Y1 y Y2 a partir de U1
% y U2, tal que Y1 = 1.2 U1 – 0.1 U2 y Y2 = U1 + 0.1 U2
% 
% Haga el gráfico de dispersión (ej: scatter(u1, u2)) y calcule el coeficiente de correlación
% para cada uno de casos.
% Nota: defina el límite de los ejes del gráfico con axis([-1 3 -1 3] ).

clear all;
n=100000
U_1 = unifrnd(0,2,[1,n]);
U_2 = unifrnd(0,3,[1,n]);

U = [U_1 ; U_2]; %vector uniforme

X1=0.5*U_1 - 0.3*U_2 ;
X2= 0.7*U_1+0.2*U_2;

X = [X1;X2];

Y1=1.2*U_1 - 0.1*U_2;
Y2= U_1+0.1*U_2;

Y = [Y1;Y2];

figure;
scatter(U_1,U_2);
axis([-1 3 -1 3] )

figure;
scatter(X1,X2);
axis([-1 3 -1 3] )

figure;
scatter(Y1,Y2);
axis([-1 3 -1 3] )

corrcoef(U_1,U_2)

corrcoef(X1,X2)

corrcoef(Y1,Y2)
