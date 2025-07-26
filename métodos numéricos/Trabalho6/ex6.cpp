#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include <math.h>
#include <vector>

using namespace std;

/*
Falta fazer o metodo do trapezio mas com erro
No Romberg corrigir os erros de código

no ex 2
usar o trapezio ja feito

*/

double V(double x)
{
	double g = 9.8;
	double pi = 4.0*atan(1.0);
	double V = (-pi/3.0)*pow(x,3.0)*9.8*997.0+(pi*2.0)*pow(x,2.0)*9.8*997.0;

	return V;
}

double trapezio( double a, double b, int n)
{
	double h = 0;
	double soma = 0;
	double resultado = 0;
	h = (b-a)/n;
	soma = V(a)+V(b);
	for( int i = 1; i<n;i++)
	{
		soma += 2*V(a+i*h);
	
	}
	
	resultado = (h/2.0)*soma;
	return resultado;
}
/*
valores iniciais a e b, dimensao n, precisao p
vector <double> &nome_da_variavel permite-me dar return de arrays
assim posso usar void, que apenas recebe valores, e mudar os valores do meu array
*/
void Romberg(double a, double b, int n_max, double p, vector<double> &resultado, vector<double> &erro_romberg)
{
	
	int k_max = n_max;
	double I[n_max+1][n_max+1]={0};
	int k = 0;
	int n = 0;
	double erro = 10;
	
	I[0][0] = trapezio(a,b,pow(2,n));
	
	while(erro>p && k < k_max)
	{
		n++;
		I[n][0]=trapezio(a,b,pow(2,n));
		k++;
		for( int i = 1; i < k+1; i++)
		{
			int j = k;
			I[j][i] = (pow(2,2*k)*I[j][i-1]-I[j-1][i-1])/(pow(2,2*k)-1);
		}
		erro = abs((I[k][k]-I[k][k-1])/I[k][k]);

	
	
	}
	resultado.push_back(I[k][k]);
	erro_romberg.push_back(erro);

}
double Simpson ( double a, double b, double n)
{
	double h = 0;
	double soma_h = 0;
	double resultado = 0;
	h = (b-a)/n;
	soma_h = V(a)+V(b);
	/*
	este ciclo eh para os valores impares 
	*/
	for( int i = 1; i<n+1;i+=2)
	{
		soma_h += 4*V(a+i*h);
	
	}
	/*
	este ciclo eh para os valores pares 
	*/
	for( int j = 2; j<n;j+=2)
	{
		soma_h += 2.0*V(a+j*h);
	
	}
	resultado = (h/3.0)*soma_h;
	return resultado;
}
int main()
{
	
	double a = 0.0;
	double b = 2.0;
	double n = 30;
	double I = 0;
	double v = 0;
	double p =0.3;
	double valor_real = 122781.0;

		

	//cout<< "trapezio "<< trapezio(a,b,n)<<endl;
	
	vector<double> resultado;
	vector<double> erro_romberg;

	Romberg( a, b, n, p, resultado, erro_romberg);
	
	cout <<"Romberg"<<"\t"<<resultado[0]<<"+/-"<<erro_romberg[0]<<endl;



	/*
	metodo de Simpson
	*/
	double s_h = Simpson(a,b,n);
	double s_2h = Simpson(a,b,n/2);
	double erro_simpson = abs(s_h-s_2h)/15;

	cout<<"Simpson"<<"\t"<< s_h << "+/-"<<erro_simpson<<endl;

	/*
	exercico 2
	*/
	int n2 = 11;
	double F[n2] = {0.0,37.0,71.0,104.0,134.0,161.0,185.0,207.0,225.0,239.0,250.0};
	double soma_h = F[n2-1]+F[0];
	for (int i = 1; i < n2-1; i++)
	{
		soma_h+=2*(F[i]);

	}
	I = (0.05/2.0)*soma_h;
	v = sqrt(2.0/0.075*I);
	
	cout << v << endl;
	
	

	return 0;
}
