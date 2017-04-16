// æw 5.cpp: Okreœla punkt wejœcia dla aplikacji konsoli.
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
using namespace std;

void wypiszMacierz(double macierz[4][4])
{
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cout << macierz[i][j] << "\t";
		}
		cout << endl;
	}
	cout << endl;
}

void wypiszWektor(double wektor[4])
{
	for (int i = 0; i < 4; i++)
	{
		cout << wektor[i] << endl;
	}
	cout << endl;
}

int maxBezwgledna(double macierz[4][4], int i, int j)
{
	int k = 0;
	int maxindeks = i;
	if (maxindeks == 3)
	{
		return maxindeks;
	}

	for (k = i + 1; k < 4; k++)
	{
		if (abs(macierz[k][j]) > abs(macierz[maxindeks][j]))
		{
			maxindeks = k;
		}
	}
	return maxindeks;
}

void zmienRzad(double macierz[4][4], int j1, int j2, double wektor[4])
{
	double tmp;

	for (int i = 0; i < 4; i++)
	{
		tmp = macierz[j1][i];
		macierz[j1][i] = macierz[j2][i];
		macierz[j2][i] = tmp;
	}
	tmp = wektor[j1];
	wektor[j1] = wektor[j2];
	wektor[j2] = tmp;
}

void czesciowyWybor(double macierz[4][4], int i, int j, double wektor[4])
{
	zmienRzad(macierz, maxBezwgledna(macierz, i, j), j, wektor);
}

void metodaGausa(double macierz[4][4], int ip, int jp)
{
	for (int i = ip + 1; i < 4; i++)
	{
		macierz[i][jp] = macierz[i][jp] / macierz[ip][jp];
		for (int j = jp + 1; j < 4; j++)
		{
			macierz[i][j] = macierz[i][j] - macierz[i][jp] * macierz[ip][j];
		}
	}

}

void rozwiazL(double macierz[4][4], double L[4], double wektor[4])
{
	for (int i = 0; i < 4; i++)
	{
		double sum = 0.0;
		for (int j = 0; j < i; j++)
		{
			sum += macierz[i][j] * L[j];
		}
		L[i] = (wektor[i] - sum); // /1.0 (bo na przekatnej sa jedynki)
	}
}

void rozwiazU(double macierz[4][4], double U[4], double wektor[4])
{
	for (int i = 3; i >= 0; i--)
	{
		double sum = 0.0;
		for (int j = i + 1; j < 4; j++)
		{
			sum += macierz[i][j] * U[j];
		}
		U[i] = (wektor[i] - sum) / macierz[i][i];
	}
}


int main()
{
	double macierzA[4][4] =
	{
		{ 1.0,  20.0, -30.0,  -4.0},
		{ 4.0,  20.0,  -6.0,  50.0},
		{ 9.0, -18.0,  12.0, -11.0},
		{16.0, -15.0,  14.0, 130.0}
	};
	double wektorB[4] = { 0,114,-5,177 };
	double wektorL[4];
	double wektorU[4];

	wypiszMacierz(macierzA);
	wypiszWektor(wektorB);


	for (int i = 0; i < 4; i++)
	{

		if (macierzA[i][i] == 0)
		{
			cout << "Czesciowy wybor " << i << ", " << i << endl;
			czesciowyWybor(macierzA, i, i, wektorB);
		}

		wypiszMacierz(macierzA);

		cout << "Eliminacja Gausa: " << i << ", " << i << endl;
		metodaGausa(macierzA, i, i);
		wypiszMacierz(macierzA);
	}

	cout << "Wektor B po zamianach" << endl;
	wypiszWektor(wektorB);

	rozwiazU(macierzA, wektorU, wektorB);

	cout << "wektor U" << endl;
	wypiszWektor(wektorU);

	rozwiazL(macierzA, wektorL, wektorU);

	cout << "wektor L" << endl;
	wypiszWektor(wektorL);

	system("Pause");
    return 0;
}

/*
Ax=b
macierz L ma jedynki na przek¹tnej
funkcja która robi rozk³¹d LU macierzy A
wybór elementu podstawowego (zamiana wierszy)
wektor b i macierz A i rozwi¹zujemy uk³ad równañ
b siê zmienia z ka¿dym krokiem
*/
