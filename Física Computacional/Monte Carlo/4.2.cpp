#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include<cmath>

using namespace std;

int main()
{
	int L = 1; // tamanho do lado da caixa
	int Np = 1000; // numero de pontos distribuidos uniformemente
	int M = 1000; // numero de configurações
	double soma_dmedia = 0;
	double dmedia = 0;
	double dij = 0;
	double x[Np];
	double y[Np];
	double z[Np];
	double dmedio = 0;

	ofstream file;

	file.open("Np1000_M1000.txt");

	for (int m = 1; m <= M; m++)
	{
		dij = 0;
		// ciclo que gera os pontos
		for (int k = 0; k < Np; k++)
		{
			x[k] = (double)L * drand48();
			y[k] = (double)L * drand48();
			z[k] = (double)L * drand48();
		}

		for (int i = 0; i < Np; i++)
		{
			for (int j = i + 1; j < Np; j++)
			{
				dij = dij + sqrt(pow((x[i] - x[j]), 2) + pow((y[i] - y[j]), 2) + pow((z[i] - z[j]),2));
			}
		}


		dmedia = 2.0 / (double)(Np * (Np - 1)) * dij;
		soma_dmedia = soma_dmedia + dmedia;
		dmedio = soma_dmedia / (double)m;

		file << m << "\t" << dmedio << endl;
	}
	file.close();

	return 0;
}
