#include <iostream>
#include <math.h>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	ofstream outfile;
	long long int N = 10000; // dimensao// 100//1000
	long long int x0 = 214587; // semente x0=21
	long long int p = 2147483647; // periodo maximo p=31
	long long int c = 16807; // multiplicador c=3
	int k = 11; // numero de intervalos
	long long int x[N]; // valores gerados ( vetor )
	long long int K[N]; // inertvalos ( vetor )
	double np = (double)N/(double)k;
	double qi2 = 0; // variavel do qi quadrado
	int total = 0;
	double xn[N]; // vetor com os valores normalizados

	for( int l=0; l<k;l++)
	{
		K[l]=0;
	}
	
	x[0]=x0;
	xn[0]= (double)x[0]/(double)p;

	outfile.open("qui2.txt");
	for(int i = 1; i < N; i++)// valores normalizados
 	{

		x[i]=(c*x[i-1])%p;
		xn[i]=(double)x[i]/(double)p;
		//outfile <<xn[i]<< "\t"<< endl;
	}
	



	// ciclo que separa os valores por intervalos
	for(int i = 0; i < N; i++)
 	{
   		for(int a = 0; a < k; a++)
   		{ 
     			if(xn[i] > (double)a / (double)k && xn[i] <= ((double)a + 1.0) / (double)k)
    			 {
     
      				K[a]++;
     
     			}     
   		}     
 	}


	
 	for( int j = 0; j < k; j++)
 	{
   
   		qi2 = qi2 + pow( ((double)K[j] - np) , 2) / np;  //calculo do qi quadrado
   		total = total + K[j];
   		outfile <<xn[j]<< "\t"<<K[j] <<endl;
   
 	}
	 outfile.close();
 
 	cout <<fixed <<setprecision(2) <<"qi2=" <<qi2 <<endl;
 	cout <<total <<endl;
 
	 return 0;

}
