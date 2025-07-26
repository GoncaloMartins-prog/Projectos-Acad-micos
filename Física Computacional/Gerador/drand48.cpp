#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;


int main ()
{
	
	long long int N = 500; // numero de pontos gerados
	double y[N];
	y[0]= drand48();
	y[1]= drand48();
	ofstream outfile;
	outfile.open("drand48.txt");
	
	for (long long int i=2; i<=N; i++)
	{
		y[i]=drand48();
		outfile <<y[i-2]<<"\t"<<y[i-1]<<"\t"<<y[i]<<endl;
		
	}
	outfile.close();
	return 0;
}
