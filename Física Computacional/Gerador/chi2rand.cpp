#include <iostream>
#include <math.h>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
using namespace std;


int main ()
{
	
	long long int N = 1000; // numero de pontos gerados
	long long int y[N];
	long long int p = 2147483647;
	double yn[N];// vetor com os valores normalizados
	int k =21;
	long long int K[N]; // inertvalos ( vetor )
	double np = (double)N/(double)k;
	double qi2 = 0; // variavel do qi quadrado
	int total = 0;
	int seed = 16807;
	srand(seed);
	ofstream outfile;
	outfile.open("Valores normalizados_rand.txt");
	for (int l = 0; l < k; l++)
	{
		K[l] = 0;
	}
	
	
	for (long long int i=0; i<=N; i++)
	{
		y[i]=rand();
		yn[i]=(double)y[i]/(double)p;// normalizacao dos valores
		outfile << y[i]<<"\t"<< yn[i] << endl;
		
	}
	outfile.close();
	
	for(int i = 0; i < N; i++)
 	{
   		for(int a = 0; a < k; a++)
   		{ 
     			if(yn[i] > (double)a / (double)k && yn[i] <= ((double)a + 1.0) / (double)k)
    			{
     
      				K[a]++;
     
     			}     
   		}     
 	}
	outfile.open("Quantidades em cada intervalo_rand.txt");
	for( int j = 0; j < k; j++)
 	{
   
   		qi2 = qi2 + pow( ((double)K[j] - np) , 2) / np;  //calculo do qi quadrado
   		total = total + K[j];
		outfile << j << "\t" << K[j] << endl;
   		
   
 	}
	outfile.close();

	cout <<fixed <<setprecision(4) <<"qi2=" <<qi2 <<endl;
 	cout <<total <<endl;
	
	return 0;
}
