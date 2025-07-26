#include <iostream>
#include <stdlib.h>
#include "latticeview.h"
#include <fstream>

#define ImageWidth 1000
#define ImageHeight 1000

using namespace std;

int main()
{

	int N = 64;  //tamanho da configuracao  16,32,64,128
	double pi;  //numero aleatorio para gerar uma configuracao aleatoriamente
	int lat[N*N];  //matriz da configuracao
	int N_2 = 0;  //numero de lugares a queimar (ou seja com valor 2)
	int paragem;  //variavel que indica quando o fogo chega ao outro lado
	int caminho_curto;  //soma dos numeros de passos dos caminho mais curtos das amostras em que ha percolacao
	int tempo_queima;  //soma dos numeros de passos necessarios que o codigo faz para queimar tudo das amostras em que ha percolacao
	int Amostras = 1000;  //numero de amostras
	int contagem;  //numero de passos ate atingir o outro lado
	int caminho_medio;  //caminho mais curto medio das amostras
	int percolacao;  //numero de casos em que houve percolacao dentro do total das Amostras
	int tempo_medio;  //numero medio de passos que o codigo da queima faz para queimar tudo no total das Amostras
	double probabilidade_percolacao;  //probabilidade de percolacao
	int contagem_total;  //numero total de passos do codigo da queima

	ofstream datafile1;
	ofstream datafile2;
	ofstream datafile3;

	datafile1.open("CM10.txt");
	datafile2.open("TM10.txt");
	datafile3.open("PP10.txt");

	//ciclo for para diferentes probabilidades de ocupacao
	for (double p = 0.400; p <= 0.700; p += 0.001)
	{
		caminho_medio = 0;
		probabilidade_percolacao = 0;
		tempo_medio = 0;
		caminho_curto = 0;
		tempo_queima = 0;
		percolacao = 0;

		//ciclo das Amostras
		for (int a = 1; a <= Amostras; a++)
		{
			paragem = 0;  //Em cada amostra paragem tem de ser 0
			contagem = 0;  //O mesmo para contagem
			contagem_total = 0;

			//Gerador de lugares
			for (int i = 0; i < N*N; i++)
			{
				pi = drand48();

				if (pi < p)
				{
					lat[i] = 1;
				}

				else
				{
					lat[i] = 0;
				}
			}

			//Queimar a primeira linha
			for (int j = 0; j < N; j++)
			{

				if (lat[j] == 1)
				{
					lat[j] = 2;
					N_2++;
				}

			}

			contagem = contagem + 1;

			//Queimar os vizinhos
			while (N_2 > 0)
			{

				for (int k = 0; k < N*N; k++)
				{

					if (lat[k] == 1)
					{

						//Comparar com os da esquerda
						if (k % N != 0)
						{
							if (lat[k - 1] == 2)
							{
								lat[k] = 4;
							}
						}

						//Comparar com os da direita
						if (k % N != N - 1)
						{
							if (lat[k + 1] == 2)
							{
								lat[k] = 4;
							}
						}

						//Comparar com o de baixo
						if (k >= N)
						{
							if (lat[k - N] == 2)
							{
								lat[k] = 4;
							}
						}

						//Comparar com o de cima
						if (k < N*N - N)
						{
							if (lat[k + N] == 2)
							{
								lat[k] = 4;
							}
						}

					}
				}

				//Passar as celulas com valor 2 a 3 e as celulas com valor 4 a 2
				for (int h = 0; h < N*N; h++)
				{
					if (lat[h] == 2)
					{
						lat[h] = 3;
						N_2--;
					}

					if (lat[h] == 4)
					{
						lat[h] = 2;
						N_2++;
					}
				}

				//verificaçao se chegou ao outro lado. Este ciclo para se paragem for 1
				for (int m = N*N - N; m < N*N && paragem == 0; m++)
				{
					if (lat[m] == 2)
					{
						paragem = 1;
					}
				}

				//Enquanto nao chegar ao outro lado paragem sera 0 e acrescenta-se um incremento a contagem
				if (paragem == 0)
				{
					contagem = contagem + 1;
				}

				contagem_total = contagem_total + 1;

			}

			//Se paragem for alguma vez 1 entao caminho_curto toma o valor de contagem e percolacao incrementa mais um
			if (paragem == 1)
			{
				percolacao = percolacao + 1;  //numero total de casos em que ha percolacao
				caminho_curto = caminho_curto + contagem + 1;  //numero de passos ate o fogo chegar ao outro lado mais um passo pois contagem pára quando paragem = 1
				tempo_queima = tempo_queima + contagem_total;
			}

		}

		probabilidade_percolacao = (double)percolacao / (double)Amostras;

		//Se nao houver amostras com percolacao o caminho medio e tempo medio sao zero
		if (percolacao != 0)
		{
			caminho_medio = caminho_curto / percolacao;
			tempo_medio = tempo_queima / percolacao;
		}
		else
		{
			caminho_medio = 0;
			tempo_medio = 0;
		}

		datafile1 << p << "\t" << caminho_medio << endl;
		datafile2 << p << "\t" << tempo_medio << endl;
		datafile3 << p << "\t" << probabilidade_percolacao << endl;

	}

	datafile1.close();
	datafile2.close();
	datafile3.close();


	return 0;
}
