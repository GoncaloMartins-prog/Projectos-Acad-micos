#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include <math.h>
#include "latticeview.h"

#define ImageWidth 1024
#define ImageHeight 1024

using namespace std;

int energia(int lat[], int L, int a);

int main()
{

	int L =600; // utilizar valores maiores que 100
	int N = L*L;// numero total de spins
	int lat[L*L];
	int J=1;
	int E_total=0;
	int E_inicial=0;
	int M_inicial=0;
	int M=0;
	int delta_E; //variacao da energia 
	int p_a;
	double T_max=5.0;// [0,5]
	double Kb=1.0;
	int x_a;
	int y_a;
	double p_flip;
	int amostras=3;
	int sum_M=0;
	int sum_E=0;
	double E_media;
	double M_media;
	double M_mediaquad;// quadrado da media
	double M_quad;// quadrado da magnetizacao
	double M_quad_t;
	double var; // variancia da magnetizacao
	int conta = 0;
	

	ofstream file;
	ofstream file2;
	ofstream file3;
	
	// rede com os spins todos orientados
	for( int a =0; a <L*L;a++)
	{
		lat[a]=1;
	}

	file.open("E_L600.txt");
	file2.open("M_L600.txt");
	file3.open("varM_L600.txt");
	
	for(double T=0.1; T <= T_max; T= T + 0.001)
	{
		sum_E=0;
		sum_M=0;
		M_quad=0;
		
		for(int n =1; n <= amostras; n++)
		{	

			/*
			Retirar este ciclo no 2º exercicio, pois queremos utilizar as disposicao anterior
			*/
			/*for (int a = 0; a < L*L; a++)
			{
				lat[a] = 1;
			}*/
			

			M = 0;
			E_total=0;
			for(int b=0; b<L*L;b++) 
			{
				M=M+lat[b];
				E_total=E_total +energia(lat,L,b);
				E_inicial= E_inicial + energia(lat,L,b);
				M_inicial = M_inicial + lat[b];
				M_quad = (M_quad + pow(M,2))/((double)amostras*N);
				
			}
	
			//Print_lattice(lat, L, L, ImageWidth, ImageHeight, "Estado_Inicial.ppm"); // tenho de ter imagem toda a vermelho
			//cout <<"Energia Inicial = " <<E_total <<endl;
			//cout <<"Magnetizacao Inicial = " <<M <<endl;

			for(int s=1;s<=3*L*L;s++) // L*L*3
			{
				p_a=rand() % N;
				delta_E= -2*J*energia(lat,L,p_a); // temos de colocar um - antes pois temos a função energia negativa
				//cout <<"Variacao Energia = " <<delta_E <<endl;
				//cout <<"valor de p_a = "<<p_a <<endl;
				
				// inversao dos spins
				if(delta_E<=0)
				{
					lat[p_a] = -1 * lat[p_a];
					E_total= E_total + delta_E;
					M = M + 2 * lat[p_a];
					M_quad = M_quad + pow(M,2);
			
				}
		
				else
				{
					p_flip = drand48();

					if( p_flip<exp(-(double)delta_E/(Kb*T)))
					{
						lat[p_a] = -1 * lat[p_a];
						E_total= E_total + delta_E;
						M = M + 2 * lat[p_a];
						M_quad = M_quad + pow(M,2);
					}
				}
				
				
				
				//cout <<p_flip <<"\t" <<exp(-(double)delta_E / (Kb * T)) <<endl;
				//cout <<"Energia final = " <<E_total <<endl;
				//cout <<"Magnetizacao final = " <<M <<endl;
				//Print_lattice(lat, L, L, ImageWidth, ImageHeight, "Estado_Final.ppm");
			}
			 
			
			sum_E = sum_E + E_total;
			sum_M = sum_M + M;
			M_quad_t = (M_quad_t + M_quad)/(3*N);
			

		}
		
		//cout << "temperatura=" << T << endl;  //apenas para ver quando é que muda de T
		//M_quad =pow((double)sum_M,2)/((double)amostras*N);
		//cout << M_quad<<endl;
		E_media = (double)sum_E/((double)amostras*N);// energia media por spin
		M_media = (double)sum_M /((double)amostras*N);// magnetização media por spin
		M_mediaquad = pow(M_media,2);
		//cout << M_mediaquad << endl;
		E_inicial = E_inicial / amostras;
		var = (M_quad_t- M_mediaquad)/((double)amostras*N);
		//cout << var <<endl;
		/*cout <<"Energia inicial = " <<E_inicial <<endl;
		cout <<"Energia media = " <<E_media <<endl;
		cout <<"Magnetizacao inicial = " <<M_inicial <<endl;
		cout <<"Magnetizacao media = " <<M_media <<endl;*/

	//Print_lattice(lat, L, L, ImageWidth, ImageHeight, "T3_L128.ppm");
	
	file <<T <<"\t" <<E_media <<endl;
	file2 <<T <<"\t" <<M_media <<endl;
	file3 << T <<"\t" << var <<endl;
	
	}
	
	file.close();
	file2.close();
	file3.close();
	
	return 0;
}

int energia(int lat[], int L, int a)
{
	int E=0;

	// Condicoes de fronteira, 4 cantos da rede
	if(a % L== 0 and a/L == 0)
	{
		E= - lat[a]*(lat[a+1]+ lat[a + (L - 1)] + lat[a + L] + lat[a + L * (L - 1)]);
	}
	else if( a%L == 0 and a/L== L-1)
	{
		E = - lat[a] * (lat[a + 1] + lat[a + (L - 1)] + lat[a - L * (L - 1)] + lat[a - L]);
	}
	else if( a %L == L-1 and a/L == 0)
	{
		E = - lat[a] * (lat[a - (L - 1)] + lat[a - 1] + lat[a + L] + lat[a + L * (L - 1)]);
	}
	else if(a %L == L-1 and a/L == L-1)
	{
		E = - lat[a] * (lat[a - (L - 1)] + lat[a - 1] + lat[a - L * (L - 1)] + lat[a - L]);
	}


	//Condicoes de fronteira 1º coluna e ultima coluna
	else if(a%L==0)
	{
		E = - lat[a] * (lat[a + 1] + lat[a + (L - 1)] + lat[a + L] + lat[a - L]);
	}
	else if(a%L == L-1)
	{
		E = - lat[a] * (lat[a - (L - 1)] + lat[a - 1] + lat[a + L] + lat[a - L]);
	}
	
	//Condicoes de fronteira 1º linha e ultima linha
	else if( a/L == L-1)
	{
		E = - lat[a] * (lat[a + 1] + lat[a - 1] + lat[a - L * (L - 1)] + lat[a - L]);
	}
	else if(a/L == 0)
	{
		E = - lat[a] * (lat[a + 1] + lat[a - 1] + lat[a + L] + lat[a + L * (L - 1)]);
	}
	
	// Caso geral
	else
	{
		E = -lat[a] * (lat[a + 1] + lat[a - 1] + lat[a + L] + lat[a - L]);
	}

	return E;
}

	





		
			

	





	
