#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <cmath>
#include <fstream>


using namespace std;

double funcao(double x)
{
	double resultado;
	resultado = 0.5*pow((x - 2), 2);
	return resultado;
}
double funcaolinha(double x)
{
	double resultado;
	resultado = x - 2;
	return resultado;
}

double funcao2 ( double x)
{
	double resultado;
	resultado = 80*exp(-2*x)-10/x;
	return resultado;
}

double funcao2linha ( double x)
{
	double resultado;
	resultado = -160*exp(-2*x)+10/pow(x,2);
	return resultado;
}

double funcao3 ( double x )
{
	double resultado;
	resultado = 160*2*exp(-2*x)-20/pow(x,3);
	return resultado;
}

double df_dx ( double x, double y)
{
	double resultado;
	resultado = (-160*x*exp(-2*sqrt(pow(x,2)+pow(y,2))))/(sqrt(pow(x,2)+pow(y,2)))+(10*x)/pow(pow(x,2)+pow(y,2),1.5);
	return resultado;
}
double df_dy ( double x, double y)
{
	double resultado;
	resultado = (-160*y*exp(-2*sqrt(pow(x,2)+pow(y,2))))/(sqrt(pow(x,2)+pow(y,2)))+(10*y)/pow(pow(x,2)+pow(y,2),1.5);
	return resultado;
}

int main()
{
	/*
	Exercício 1
	alinea a) método do número dourado para uma função
	com os intervalos iniciais iguais a  [a,b]={[-0.7,2.6];[0.4,1.7]}
	com critério de 0.001.
	alinea b) método do gradiente para uma função
	10 iterações max, x0=0 precisão de 10^-5 e lambda igual a {0.1; 0.5; 1; 2; 2.1}.
	*/

	// método do número dourado

	double a = 0.4;
	double b = 1.7;
	double phi = (1 + sqrt(5)) / 2;
	double x0 = b - (b - a) / phi;
	double x1 = a + (b - a) / phi;

	//cout << x0 << "\t" << x1<<endl;
	ofstream outfile;
	outfile.open("numero_dourado2.txt");

	while (abs(b - a) / (abs(x0) + abs(x1)) > 0.001)
	{
		if (funcao(x0) < funcao(x1))
		{
			b = x1;
		}
		else
		{
			a = x0;
		}
		x0 = b - (b - a) / phi;
		x1 = a + (b - a) / phi;
	
	
	}
	cout << "posicao de equilibrio= "<< "\t"<<(b + a) / 2 << endl;
	outfile << (b + a) / 2 << endl;
	
	
	
	// método do gradiente

	double y0 = 0;
	double lambda = 1;
	double d = funcaolinha(y0);
	double y1 = y0 - lambda * d;
	int k = 0;

	ofstream outfile2;
	outfile2.open("lambda_1.txt");

	while (abs(lambda*d) > pow(10, -5) && k < 10)
	{
		y0 = y1;
		d = funcaolinha(y0);
		y1 = y0 - lambda * d;
		k++;
		outfile2<< k << "\t" << y1 << endl;
	
	}
	cout <<"valor intermedio= "<< y1<< "\t"<<"iteracoes= "<< k<<endl;
	outfile2.close();
	
	/*
	Exercicio 2 utilizar o newton e o método do gradiente	
	*/

	double m = 0;
	ofstream outfile3;
	outfile3.open("exercicio2.txt");

	for(int i = 1; i < 10; i++)
	{
		m = funcao2(i);
		outfile3 << i << "\t" << m <<endl;
		cout<< m <<endl;

	}
	outfile3.close();

	// metodo do gradiente
	double z0 = 1;
	double lambda2 = 0.5;
	double d2 = funcao2linha(z0);
	double z1 = z0 - lambda2 * d2;
	int l = 0;

	ofstream outfile4;
	outfile4.open("Ex2_gradiente.txt");

	while (abs(lambda2*d2) > pow(10, -5) && l < 100)
	{
		z0 = z1;
		d2 = funcao2linha(z0);
		z1 = z0 - lambda2 * d2;
		outfile4 << l << "\t" << z1 << endl;
		l++;
		
	
	}
	cout <<"valor intermedio= "<< z1<< "\t"<<"iteracoes= "<< l<<endl;
	outfile4.close();
	// metodo newton valor intermédio
	double x = 1.8;
	double fk = funcao2linha(x);
	double fklinha = funcao3(x);
	int n = 0;
	double d3 = (fk / fklinha);
	ofstream outfile5;
	outfile5.open("Ex2_newton.txt");
	
	while ( abs(d3) > pow(10, -5) && n <50)
	{
		x = x - d3;
		fk = funcao2linha(x);
		fklinha = funcao3(x);
		d3 = (fk / fklinha);
		outfile5 << x << "\t" << n << endl;
		n++;
		
	
	}
	cout <<"valor intermedio= "<< x<< "\t"<<"iteracoes= "<< n<<endl;
	outfile5.close();

	// metodo gradiente 2D
	
	double xinicial = 5.0;
	double yinicial = -5.0;
	double lambda3 = 0.5;
	double dx = df_dx(xinicial,yinicial);
	double dy = df_dy(xinicial,yinicial);
	double s = xinicial - lambda3*dx;
	double v = yinicial - lambda3*dy;
	int t = 0;
	ofstream outfile6;
	ofstream outfile7;
	ofstream outfile8;
	outfile6.open("Ex2_gradiente2D.txt");
	outfile7.open("Ex2_gradiente2D_x.txt");
	outfile8.open("Ex2_gradiente2D_y.txt");
	
	while( abs(lambda3 * sqrt(pow(dx,2)+pow(dy,2)))>pow(10, -5) && t < 50)
	{
		xinicial = s;
		yinicial = v;
		dx = df_dx(xinicial,yinicial);
		dy = df_dy(xinicial,yinicial);
		s = xinicial - lambda3*dx;
		v = yinicial - lambda3*dy;
		t++;
		outfile6 << v << "\t" << s << endl;
		outfile7 << t << "\t" << s << endl;
		outfile8 << t << "\t" << v << endl;
		
	}
	double valor = sqrt(pow(s,2) + pow(v,2));
	cout << "valor intermedio= "<< valor << "\t"<<"iteracoes= "<< t<<endl;
	outfile6.close();
	outfile7.close();
	outfile8.close();
		

	return 0;
}
