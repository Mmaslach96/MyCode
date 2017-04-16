// æw4.cpp: Okreœla punkt wejœcia dla aplikacji konsoli.
//

#include "stdafx.h"
#include <iostream>
#include <math.h>
#include <iomanip>
#include <fstream>

const int literacji = 50;
const double e = 1e-15;

using namespace std;

double funkcja1(double x, double y, double z)
{
	return x * x + y * y + z * z - 2;
}
double funkcja2(double x, double y)
{
	return x * x + y * y - 1;
}
double funkcja3(double x, double y)
{
	return x * x - y;
}

double norma(double x, double y, double z)
{
	return fabs(x) > fabs(y) ? fabs(x) > fabs(z) ? fabs(x) : fabs(z) : fabs(y) > fabs(z) ? fabs(y) : fabs(z);
}

double wyznacznik(double(&tab)[3][3])
{
	return	tab[0][0] * tab[1][1] * tab[2][2] + tab[0][1] * tab[1][2] * tab[2][0] + tab[0][2] * tab[1][0] * tab[2][1] - tab[0][2] * tab[1][1] * tab[2][0] - tab[0][0] * tab[1][2] * tab[2][1] - tab[0][1] * tab[1][0] * tab[2][2];
}


int main()
{
	ofstream plik;
	plik.open("wyniki.txt");
	cout.precision(5);
	double x, y, z, detX, detY, detZ, f1, f2, f3, Jacobi[3][3], tabsupp[3][3], detJacobi, estymator, residuum;
	double X = 0;
	double Y = 0;
	double Z = 0;

	x = 2;
	y = 5;
	z = 1;


	cout << "lp:     x:                 y:                     z:                   estymator:                     residuum: " << endl;
	if (plik.is_open())
	{
		for (int i = 0; i < literacji; ++i)
		{
			f1 = funkcja1(x, y, z);
			f2 = funkcja2(x, y);
			f3 = funkcja3(x, y);

			//liczenie normy masksimum estymatora i residuum
			estymator = norma(X, Y, Z);
			residuum = norma(f1, f2, f3);

			//Jakobian(tabela pochodnych)
			Jacobi[0][0] = 2 * x;
			Jacobi[0][1] = 2 * y;
			Jacobi[0][2] = 2 * z;
			Jacobi[1][0] = 2 * x;
			Jacobi[1][1] = 2 * y;
			Jacobi[1][2] = 0;
			Jacobi[2][0] = 2 * x;
			Jacobi[2][1] = -1;
			Jacobi[2][2] = 0;



			//liczenie wyznacznika Jakobianu
			detJacobi = wyznacznik(Jacobi);
			//przypisujemy tablicy pomocniczej wartosci funkcji
			tabsupp[0][0] = f1;
			tabsupp[1][0] = f2;
			tabsupp[2][0] = f3;
			for (int j = 0; j < 3; ++j)
			{
				for (int k = 1; k < 3; ++k)
				{
					tabsupp[j][k] = Jacobi[j][k];
				}
			}
			//liczymy wyznacznik dla X
			detX = wyznacznik(tabsupp);


			//przypisujemy tablicy pomocniczej wartosci funkcji
			tabsupp[0][1] = f1;
			tabsupp[1][1] = f2;
			tabsupp[2][1] = f3;
			for (int j = 0; j < 3; ++j)
			{
				for (int k = 0; k < 3; ++k)
				{
					if (k != 1)
					{
						tabsupp[j][k] = Jacobi[j][k];
					}
				}
			}
			//liczymy wyznacznik dla Y
			detY = wyznacznik(tabsupp);


			//przypisujemy tablicy pomocniczej wartosci funkcji
			tabsupp[0][2] = f1;
			tabsupp[1][2] = f2;
			tabsupp[2][2] = f3;

			for (int j = 0; j < 3; ++j)
			{
				for (int k = 0; k < 2; ++k)
				{
					tabsupp[j][k] = Jacobi[j][k];
				}
			}
			//liczymy wyznacznik dla Z
			detZ = wyznacznik(tabsupp);



			//dzielenie wyznacznikow X,Y,Z przez wyznacznik Jakobianu
			X = detX / detJacobi;
			Y = detY / detJacobi;
			Z = detZ / detJacobi;

			x = x - X;
			y = y - Y;
			z = z - Z;

			cout << i;
			cout << x << cout.width(11);
			cout << y << cout.width(17);
			cout << z << cout.width(22);
			cout << estymator << cout.width(26);
			cout << residuum << cout.width(30) << endl;

			plik << i << "\t";
			plik << estymator << "\t";
			plik << residuum << "\t" << endl;

			if (fabs(f1) < e && fabs(f2) < e && fabs(f3) < e && estymator < e)
			{
				break;
			}
		}
	}
	else
	{
		cout << "Nie polaczono z plikiem " << endl;
	}
	
	system("Pause");
	return 0;
}

//klase do wektorów xn+1=xn-(f(xn)/f'(xn))
//macierz jacobiego - macierz sk³¹daj¹ca siê z macierzy pochodnych
//nie liczyæ odwrotnoœci

//takie same jak w 3
//residuum (wart bzwgl z roznicy)