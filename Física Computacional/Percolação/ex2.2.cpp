#include<iostream>
#include<stdlib.h>
#include "latticeview.h"
#include <fstream>
#include<cmath>
#include <time.h>

#define ImageWidth 1000
#define ImageHeight 1000

using namespace std;

main()
{
	int N = 32;
	int lat[N*N];
	double p = 0.5;// p=0.6
	double pi; //numero aleatorio para gerar uma configuracao aleatoriamente
	int caminho_curto = 0; // passos para o caminho mais curto
	int N_2 =0; // numero de lugares a queimar ( vao tomar o valor 2)
	int tempo_total = 0; // numero total de passos de tempo ate o fogo parar completamente
	int sitio = 0; // variavel que guarda o lugar da ultima linha de configuração onde o fogo chega 1º
	int paragem =0; // variavel que indica quando o fogo chega ao outro lado
	int contagem =0; // incrementa quando a variavel paragem for igual a 0 e igual a 1
	
	srand(time(NULL));// origina valores aleatorios novos sempre  que o programa eh executado
	
		// gera a rede(lugares)
		for(int icounter=0; icounter<N*N; icounter++)
		{
			pi=(double)rand()/(double)(RAND_MAX);
		
			if(pi < p)
			{
				lat[icounter]=1;
			}

			else
			{
				lat[icounter]=0;
			}

		}

		// queimar a 1º linha
		for( int jcounter=0; jcounter<N; jcounter++)
		{
			if(lat[jcounter] ==1)
			{
				lat[jcounter] = 2;
				N_2++;
			}
	
		}

		contagem = contagem +1;
	
		// queimar vizinhos
		while(N_2 > 0)
		{
			for(int k =0; k < N*N; k++)
			{
				if(lat[k]==1)
				{
					//compara com o vizinho a esquerda
					if(k%N != 0)
					{
						if(lat[k - 1] ==2)
						{
							lat[k]=4;
						}
					}

				
					// compara com o vizinho a direita
					if(k% N != N-1)
					{
						if(lat[k + 1]==2)
						{
							lat[k]=4;
						}
					}
				
				
					//compara com o vizinho a baixo
					if(k >= N)
					{
						if(lat[k - N]==2)
						{
							lat[k]=4;
						}
					}

					//compara com o vizinho a cima
				 	if(k < N*N - N)
					{
						if(lat[k + N]==2)
						{
							lat[k]=4;
						}
					}

				}
			}
			// Celulas com valor 2 passam a 3 e de valor 4 passam a 2
			for(int h=0; h < N*N;h++)
			{
				if(lat[h]==2)
				{
					lat[h]=3;
					N_2--;
				}
				if(lat[h]==4)
				{
					lat[h]=2;
					N_2++;
				}

			}
			// verificar se chegou ao outro lado. O ciclo para se a paragem for 1
			for(int m=N*N - N;m < N*N and paragem == 0;m++)
			{
				if(lat[m] == 2)
				{
					paragem = 1;
					m = sitio;
				}
			}
	
			//Incremetacao da variavel contagem
			if(paragem ==0)
			{
				contagem = contagem +1;
			}
	
			if(paragem==1 && caminho_curto ==0)
			{
				caminho_curto= contagem +1;
				Print_lattice(lat, N, N, ImageWidth, ImageHeight, "Caminho Curto.ppm");
			}

			tempo_total = tempo_total + 1;
		}

	cout <<caminho_curto <<"\t" <<tempo_total <<endl;
	
	Print_lattice(lat, N, N, ImageWidth, ImageHeight, "Metodo da Queima_p=0.5.ppm");
	
	return 0;
}
