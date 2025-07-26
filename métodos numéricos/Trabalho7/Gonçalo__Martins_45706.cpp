#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include <math.h>
#include <vector>

using namespace std;

double f(double y)
{
	return (-2.3*y);


}
/*EDO's* exercicio 2*/
double dy( double t , double v0, double theta)
{
	return ((v0*sin(theta)-9.8*t));
}
double dx( double v0, double theta)
{
	return v0 * cos(theta);
}
/*equacoes do movimento*/
double px(double t, double v0, double theta)
{
	return v0*cos(theta)*t;
}
double py(double t, double v0, double theta)
{
	return v0*sin(theta)*t - 9.8*0.5*pow(t, 2);
}

double Euler( double x0, double x_max, double h)
{
	ofstream file;
	file.open("Euler_h=0.7.txt");
	int n = (int)((x_max-x0)/h);
	
	double y[n]= {0.0};
	y[0]=1.0;
	for( int i = 0; i<n+1;i++)
	{
			
		
		y[i+1]=y[i]+f(y[i])*h;
		file<<x0<<"\t"<<y[i]<<endl;
		x0+=h;
		
			
	}
	file.close();
	
	return y[n-1];
}


double Runge_Kutta(double x0, double x_max,double h)
{
	ofstream file;
	file.open("Runge_Kutta_h=0.7.txt");
	int n = (int)((x_max-x0)/h);
	double y[n]= {0.0};
	y[0]={1.0};
	double k1;
	double k2;
	double k3;
	double k4;	
	for( int i = 0; i<n+1;i++)
	{
		k1 = f(y[i]);
		k2 = f(y[i]+k1*h*0.5);
		k3 = f(y[i]+k2*h*0.5);
		k4 = f(y[i]+k3*h);
		y[i+1] = y[i] +(h/6)*(k1+2*k2+2*k3+k4);
		file<<x0<<"\t"<<y[i]<<endl;
		x0+=h;
		
	}

	return y[n-1];

	

}

int main()
{
	
	
	double h=0.7;
/*{0.5,0.7,1.0} para o Euler 1a) para os dois metodos 1b)
{1,0.5,0.25,0.0125,0.625,0.02777776,0.015625}*/
	double erro_Euler = 0;
	double erro_Runge_Kutta = 0;
	double x_max = 5.0;
	double x0 = 0.0;
	Euler(x0, x_max, h);
	Runge_Kutta(x0, x_max, h);
	/*int N = 0;
	double h2[7]={1,0.5,0.25,0.0125,0.625,0.02777776,0.015625};
	ofstream file2;
	file2.open("erro_Euler.txt");
	ofstream file3;
	file3.open("erro_Runge_Kutta.txt");
	while(N<7)
	{
		erro_Euler = abs(Euler(x0,x_max,h2[N])-2.3*5);
		erro_Runge_Kutta = abs(Runge_Kutta(x0,x_max,h2[N])-2.3*5);
		file2<<erro_Euler<<"\t"<<log(h2[N])<<endl;
		file3<<erro_Runge_Kutta<<"\t"<<log(h2[N])<<endl;
		N++;
	}
	*/

	/*
	exercicio 2, velocidade inicial 20 m/s com um angulo pi/4
	*/
	/*
	double h = 0.5;
	double v0 = 20;
	double pi = 4 * atan(1);
	double theta = pi / 4;
	double x0 = 0.0;
	double x_max = 5.0;
	int n = (int)((x_max - x0) / h);
	*/
	/*Runge_Kutta*/
	/*ofstream file4;
	file4.open("Ex2_Runge_Kutta.txt");
	double y[n] = { 0.0 };
	double x[n] = { 0.0 };
	double k1_y, k1_x;
	double k2_y, k2_x;
	double k3_y, k3_x;
	double k4_y, k4_x;
	for (int i = 0; i < n + 1 ; i++)
	{
		k1_y = dy(x0,v0,theta);
		k2_y = dy(x0+0.5*h,v0,theta);
		k3_y = dy(x0+h*0.5,v0,theta);
		k4_y = dy(x0+h,v0,theta);
		k1_x = dx(v0, theta);
		k2_x = dx(v0, theta);
		k3_x = dx(v0, theta);
		k4_x = dx(v0, theta);
		y[i + 1] = y[i] + (h / 6)*(k1_y + 2 * k2_y + 2 * k3_y + k4_y);
		x[i + 1] = x[i] + (h / 6)*(k1_x + 2 * k2_x + 2 * k3_x + k4_x);
		file4 << x0 << "\t" << y[i] << "\t" << x[i] << endl;
		x0 += h;

	}*/
	/*Euler*/
	/*
	ofstream file5;
	file5.open("Ex2_Euler.txt");

	double y1[n] = { 0.0 };
	double x1[n] = { 0.0 };
	for (int i = 0; i < n + 1; i++)
	{


		y1[i + 1] = y1[i] + dy(x0,v0,theta)*h;
		x1[i + 1] = x1[i] + dx(v0,theta)*h;
		file5 << x0 << "\t" << y1[i] << "\t" << x1[i] << endl;
		x0 += h;


	}
	file5.close();
	double solx[12];
	double soly[12];
	double jj = 0.0;
	ofstream file6;
	file6.open("Ex2_Sol.txt");
	for (int j = 0; j <= 12; j++)
	{
		solx[j] = px(jj, v0, theta);
		soly[j] = py(jj, v0, theta);
		file6<< soly[j] << "\t" << solx[j] << endl;
		jj += 0.5;
	}
	file6.close();
	*/
	return 0;
}
