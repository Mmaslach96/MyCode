// æw 3.cpp: Okreœla punkt wejœcia dla aplikacji konsoli.


#include "stdafx.h"
#include <iostream>
#include <math.h>
#include <iomanip>
#include <fstream>



const int literacji = 50;  //liczba iteracji
const double e = 1e-12;

using namespace std;

double funkcja(double xn, int n)
{
	if (n == 1) 
	{
		return sin(xn / 4)*sin(xn / 4) - xn;
	}
	else if (n == 2)
	{
		return tan(2 * xn) - xn - 1;
	}
	else return 0;
}

double fi(double xn, int n)
{
	if (n == 1)
	{
		return sin(xn / 4)*sin(xn / 4);
	}
	else if (n == 2)
	{
		return tan(2 * xn) - 1;
	}
	else return 0;
}

double pochodna(double xn, int n)
{
	if (n == 1)
	{
		return (1 / 4)*sin(xn / 2) - 1;
	}
	else if (n == 2)
	{
		return 2 / (cos(2 * xn)*cos(2 * xn)) - 1;
	}
	else return 0;
}

void Picarda(double xn, int n, string nazwa)
{
	ofstream plik;
	plik.open(nazwa);
	int i;
	double x1, residuum, estymator;
	cout << endl;
	cout << "lp:         xn:                   estymator:                         residuum:" << endl;
	if (plik.is_open())
	{
		for (i = 0; i < literacji; i++)
		{
			residuum = fabs(funkcja(xn, n));
			x1 = fi(xn, n);
			estymator = fabs(x1 - xn);
			xn = x1;

			cout << i;
			cout << xn << cout.width(16);
			cout << estymator << cout.width(24);
			cout << fabs(residuum) << cout.width(32) << endl;
			plik << i << "\t";
			plik << estymator << "\t";
			plik << residuum << "\t" << endl;
			if (estymator < e || residuum < e)
			{
				break;
			}
		}
		cout << " \n xn = " << xn << endl << endl;
	}
	else
	{
		cout << "Nie polaczono z plikiem " << endl;
	}
}


void Bisekcji(double a, double b, int n, string nazwa)
{
	ofstream plik;
	plik.open(nazwa);
	int i;
	double estymator, xn, residuum;
	cout << endl;
	cout << "lp:         xn:                   estymator:                         residuum:" << endl;
	if (plik.is_open())
	{
		for (i = 0; i < literacji; i++)
		{
			xn = (a + b) / 2;
			estymator = fabs(b - a) / 2;
			residuum = funkcja(xn, n);
			if (funkcja(a, n)*residuum < 0)
			{
				b = xn;
			}
			else
			{
				a = xn;
			}
			cout << i;
			cout << xn << cout.width(16);
			cout << estymator << cout.width(24);
			cout << fabs(residuum) << cout.width(32) << endl;
			plik << i << "\t";
			plik << estymator << "\t";
			plik << residuum << "\t" << endl;
			if (estymator < e || fabs(residuum) < e)
			{
				break;
			}
		}
		cout << " \n xn = " << xn << endl << endl;
	}
	else
	{
		cout << "Nie polaczono z plikiem " << endl;
	}
}


void Newtona (double xn, int n, string nazwa)
{
	ofstream plik;
	plik.open(nazwa);
	int i;
	double residuum, x1, estymator;
	cout << endl;
	cout << "lp:         xn:                   estymator:                         residuum:" << endl;
	if (plik.is_open())
	{
		for (i = 0; i < literacji; i++)
		{
			x1 = xn;
			residuum = funkcja(x1, n);
			xn = x1 - residuum / pochodna(x1, n);
			estymator = fabs(x1 - xn);
			cout << i;
			cout << xn << cout.width(16);
			cout << estymator << cout.width(24);
			cout << fabs(residuum) << cout.width(32) << endl;
			plik << i << "\t";
			plik << estymator << "\t";
			plik << residuum << "\t" << endl;
			if (estymator < e || fabs(residuum) < e)
			{
				break;
			}

		}
		cout << " \n xn = " << xn << endl << endl;
	}
	else
	{
		cout << "Nie polaczono z plikiem " << endl;
	}
}


void Siecznych(double x0, double x1, int n, string nazwa)
{
	ofstream plik;
	plik.open(nazwa);
	int i;
	double xn, estymator, residuum;
	cout << endl;
	cout << "lp:         xn:                   estymator:                         residuum:" << endl;
	if (plik.is_open())
	{
		for (i = 0; i < literacji; i++)
		{
			xn = x1 - (funkcja(x1, n) / ((funkcja(x1, n) - funkcja(x0, n)) / (x1 - x0)));
			x0 = x1;
			x1 = xn;
			residuum = fabs(funkcja(x0, n));
			estymator = fabs(x0 - x1);
			cout << i;
			cout << xn << cout.width(16);
			cout << estymator << cout.width(24);
			cout << residuum << cout.width(32) << endl;
			plik << i << "\t";
			plik << estymator << "\t";
			plik << residuum << "\t" << endl;
			if (estymator < e || residuum < e)
			{
				break;
			}
		}
		cout << " \n xn = " << xn << endl << endl;
	}
	else
	{
		cout << "Nie polaczono z plikiem " <<endl;
	}
}

int main()
{
	cout << endl << "Funkcja sin(x/4)*sin(x/4)-x" << endl << endl;

	cout<< "Picarda:";
	Picarda(7, 1,"Picard 1.txt");

	cout << "Bieskcji:";
	Bisekcji(-4.5, 10, 1,"Bisekcji 1.txt");

	cout << "Newtona:";
	Newtona(3, 1,"Newstona 1.txt");

	cout << "Siecznych:";
	Siecznych(3, 7, 1, "Siecznych 1.txt");



	cout << endl << "Funkcja tan(2*x)-x-1" << endl << endl;
	
	cout << "Picarda:";
	Picarda(1, 2, "Picard 2.txt");

	cout << "Bieskcji:";
	Bisekcji(-0.5,1.5 , 2, "Bisekcji 2.txt");

	cout << "Newtona:";
	Newtona(1, 2, "Newstona 2.txt");

	cout << "Siecznych:";
	Siecznych(0.8, 1.5, 2, "Siecznych 2.txt");



	system("pause");
	return 0;
}


//liczba iteracji
//wartosc funkcja jest mniejsza ni¿ tolerancja(wartosc bliska 0) (estymator)
//roznica pomiedzy przyblizeniami jest mniejsza ni¿ tolerancja (rezziduum)

//estymator b³edu ró¿nica miêdzy kolejnymi przybli¿eniami
//ressidum wartosc bezwgledna x = 0

//numer iteracji, wartosc, rezdzium etymator do pliku lub wypisuje