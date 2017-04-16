// æw 5 with class.cpp: Okreœla punkt wejœcia dla aplikacji konsoli.
//
#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

class Wektor{
public:
	size_t W;
	double *wektorB;
	double *y;
	double *x;
public:
	Wektor::Wektor(size_t W);
	void wpiszWektor();
	void wypiszWektor(double *wektor);
};

Wektor::Wektor(size_t W) : W(W)
{
	y = new double[W];
	x = new double[W];
	wektorB= new double[W];
	wpiszWektor();
}

void Wektor::wpiszWektor()
{
	wektorB[0] = 0;
	wektorB[1] = 114;
	wektorB[2] = -5;
	wektorB[3] = 177;
}

void Wektor::wypiszWektor(double *wektor)
{
	for (int i = 0; i < 4; i++)
	{
		cout << wektor[i] << endl;
	}
	cout << endl;
}



class Macierz :public Wektor{
public:
	size_t M, N;
	double **macierzA = new double *[M];
	double **macierzL = new double *[M];
public:
	Macierz(size_t M, size_t N, size_t W);
	void wpisz();
	void wypiszMacierz(double **macierz);
	bool czesciowyWybor(int x, int indeks[4]);
	void dekompozycjaLU();
};

Macierz::Macierz(size_t M, size_t N, size_t W) : M(M), N(N), Wektor(W)
{
	for (int i = 0; i < M; i++)
	{
		macierzA[i] = new double[N];
		macierzL[i] = new double[N];
	}
	wpisz();
}
void Macierz::wypiszMacierz(double **macierz)
{
	for (size_t i = 0; i<M; ++i)
	{
		for (size_t j = 0; j<N; ++j)
		{
			cout << macierz[i][j] << ("\t");
		}
		cout << endl;
	}
}

void Macierz::wpisz()
{
	macierzA[0][0] = 1.0;	macierzA[0][1] = 20.0;	macierzA[0][2] = -30.0;	macierzA[0][3] = -4.0;
	macierzA[1][0] = 4.0;	macierzA[1][1] = 20.0;	macierzA[1][2] = -6.0;	macierzA[1][3] = 50.0;
	macierzA[2][0] = 9.0;	macierzA[2][1] = -18.0;	macierzA[2][2] = 12.0;	macierzA[2][3] = -11.0;
	macierzA[3][0] = 16.0;	macierzA[3][1] = -15.0;	macierzA[3][2] = 14.0;	macierzA[3][3] = 130.0;

	macierzL[0][0] = 1;	macierzL[0][1] = 0;	macierzL[0][2] = 0;	macierzL[0][3] = 0;
	macierzL[1][0] = 0;	macierzL[1][1] = 1;	macierzL[1][2] = 0;	macierzL[1][3] = 0;
	macierzL[2][0] = 0;	macierzL[2][1] = 0;	macierzL[2][2] = 1;	macierzL[2][3] = 0;
	macierzL[3][0] = 0;	macierzL[3][1] = 0;	macierzL[3][2] = 0;	macierzL[3][3] = 1;
}

bool Macierz::czesciowyWybor(int x, int indeks[4])
{
	double max = 0;
	int indeks_max = x, temp;
	bool znaleziono = false;

	for (int i = x; i < 4; ++i)
	{
		if (fabs(macierzA[indeks[i]][x]) > max)
		{
			max = fabs(macierzA[indeks[i]][x]);
			indeks_max = i;
			znaleziono = true;
		}
	}

	if (znaleziono)
	{
		temp = indeks[indeks_max];
		indeks[indeks_max] = indeks[x];
		indeks[x] = temp;
	}

	return znaleziono;
}

void Macierz::dekompozycjaLU()
{
	double wspl, temp;
	int indeksy[4];
	int n = 4, i, j, k;


	for (i = 0; i < n; ++i)
		indeksy[i] = i;


	wpisz();
	cout << "Macierz A:" << endl;
	wypiszMacierz(macierzA);
	cout << endl;
	cout << " Wektor b:" << endl;
	wypiszWektor(wektorB);
	cout << endl;

	for (i = 0; i < 3; i++)
	{
		for (j = i + 1; j < 4; j++)
		{
			if (macierzA[indeksy[i]][indeksy[i]] == 0)
			{
				if (!czesciowyWybor(i, indeksy))
				{
					break;
				}
			}

			macierzL[j][i] = macierzA[indeksy[j]][i] / macierzA[indeksy[i]][i];
			cout << "Macierz L:" << endl;
			wypiszMacierz(macierzL);
			cout << macierzL[j][i] << endl;
			wspl = macierzA[indeksy[j]][i] / macierzA[indeksy[i]][i];
			for (k = i; k < 4; k++)
			{
				macierzA[indeksy[j]][k] = macierzA[indeksy[j]][k] - macierzA[indeksy[i]][k] * wspl; //U
			}
			cout << " Macierz U" << endl;
			wypiszMacierz(macierzA);
			cout << endl;
		}
	}

	for (i = 0; i < 4; ++i)
	{
		macierzL[indeksy[i]][i] = 1;
	}

	cout << " Macierz U:" << endl;
	wypiszMacierz(macierzA);
	cout << endl;
	cout << " Macierz L:" << endl;
	wypiszMacierz(macierzL);
	cout << endl;
	cout << " Wektor b:" << endl;
	wypiszWektor(wektorB);
	cout << endl;

	for (i = 0; i < 4; i++)
	{
		temp = 0;
		for (j = 0; j < i; j++)
		{
			temp += macierzL[indeksy[i]][j] * y[indeksy[j]];
		}
		y[indeksy[i]] = (wektorB[indeksy[i]] - temp);
	}

	cout << " Wektor b: " << endl;
	wypiszWektor(wektorB);
	cout << endl;

	cout << " Wektor y: " << endl;
	wypiszWektor(y);
	cout << endl;

	for (i = n - 1; i >= 0; i--)
	{
		temp = 0.0;
		for (j = i + 1; j < 4; j++)
		{
			temp += macierzA[indeksy[i]][j] * x[indeksy[j]];
		}

		if (macierzA[indeksy[i]][i] == 0)
			macierzA[indeksy[i]][i] = 0;

		x[indeksy[i]] = (1 / macierzA[indeksy[i]][i]) *(y[indeksy[i]] - temp);

	}

	cout << " Wektor x: " << endl;
	wypiszWektor(x);
	cout << endl;

	for (i = 0; i < n; i++)
	{
		delete[] macierzA[i];
		delete[] macierzL[i];
	}

	delete[] macierzA;
	delete[] macierzL;
	delete[] wektorB;
	delete[] x;
	delete[] y;
}


int main()
{
	Macierz m(4, 4, 4);
	m.wpisz();
	m.dekompozycjaLU();

	system("Pause");
	return 0;
}
