% Para la imagen img_01.png provista en el campus, defina realizaciones de un vector
% X = [X1, X2]T seleccionando cada par de p�xeles contiguos en la imagen (ver esquema en
% siguiente filmina)
% 1.
% Haga un gr�fico de dispersi�n del vector X.
% 2.
% Estime la matriz de covarianza de X y compute las proyecciones Y en las direcciones
% principales. Haga un gr�fico de dispersi�n de Y. Determine cu�l de las componentes
% puede ser descartada.
% 3.
% Defina la matriz de proyecci�n V que descarta el autovector asociado al menor
% autovalor. Obtenga la proyecci�n YR de X en ese espacio reducido.
% 4.
% Reconstruya el conjunto de vectores XR con la transformaci�n inversa.
% 5.
% Rearme la imagen a partir de los vectores reconstruidos y graf�quela

clear all;

img = imread('img_01.jpg');

img_gris = rgb2gray(img);
data = double(img_gris);

sizeData = size(data);%el tama�o de la imagen
rows=2;
cols=sizeData(2)*sizeData(1)/2;
img_out = reshape(data, [rows, cols]); % ac� tenemos el vector correcto


scatter(img_out(1,:),img_out(2,:))

% queremos estimar la matriz de covarianza, usamos la funci�n de cov
%Cx = cov(img_out(:,1),img_out(:,2));
Cx = cov(transpose(img_out));
% ahora veamos los autovalores y autovectores
[autovecs,autovals,V]=svd(Cx);

autovals

% definimos una matriz truncada de autovectores

Vtruc = autovecs(:,1); %1er col

ux = mean(img_out);
Yr = transpose(Vtruc)*(img_out-ux);% supestamentela proyecci�n sobre la direcci�n del autovalor que tiene sentido conservar

Xr = Vtruc*Yr+ux; % supestamente llo reconstruido sin la info de ese autovalor chico


data_out = reshape(Xr,sizeData);

imshow(uint8(data_out))