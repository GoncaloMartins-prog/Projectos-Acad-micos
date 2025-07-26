#include <iostream>
#include <math.h>
#include <fstream>
#include <iomanip>

using namespace std;

double funcao(double u[], int i, int j, int L,  double b)
{
	double resultado;
	//Condicoes de fronteira para os 4 cantos da configuracao
	if(i == 0 and j == 0)
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i + 1) + j * L] + u[(i + (L -1)) + j * L]) - u[i + (j + (L - 1)) * L];
	}
	else if(i == 0 and j == L - 1)
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i + 1) + j * L] + u[(i + (L -1)) + j * L]) - u[i + (j - 1) * L];
	}
	else if(i == L - 1 and j == 0)
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i - (L - 1)) + j * L] + u[(i - 1) + j * L]) - u[i + (j + (L - 1)) * L];
	}
	else if(i == L - 1 and j == L - 1)
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i - (L - 1)) + j * L] + u[(i - 1) + j * L]) - u[i + (j - 1) * L];
	}

	//Condicoes de fronteira para a primeira e ultima coluna
	else if(i == 0)
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i + 1) + j * L] + u[(i + (L - 1)) + j * L]) - u[i + (j - 1) * L];
	}
	else if(i == L - 1)
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i - (L - 1)) + j * L] + u[(i - 1) + j * L]) - u[i + (j - 1) * L];
	}

	//Condicoes de fronteira para a primeira e ultima linha
	else if(j == 0)
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i + 1) + j * L] + u[(i - 1) + j * L]) - u[i + (j + (L - 1)) * L];
	}
	else if(j == L - 1)
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i + 1) + j * L] + u[(i - 1) + j * L]) - u[i + (j - 1) * L];
	}
		
	//Formula da função de onda geral
	else
	{
		resultado = 2 * (1 - b) * u[i + j * L] + b * (u[(i + 1) + j * L] + u[(i - 1) + j * L]) - u[i + (j - 1) * L];
	}	 
	
	return resultado;
}

int main()
{ 
	int L = 100;
	double u[L*L];
	double delta_x = 0.5;
	double delta_t = 0.01;
	double b = 0.5;// fazer para b= 1, b= 2; b= 1.5; b = 0.5
	
	
	ofstream file;
	file.open("onda_b0.5_L100.txt");

	for(int i =0; i < L; i++)
	{
		u[i + 0*L]= exp(-pow((double)i* delta_x -10,2));
		u[i + (L-1)*L]= exp(-pow((double)i* delta_x - sqrt(b)*delta_x - 10,2));
	}
	
	for( int t = 0; t < L-1; t++)
	{
		for( int j = 0; j < L; j++)
		{
			u[j + (t+1)*L]=funcao(u, j, t, L, b);
			
		}
	}

	for(int i = 0; i < L*L; i++)
	{
		file << (double)(i%L) * delta_x << "\t" << (double)(i/L)*delta_t << "\t" << u[i]<< endl;
		if(i%L == L-1)
		{
			file << endl;
		}
	}

	
	
	file.close();
	
	return 0;
}
































