#include<iostream>
#include<stdlib.h>
#include "latticeview.h"
#include<cmath>

#define ImageWidth 1000 // image width
#define ImageHeight 1000 // image height

using namespace std;

main()
{
	int N = 32;
	int lat[N*N]; // Tamanho da configuraçao
	double p = 0.6; // 0.5 0.4 // probabilidade do vizinho estar ocupado
	double pi; // numero aleatorio para comparar com p
	int icounter;

	for( icounter=0; icounter<N*N; icounter++)
	{
		pi = (double) rand() / (double)(RAND_MAX); // drand48()
		
		if( pi<p)
		{
			lat[icounter]=1;
		}
		
		else
		{
			lat[icounter ]=0;
		}
	}

	Print_lattice ( lat, N, N, ImageWidth, ImageHeight, "rede.ppm");
	
	return 0;
}
