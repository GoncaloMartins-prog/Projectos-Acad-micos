#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include <math.h>

using namespace std;


int main()
{

	/* Neste exercicio foi utilizado o metodo de Gauss-Seidel sem relaxacao e com relaxacao
	para utilizar o Gauss_seidel com relaxacao substituir o calculo de x[i] pelo que esta em comentarios.
	*/
	int n = 5;
	double x[n]={0};
	double a[n][n]={{-5,3,0,0,0},{3,-6,3,0,0},{0,3,-6,3,0},{0,0,3,-6,3},{0,0,0,3,-5}};
	double b[n]={-80,0,0,60,0};
	double erro_rel = 0;
	double x_anterior = 0;
	double erro_max = 10;
	int k_max = 200;
	int k = 0;
	double soma_antes = 0;
	double soma_depois = 0;
	double lamb = 2.0;// toma os valores {0.5,1,1.2,2}
	//ofstream outfile1;
	//outfile1.open("dados1.txt");
	
	while(abs(erro_max)>0.0001 && k < k_max)
	{
		erro_max = 0;
		for (int i = 0; i < n; i++)
		{
			soma_antes=0;
			for( int j = 0; j < i;j++)
			{
				soma_antes += a[i][j]*x[j];
			} 	
		soma_depois = 0;
		for(int t = i +1; t < n;t++)
		{
		
			soma_depois += a[i][t]*x[t];
			

		}
		x_anterior = x[i];
		x[i] =(b[i] - soma_antes - soma_depois)/a[i][i];
		//x[i] =lamb*(b[i] - soma_antes - soma_depois)/(a[i][i])+(1-lamb)*x[i];
		erro_rel = abs((x[i]-x_anterior)/x[i]);
 		if(erro_rel > erro_max)
		{
			erro_max = erro_rel;		
		}
		
		}
		k++;
	}
	for(int l = 0; l < n; l++)
	{
	//outfile1 << k << "\t" << (double)x[l] << "\t" <<erro_max<< endl;
	cout << "numero de iteracoes= " << k <<"\t"<< "Valor de x= " <<setprecision(6)<<(double)x[l]<<endl;
	}
	//outfile1.close();
	/*Neste exercício aplicar o metodo de newton. para resolver Jd= F
	foi usado o metodo de eliminacao de gauss
	*/
	int n1 = 2;
	int k2 = 0;
	double x1[2] = {-1.0,1.0 };
	double d[2]={0.0,0.0};
	double F[2]= {pow(x1[0],2) - 5 + pow(x1[1],2),x1[1] + 1 - pow(x1[0],2) };
	double JF[2][2]= { {x1[0]*2,x1[1]*2},{x1[0]*2,-1} };
	double err_max = 10;
	double k_max1 = 100;
	ofstream outfile;
	outfile.open("dados.txt");
	outfile<<x1[0]<<"\t"<<x1[1]<<"\t"<<k2<<endl;
	while (abs(err_max) > 0.0001 && k2 < k_max1)
	{
		err_max = 0;
		F[0]= pow(x1[0],2) - 5 + pow(x1[1],2);
		F[1] = x1[1] + 1 - pow(x1[0],2);
		JF [0][0]=x1[0]*2;
		JF [0][1]=x1[1]*2;
		JF [1][0]=-x1[0]*2;
		JF [1][1]=1;
		
		cout << F[0] << "\t" << F[1] << endl;


		int maxi = 0;
		double temp=0;
		double m3 =0;
		for (int z = 0; z < n1 - 1; z++)
		{
			maxi = z;
			for (int c = z + 1; c < n1; c++)
			{
				if (abs(JF[c][z]) > abs(JF[maxi][z]))
				{
					maxi = c;
				}
			}
			if (maxi != z)
			{
				for (int b = z; b < n1; b++)
				{
					temp = JF[z][b];
					JF[z][b] = JF[maxi][b];
					JF[maxi][b] = temp;
				}
				temp = F[z];
				F[z] = F[maxi];
				F[maxi] = temp;
				
			}
			for (int t = z + 1; t < n1; t++)
			{
				m3 = JF[t][z] / JF[z][z];
				for (int v = z; v < n1; v++)
				{
					JF[t][v] = JF[t][v] - m3 * JF[z][v];
				}

				F[t] = F[t] - m3 * F[z];
				
			}

		}
		double soma3 = 0;
		d[n1 - 1] = F[n1 - 1] / JF[n1 - 1][n1 - 1];
		for (int i = n1 - 1; i > -1; i--)
		{

			soma3 = 0;
			for (int j = i + 1; j < n1; j++)
			{
				soma3 = soma3 + JF[i][j] * d[j];
			}

			d[i] = (F[i] - soma3) / JF[i][i];
			

		}

		
		for (int i = 0; i < 2; i++)
		{
			x1[i]= x1[i]-d[i];
			if( abs(d[i]/x1[i])>abs(err_max))
			{
				err_max = abs(d[i]/x1[i]);
			}
		}
		k2++;
		outfile<<x1[0]<<"\t"<<x1[1]<<"\t"<<k2<<endl;
	
	}
	for( int j = 0; j < 2; j++)
	{
		cout << "valor de x= "<<x1[j]<<"\t"<<"iteracoes "<<k2<< "\t"<<"erro max = "<<err_max<<endl;
	
	}
	outfile.close();
	return 0;
}
