#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int N_particulas = 5;
	int particulas_a_mover = 1;
	double R = 1.0;
	double x_in = -R;
	double d_epsi = 1.5;
	double v_in = 1.0;
	double tmax = 40;// tempo maximo
	double d_fronteira = 8.75 - d_epsi / 2 * (N_particulas - 5); // tamanho da caixa

	double raio_particulas[N_particulas + 2];
	for (int j = 0; j <= N_particulas + 2; j++)
	{
		raio_particulas[j] = R;
	}


	double dij = 0;
	int dij_norma = 0;
	double vel = 0;
	double tij = 0;
	double t_colisao = pow(10, 6);

	vector<int> colisao;

	int n1 = 0;
	int n2 = 0;
	double vn1 = 0;
	double vn2 = 0;
	double t_total = 0;


	double v[N_particulas + 2] = { 0 };
	double r[N_particulas + 2] = {};
	r[0] = x_in;

	double d = 2 * R;

	ofstream file;
	file.open("dados1.txt");

	file << t_total<<"\t";
	// posicoes iniciais
	for (int i = 1; i <= particulas_a_mover; i++)
	{
		r[i] = r[i - 1] + d;
		file << r[i]<<"\t";
		v[i] = v_in;
		d = 2 * R + d_epsi;
		//cout << " posicoes iniciais" << endl;
		//cout << "particula" << "\t" << i << "\t" << "posicao" << "\t" << r[i] << endl;
	}

	d = d_fronteira + 2 * R + d_epsi;

	for (int n = particulas_a_mover + 1; n <= N_particulas; n++)
	{
		r[n] = r[n - 1] + d;
		file << r[n]<<"\t";
		d = 2 * R + d_epsi;
		//cout << "particula" << "\t" << n << "\t" << "posicao" << "\t" << r[n] << endl;
	}
		
	file << endl;
		r[N_particulas + 1] = r[N_particulas] + d_fronteira + 2 * R + d_epsi*(particulas_a_mover);
		//cout << "particula " << "\t" << N_particulas + 1 << "\t" << " posicao " << "\t"  << r[N_particulas + 1] << endl;
		

		for (int n = 0; n < N_particulas + 2; n++)
		{
			//cout << "paricula" << "\t" << n << "\t" << "velocidade" << "\t"  << v[n] << endl;
		}
	


		for (int t = 0; t < tmax; t++)
		{
			//cout << "tempo" << "\t" << t << endl;


			for (int n = 0; n <= N_particulas; n++)
			{
				dij = r[n + 1] - r[n];
				
				vel = v[n + 1] - v[n];

				if (vel < 0)
				{	
					tij = (raio_particulas[n] + raio_particulas[n + 1]-dij) / vel;
					if (tij == t_colisao)
					{
						colisao.push_back(n);
					}
					if (tij < t_colisao)
					{
						t_colisao = tij;
						colisao.clear();
						colisao.push_back(n);
					}
				}
			}
			//cout << "tempo de colisao" << "\t" << t_colisao << endl;
			t_total += t_colisao;
			file << t_total<<"\t";
			for (int n = 1; n <= N_particulas; n++)
			{
				r[n] += v[n] * t_colisao;
				file << r[n]<<"\t";
			}
			file << endl;
				

			for (int j = 0; j < colisao.size(); j++)
			{
				n1 = colisao[j];
				n2 = colisao[j] + 1;

				// condicoes de fronteira
				if (n2 == N_particulas + 1 and v[n1] > 0)
				{
					v[n1] = -v[n1];
					goto end;
				}
				if (n1 == 0 and v[n2] < 0)
				{
					v[n2] = -v[n2];
					goto end;
				}

				vn1 = v[n1];
				vn2 = v[n2];
				v[n1] = vn2;
				v[n2] = vn1;




			}
		end:
			colisao.clear();
			t_colisao = pow(10, 10);
		}
		file.close();
	
		return 0; 
}