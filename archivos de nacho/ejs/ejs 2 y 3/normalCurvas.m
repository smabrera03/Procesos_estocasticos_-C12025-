clear all;

N=10^3; % realizaciones
mean = [1; -2]; % media
Cx = [2 1;1 1]; % matriz de covarianza

A = mvnrnd(mean,Cx,N); % simulamos la multivariable

figure;
scatter(A(:,1),A(:,2)); % la ploteamos



x = linspace(-10,10,N); % generar N puntos entre xmin y xmax
y = linspace(-10,10,N); % generar N puntos entre ymin e ymax
[XX, YY] = meshgrid(x,y); % matrices de puntos para x e y

Z = fz(XX,YY);

figure;
contour(XX,YY,fz(XX,YY),10);

function Z = fz(x,y)  
    Z = -0.5.*x.*x +x.*(y-3)-y.*y-5.*y-13/2;
end