#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
	/*
	primeiro exercício alinea a) aplicar o método de substituição inversa
	usar R3 igual a 0 e 2.
	*/
	double R3 = -2.0;
	double a1[3][3]={{1.0,-1.0,-1.0},{0.0,2.0,-1.0},{R3,0.0,-1.0}};
	// ciclo para confirma valores de a1
	/*for(int i = 0; i<3;i++)
	{
		for(int j=0; j<3;j++)
		{
			cout<< a1[i][j]<<endl;
		}
	}*/
	double b1[3]={0.0,-2.0,-7.0};
	double x1[3]={0.0};
	int n = 3;
	double soma1 = 0;
	x1[n-1]=b1[n-1]/a1[n-1][n-1];
	for(int i =n-1; i>-1;i--)
	{

		soma1 = 0;
		for(int j =i+1; j<n;j++)
		{
			soma1 = soma1 + a1[i][j]*x1[j];
		}
		
		x1[i]=(b1[i]-soma1)/a1[i][i];

	}


	for(int k=0; k<n;k++)
	{
		cout <<"valores para alinea a) "<<"\t"<<(double)x1[k]<<endl;

	}


	/*
	inicio da alinea b) implementar o metodo de eliminacao de gauss
	sem escolha de pivot
	mesmas condições	
	*/ 
	double a2[3][3]={{1.0,-1.0,-1.0},{0.0,2.0,-1.0},{R3,0.0,-1.0}};
	double b2[3]={0.0,-2.0,-7.0};
	double x2[3]={0.0};
	double m=0;
	for(int l=0;l>n-1;l--)
	{
		for( int t=l+1;t<n;t++)
		{
			m=a2[t][l]/a2[l][l];
			for(int v =l;v<l;v++)
			{
				a2[t][v]=a2[t][v]-m*a2[l][v];
			}
			
			b2[t]=b2[t]-m*b2[l];
		}
	}
	double soma2 = 0;	
	x2[n-1]=b2[n-1]/a2[n-1][n-1];
	for(int i =n-1; i>-1;i--)
	{

		soma2 = 0;
		for(int j =i+1; j<n;j++)
		{
			soma2 = soma2 + a2[i][j]*x2[j];
		}
		
		x2[i]=(b2[i]-soma2)/a2[i][i];

	}
	for(int y=0; y<n;y++)
	{
		cout <<"valores para alinea b) "<<"\t"<<(double)x2[y]<<endl;

	}

	/*
	inicio da alinea c)  e e) implementar o metodo de eliminacao de gauss
	sem escolha de pivot e depois com escolha parcial de pivot
	R2=0 e R3=2
	para aplicar gauss sem escolha de pivot utilizar a alinea b) mundando as condicoes
	para resolver a alinea e) retirar o ciclo em comentario para variar o v entre -10 e 10
	mudar tambem o array b3 para o que está em comentario
	*/
	double R2=2.0;
	double v = - 10;
	double a3[3][3]={{1.0,-1.0,-1.0},{0.0,R2,-1.0},{R3,0.0,-1.0}};
	//double b3[3]={0.0,-v,(-5.0-v)};
	double b3[3] = { 0.0,-2.0,-7.0 };
	double x3[3]={0.0};
	int maxi =0;
	double temp=0;
	double m3 =0;
	ofstream outfile;
	outfile.open("met_gaus_pivot.txt");
	// gauss com escolha parcial de pivot
	//for (v; v <= 10; v++)
	//{	
		//b3[0] = 0.0;
		//b3[1] = -v;
		//b3[2] = -5.0 - v;
		//cout << b3[0] << "\t" << b3[1] << "\t" << b3[2] << endl;
		for (int z = 0; z < n - 1; z++)
		{
			maxi = z;
			for (int c = z + 1; c < n; c++)
			{
				if (abs(a3[c][z]) > abs(a3[maxi][z]))
				{
					maxi = c;
				}
			}
			if (maxi != z)
			{
				for (int b = z; b < n; b++)
				{
					temp = a3[z][b];
					a3[z][b] = a3[maxi][b];
					a3[maxi][b] = temp;
				}
				temp = b3[z];
				b3[z] = b3[maxi];
				b3[maxi] = temp;
				
			}
			for (int t = z + 1; t < n; t++)
			{
				m3 = a3[t][z] / a3[z][z];
				for (int v = z; v < n; v++)
				{
					a3[t][v] = a3[t][v] - m3 * a3[z][v];
				}

				b3[t] = b3[t] - m3 * b3[z];
				
			}

		}
		double soma3 = 0;
		x3[n - 1] = b3[n - 1] / a3[n - 1][n - 1];
		for (int i = n - 1; i > -1; i--)
		{

			soma3 = 0;
			for (int j = i + 1; j < n; j++)
			{
				soma3 = soma3 + a3[i][j] * x3[j];
			}

			x3[i] = (b3[i] - soma3) / a3[i][i];

		}
		// retirar para a alinea e)
		for (int y = 0; y < n; y++)
		{
			cout << "valores para alinea c) " << (double)x3[y] << endl;
		}
	
		//cout << "valores para alinea  e)" << v << "\t" << (double)x3[0] << "\t" << (double)x3[1] << "\t" << (double)x3[2] << endl;
		//outfile << v << "\t" << (double)x3[0] << "\t"<< (double)x3[1] << "\t" << (double)x3[2] << endl;
		

	//}

	outfile.close();

	return 0;
}
