#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;


int main ()
{
	long long int x = 214587; // semente
	long long int N = 500; // numero de pontos gerados
	long long int c = 16807; // multiplicador
	long long int p = 2147483647; // periodo maximo
	long long int y[N];
	double yn[N];// vetor com os valores normalizados
	y[0]= x;
	y[1]= (c*y[0])%p;
	yn[0] = (double)y[0]/(double)p;
	yn[1] = (double)y[1]/(double)p;
	ofstream outfile;
	outfile.open("dadosN=500c=16807.txt");
	
	for (int i=2; i<N; i++)
	{
		y[i]=(c*y[i-1])%p;
		yn[i]=(double)y[i]/(double)p;// normalizacao dos valores
		outfile <<yn[i-2]<<"\t"<<yn[i-1]<<"\t"<<yn[i]<<endl;
		
	}
	outfile.close();
	return 0;
}
