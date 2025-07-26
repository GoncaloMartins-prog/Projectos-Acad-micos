#include <iostream>
#include <math.h>
#include <fstream>
#include <stdlib.h>
using namespace std;


int main ()
{
	
	long long int N = 500; // numero de pontos gerados
	long long int y[N];
	long long int p = 2147483647;
	double yn[N];// vetor com os valores normalizados
	y[0]= rand();
	y[1]= rand();
	yn[0] = (double)y[0]/(double)p;
	yn[1] = (double)y[1]/(double)p;
	ofstream outfile;
	outfile.open("rand.txt");
	
	for (long long int i=2; i<=N; i++)
	{
		y[i]=rand();
		yn[i]=(double)y[i]/(double)p;// normalizacao dos valores
		outfile <<yn[i-2]<<"\t"<<yn[i-1]<<"\t"<<yn[i]<<endl;
		
	}
	outfile.close();
	return 0;
}
