%% ej 2
clear all;
close all;

N=1;
M=25;
A = unifrnd(-2,-1,M,N);
t=linspace(0,30,100);


X=transpose(exp(A.*t));

Xm=mean(X,2); %la media para cada tiempo

figure;
plot(X);

figure;
plot(Xm);


figure;
K=xcorr(X,'biased');
stem(K);

%% ej 5.2
clear all;
close all;
M=1000;
N=25;
p=0.3;
B = binornd(1,p,M,N);
n = 0:N-1; % Vector de índices
X=(-1).^n  .*B;

 figure;
 hold on;
media_estimada=mean(X);
stem(media_estimada);
media_teorica = (-1).^n  .*p; %lacualda a mano
stem(media_teorica);
hold off;

%% ej 5.3
clear all;
close all;
N=1000;
M=5;
p1=0.5;
p2=0.1;
n = 0:N-1; % Vector de índices
X=zeros(N,M);

X(1)= binornd(1,0.5); %primer valor
for j = 1:M
    for k = 2:N
         if X(k-1,j) == 0
             X(k,j)= binornd(1,p1);
         end
         if X(k-1,j) == 0
             X(k,j)= binornd(1,p2);
         end 
    end
end

X=transpose(X);


 figure;
 n=1:1:N;
 hold on;
 stem(mean(X));
hold off;

%% unfirme 11

clear all;
close all;

varianza= 2;

U=unifrnd(-sqrt(3*varianza),sqrt(3*varianza),1,1000); %varianza unitaria

MU=mean(U);
VU=var(U);

X=filter([1 1],1,U);

MX=mean(X);
VX=var(X);
teoricaVX = 2*varianza;


% normal 11

N=normrnd(0,sqrt(varianza),1,1000); %varianza unitaria

MUN=mean(N);
VUN=var(N);

XN=filter([1 1],1,N);

MXN=mean(XN);
VXN=var(XN);
teoricaVXN = 2*varianza;

figure();
hold on
stem(X)
stem(XN)
hold off


