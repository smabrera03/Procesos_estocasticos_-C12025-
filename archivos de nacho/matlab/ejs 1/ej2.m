% 1. Defina la siguiente secuencia, de largo M=10, y luego graf�quela con stem:
% x(n) = sin(2? 0.2 n)
% 2. Calcule la FFT de dicha secuencia y grafique su m�dulo.
% Si bien la FFT es discreta, nos interesa como aproximaci�n de la transformada
% de Fourier, por lo cual, utilice plot para visualizarla como gr�fico de l�nea. Sin
% embargo, en este caso agregue la opci�n 'o-' (como tercer argumento) que
% permite agregar al gr�fico de l�neas un marcador para distinguir mejor los
% puntos del vector.
% 3. Repita el mismo ejemplo anterior pero aplicando zero padding en la FFT, para
% nfft = 20, 40 y 80
N=10;
M = 0:N-1;
X = sin(2* pi* 0.2 *M);
stem(M,X);

N=80;%zrro padding
Y = fft(X,N);
w = linspace(0,2*pi,N);

figure
plot(w,abs(Y),'o-')
legend('fft')
grid on;