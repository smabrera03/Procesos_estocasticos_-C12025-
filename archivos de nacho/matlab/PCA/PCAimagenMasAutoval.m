% Para la imagen img_01.png provista en el campus, defina realizaciones de un vector
% X = [X1, X2]T seleccionando cada par de píxeles contiguos en la imagen (ver esquema en
% siguiente filmina)
% 1.
% Haga un gráfico de dispersión del vector X.
% 2.
% Estime la matriz de covarianza de X y compute las proyecciones Y en las direcciones
% principales. Haga un gráfico de dispersión de Y. Determine cuál de las componentes
% puede ser descartada.
% 3.
% Defina la matriz de proyección V que descarta el autovector asociado al menor
% autovalor. Obtenga la proyección YR de X en ese espacio reducido.
% 4.
% Reconstruya el conjunto de vectores XR con la transformación inversa.
% 5.
% Rearme la imagen a partir de los vectores reconstruidos y grafíquela

clear all;clc;close all

img = imread('img_01.jpg');

img_gris = rgb2gray(img);
data = single(img_gris);
sizeData = size(data);%el tamaño de la imagen
rows=8; % acá le das la cant de VA aleatorias, siempre se queda con 1
cols=sizeData(2)*sizeData(1)/rows;
img_out = transpose(reshape(data, [rows, cols])); % acá tenemos el vector correcto, lo trasnpongo para ver que recibe la función de cov

clear img
clear img_gris
clear data

% queremos estimar la matriz de covarianza, Matlab toma la # de columnas
% como la # de variables aleatorias, que te va a dar la dimensión de la
% matriz de covarianza
Cx = cov(img_out); 

% ahora veamos los autovalores y autovectores
[autovecs,autovals,V]=svd(Cx);

% definimos una matriz truncada de autovectores

Vtruc = autovecs(:,1); %1er col

ux = mean(img_out);

aux = transpose(img_out-ux);
Yr = transpose(Vtruc)*aux;% supestamentela proyección sobre la dirección del autovalor que tiene sentido conservar
clear aux;
Xr = Vtruc * Yr + transpose(ux); % supestamente lo reconstruido sin la info de ese autovalor chico


data_out = reshape(Xr,sizeData);

imshow(uint8(data_out)) % acá le saqué el 75% de la info