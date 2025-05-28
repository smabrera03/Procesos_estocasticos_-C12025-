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

clear all;

img = imread('img_01.jpg');

img_gris = rgb2gray(img);
data = double(img_gris);

sizeData = size(data);%el tamaño de la imagen
rows=2;
cols=sizeData(2)*sizeData(1)/2;
img_out = reshape(data, [rows, cols]); % acá tenemos el vector correcto


scatter(img_out(1,:),img_out(2,:))

% queremos estimar la matriz de covarianza, usamos la función de cov
%Cx = cov(img_out(:,1),img_out(:,2));
Cx = cov(transpose(img_out));
% ahora veamos los autovalores y autovectores
[autovecs,autovals,V]=svd(Cx);

autovals

% definimos una matriz truncada de autovectores

Vtruc = autovecs(:,1); %1er col

ux = mean(img_out);
Yr = transpose(Vtruc)*(img_out-ux);% supestamentela proyección sobre la dirección del autovalor que tiene sentido conservar

Xr = Vtruc*Yr+ux; % supestamente llo reconstruido sin la info de ese autovalor chico


data_out = reshape(Xr,sizeData);

imshow(uint8(data_out))