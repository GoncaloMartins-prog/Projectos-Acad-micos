#include <iostream>
#include <stdlib.h>
#include <cstdlib>
#include <cmath>
#include <fstream>
#define _USE_MATH_DEFINES

using namespace std;

int main()
{

	int L = 100;
	double u[L*L];
	int b[L][L] = {{0},{0}};
	double delta = 0;
	double eps = 0.01;
	double Delta = 1 / double(L);
	double uant = 0;
	double deltafinal = 1;
	double deltamax = 0;
	double contador = 0;
	int x;
	int y;
	
	//ofstream file;
	//ofstream file2;
	ofstream file3;
	//file.open("cargacentralizada.txt");
	//file2.open("cargasequidistantes.txt");
	file3.open("10cargas.txt");
	

	//b[L/2][L/2]=1; // carga centralizada
	//b[(L/2)+5][(L/2)+5] = 1; // cargas equidistantes
	//b[(L/2)-5][(L/2)-5] = 1;
	
	while( contador < 10) // 10 cargas aleatoriamente distribuidas
	{
		x = rand() % L;
		y = rand() % L;
		
		if( (x > 5 && y > 5) && (x < (L-5) && y < (L-5)))
		{
			b[x][y] = 1;
			contador ++;
		}
		else
		{
		}
	}
	

	for( int i = 0; i < L*L; i++)
	{
		u[i] = 0;
	}

	while(deltafinal>eps)
	{
		delta = 0.0;
		deltamax = 0.0;
		

		for( int i = 0; i < L*L; i++)
		{
			x = i % L;
			y = i / L;
			if( (x-1)> 0 && (x+1)<L && (y-1)>0 && (y+1)<L)
			{
				uant = u[x+y*L];
				u[x+y*L]=0.25*(u[(x+1)+y*L] + u[(x-1)+y*L] + u[x+(y+1)*L] + u[x+(y-1)*L] - b[x][y]*Delta*Delta);
				if(uant != 0 && contador > 5 )
				{
					delta = abs(abs(u[x+y*L]-uant)/uant);
					//cout << delta<< "\t" << deltamax<<endl;
					if(delta > deltamax)
					{
						deltamax = delta;
						//cout << deltamax << endl;
					}

				}
				contador = contador + 1;
				//cout << contador <<endl;
			}
		
		}
	
		if(deltamax > 0)
		{
			deltafinal = deltamax;
		}
	
	}
	cout<<deltafinal<<endl;
	
	for(int i = 0; i<L*L; i++)
	{	
		x = i%L;
		y = i/L;
		//file << x << "\t" << y << "\t" << u[i] << endl;
		//file2 << x << "\t" << y << "\t" << u[i] << endl;
		file3 << x << "\t" << y << "\t" << u[i] << endl;
	}

	//file.close();
	//file2.close();
	file3.close();
	
		

	

	return 0;
}
