#include <iostream>
#include <cmath>
#include <cstdlib>
#include <fstream>

using namespace std;

int main()
{
	int N = 5000;
	int i = 0; // contador
	double PI = 4*atan(1.0);
	double R = 5.0;
	double r;
	double teta;
	double x[N];
	double y [N];
	srand48(214587);

	ofstream outfile;
	outfile.open("circulo_corrigido.txt");


	for(i; i<N;i++)
	{ 
		r = R*sqrt(drand48());// raio aleatorio
		teta = 2*PI*(drand48()); // angulo aleatorio 
		
		x[i]= r*cos(teta);
		y[i]=r*sin(teta);
		
		outfile <<x[i]<<"\t"<<y[i]<<endl;
	}

	outfile.close();
	return 0;
}
