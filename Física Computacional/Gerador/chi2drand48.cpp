#include <iostream>
#include <math.h>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
#include <cstdlib>
using namespace std;


int main ()
{
	
	long long int N = 5000; // numero de pontos gerados
	double y[N];
	int k =21;
	long long int K[N]; // inertvalos ( vetor )
	double np = (double)N/(double)k;
	double qi2 = 0; // variavel do qi quadrado
	int total = 0;
	y[0]= drand48();
	y[1]= drand48();
	
	
	
	for (long long int i=2; i<=N; i++)
	{
		y[i]=drand48();
		
		
	}
	// ciclo que separa os valores por intervalos
	for(int i = 0; i < N; i++)
 	{
   		for(int a = 0; a < k; a++)
   		{ 
     			if(y[i] > (double)a / (double)k && y[i] <= ((double)a + 1.0) / (double)k)
    			 {
     
      				K[a]++;
     
     			}     
   		}     
 	}

	for( int j = 0; j < k; j++)
 	{
   
   		qi2 = qi2 + pow( ((double)K[j] - np) , 2) / np;  //calculo do qi quadrado
   		total = total + K[j];
   		
   
 	}


	cout <<fixed <<setprecision(4) <<"qi2=" <<qi2 <<endl;
 	cout <<total <<endl;
	
	


	return 0;
}
