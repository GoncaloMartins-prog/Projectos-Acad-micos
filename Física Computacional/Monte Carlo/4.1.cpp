#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include<cmath>

using namespace std;

int main()
{
	long long int N = 100000; // numero de pontos
	long long int Nc = 0; // numero de pontos que se encontram dento do semicirculo
	double x; // coordenada do eixo x
	double y; // coordenada do eixo y
	double pi_actual; // valor do pi actual
	double pi[N]; // vector que guarda o valor de pi para cada ponto gerado
	double log10_delta[N]; // vector que guarda o valor  do log10 do erro de pi para cada ponto gerado
	double delta; // valor do erro de pi no ciclo actual
	double distancia = 0; // distacia ah origem no ponto(x,y)
	long long int amostras = 10000; // numero de vezes que calculamos o pi e o seu erro
	double PI; // constante para definir o valor verdadeiro de pi

	ofstream file;
	ofstream file2;

	PI = 4.0 * atan(1.0); // define o valor  verdadeiro de pi

	// inicia os vectores
	for (int b = 0; b < N; b++)
	{
		pi[b] = 0;
		log10_delta[b] = 0;
	}

	file.open("log_delta_Amostras_100000.txt");
	file2.open("valores_pi_Amostras_100000.txt");

	//ciclo que faz varias amostras para N pontos
	for (int a = 1; a <= amostras; a++)
	{
		Nc = 0;
		for (long long int i = 0; i < N; i++)
		{
			x = drand48(); // gera um numero aleatorio para x
			y = drand48(); // gera um numero aleatorio para y
			distancia = sqrt(pow(x, 2) + pow(y, 2));

			if (distancia <= 1)
			{
				Nc++;
			}

			pi_actual = 4.0 * (double)Nc / ((double)(i + 1));
			pi[i] = pi[i] + pi_actual;
			delta = (PI - pi_actual);
			log10_delta[i] = log10_delta[i] + log10(sqrt(delta * delta));
		}
	}

	//ciclo para escrever nos ficheiros
	for (int c = 0; c < N; c++)
	{
		pi[c] = pi[c] / (double)amostras;
		log10_delta[c] = log10_delta[c] / (double)amostras;

		file << log10((double)(c + 1)) << "\t" << setprecision(6) << log10_delta[c] << endl;
		file2 << c + 1 << "\t" << setprecision(6) << pi[c] << endl;
	}

	file.close();
	file2.close();

	return 0;
}
