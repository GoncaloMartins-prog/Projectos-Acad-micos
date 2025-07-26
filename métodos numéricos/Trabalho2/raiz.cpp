#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <cmath>
#include <fstream>


using namespace std;

double funcao( double x)
{
	double resultado;
	resultado = pow(x,2) - 4;

return resultado;
}

double funcao2( double x)
{
	double PI = 4*atan(1.0);
	double resultado;
	resultado = 9*exp(-x)*sin(2*PI*x) - 1.5*pow(10, -3);

return resultado;
}
double funcaolinha2( double x)
{	
	double PI = 4*atan(1.0);
	double resultado;
	resultado = 18*PI*exp(-x)*cos(2*PI*x) - 9*exp(-x)*sin(2*PI*x);

return resultado;
}
double funcao3( double x)
{
	
	double resultado;
	resultado = (tan(x)*90-(9.8/(2*pow(30,2)*pow(cos(x),2)))*pow(90,2) + 1-1.8);

return resultado;
}


int main()
{
	

	/*são utilizados 3 intervalos neste exercício
	1º[0.7,2.6]2º[0.4,1.7]3º[-3,0.6]
	Neste parte do código é resolvido o exercício 1*/

	//  método da bissessão
	
	double a1 = -3.0;
	double b1 = 0.6;
	double d1 = (b1-a1)/2;
	double x1 = a1 + d1;
	int n1 = 0;
	
	double fa1 = funcao(a1);
	double fb1 = funcao(b1);
	double fx1 = 0;
	double logd1 = 0;
	ofstream outfile;
	outfile.open("dados_intervalo3_bissecao.txt");
	
	while (d1 > pow(10,-5))
	{
				
		fx1 = funcao(x1);
		if(fa1*fx1 > 0)
		{
			a1 = x1;
			fa1 = fx1;
		}
		else
		{
			b1 = x1;
			fb1 = fx1;
		}
		d1 = (b1-a1)/2;
		x1 = a1 + d1;
		logd1 = log(d1);
		n1++;
		cout <<"interassao bissessao= "<<n1 << "\t"<<"criterio= "<< d1 << "\t" << "lod do erro" << logd1 <<endl;
		outfile << n1 <<"\t"<<d1<<"\t"<< logd1<<endl;
	} 
	outfile.close();

	// método de newton
	double x = 1.0;
	double fk = funcao(x);
	int k = 0;
	double d = (fk / (2.0 * x));
	double logd = 0; // valor log10 de d
	ofstream outfile2;
	outfile2.open("dados_intervalo3_newton.txt");
	
	while ( abs(d) > pow(10, -5) && k <50)
	{
		x = x - d;
		fk = funcao(x);
		d = (fk / (2.0 * x));
		logd = log(d);
		k++;
		cout <<"interassao newton= "<<k << "\t"<<"criterio= "<< d<<"\t" <<"lod do erro"<< logd << endl;
		outfile2 << k << "\t" << d <<"\t"<< logd<< endl;
	
	}
	outfile2.close();

	// metodo da secante
	double x0 = 3.0;
	double x2 = 4.0;
	double x3 = 0;
	double f0 = funcao(x0);
	double f2 = funcao(x2);
	int l = 0;
	double d2 = f2 * ((x2 - x0) / ( f2 - f0));
	double logd2 = 0;

	ofstream outfile3;
	outfile3.open("dados_intervalo3_secante.txt");
	
	while ( abs(d2) > pow(10, -5) && l <50)
	{
		x3 = x2 - d2;
		x0 = x2;
		x2 = x3;
		f0 = f2;
		f2 = funcao(x2);
		f0 = funcao(x0);
		d2 = f2 * ((x2 - x0) / ( f2 - f0));
		logd2 = log(d2);
		l++;
		cout <<"interassao secante= "<<l <<"\t" <<"criterio= "<< d2 << "\t" << "lod do erro" << logd2 <<endl;
		outfile3 << l << "\t" << d2 <<"\t"<<logd2<< endl;
	}
	outfile3.close();

	/* inicio do exercicio 2
	É utilizado o metodo de newton para uma nova função
	valores iniciais  {0.6,0.7,0.75,0.8,0.9}	
	*/

	
	cout << " Inicio do exercio 2 " << endl;
	double y = 0.9;
	double fk2 = funcao2(y);
	double fk2_linha = funcaolinha2(y);
	int m = 0;
	double d4 = (fk2 / fk2_linha);
	ofstream outfile4;
	outfile4.open("exercicio2_0,9.txt");
	
	while ( abs(d4) > pow(10, -6) && m < 50)
	{
		y = y - d4;
		fk2 = funcao2(y);
		fk2_linha = funcaolinha2(y);
		d4 = (fk2 / fk2_linha);
		m++;
		cout <<"interassao newton= "<<m << "\t"<<"criterio= "<< y<<endl;
		outfile4 << m << "\t" << y << endl;
	
	}
	outfile4.close();

	/* inicio do exercicio 3
	É utilizado o metodo da secante para uma nova função
		
	*/
	cout << " Inicio do exercio 3 " << endl;
	double PI = 4*atan(1.0);
	double x00 = 5*PI/4;
	double x22 = 4.2;
	double x33 = 0;
	double f00 = funcao3(x00);
	double f22 = funcao3(x22);
	int n = 0;
	double d22 = f22 * ((x22 - x00) / ( f22 - f00));
	
	


	ofstream outfile5;
	outfile5.open("exercicio3.txt");
	
	while ( abs(d22) > pow(10, -5) && n <50)
	{
		x33 = x22 - d22;
		x00 = x22;
		x22 = x33;
		f00 = f22;
		f22 = funcao3(x22);
		f00 = funcao3(x00);
		d22 = f22 * ((x22 - x00) / ( f22 - f00));
		n++;
		cout <<"interassao secante= "<<n <<"\t" <<"criterio= "<< x00<<endl;
		outfile5 << n << "\t" << x00 << endl;
	}

	outfile5.close();



return 0;
}
