// æw 3.cpp: Okreœla punkt wejœcia dla aplikacji konsoli.


#include "stdafx.h"
#include <iostream>
#include <math.h>
#include <iomanip>
#include <fstream>



const int literacji = 30;  //liczba iteracji
const double e = 1e-17;

using namespace std;


void Picarda(double(*funkcja)(double), double(*fi)(double), double xn)
{
	int i;
	double x1, f0, estymator;
	cout << endl;

		for (i = 0; i <= literacji; i++)
		{
			f0 = fabs(funkcja(xn));
			x1 = fi(xn);
			estymator = fabs(x1 - xn);
			xn = x1;

			cout << i;
			cout << xn << cout.width(16);
			cout << estymator << cout.width(24);
			cout << f0 << cout.width(32) << endl;
			if (estymator < e || f0 < e)
			{
				break;
			}
		}
		cout << " \n x" << i <<" = " << xn << endl << endl;
}


void Bisekcji(double(*funkcja)(double), double a, double b)
{
	int i;
	double estymator, xn, fn;
	cout << endl;

		for (i = 0; i < literacji; i++)
		{
			xn = (a + b) / 2;
			estymator = fabs(b - a) / 2;
			fn = funkcja(xn);
			if (funkcja(a)*fn < 0)
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
			cout << fabs(fn) << cout.width(32) << endl;
			if (estymator < e || fabs(fn) < e)
			{
				break;
			}
		}
		cout << " \n x" << i << " = " << xn << endl << endl;
}


void Newtona(double(*funkcja)(double), double(*pochodna)(double), double xn)
{
	int i;
	double fn, x1, estymator;
	cout << endl;
		for (i = 0; i < literacji; i++)
		{
			x1 = xn;
			fn = funkcja(x1);
			xn = x1 - fn / pochodna(x1);
			estymator = fabs(x1 - xn);
			cout << i;
			cout << xn << cout.width(16);
			cout << estymator << cout.width(24);
			cout << fabs(fn) << cout.width(32) << endl;
			if (estymator < e || fabs(fn) < e)
			{
				break;
			}
		}
		cout << " \n x" << i << " = " << xn << endl << endl;
}


void Siecznych(double(*funkcja)(double), double x0, double x1)
{
	int i;
	double x2, estymator, f2;
	cout << endl;
		for (i = 0; i < literacji; i++)
		{
			x2 = x0 - funkcja(x0) / ((funkcja(x0) - funkcja(x1)) / (x0 - x1));
			x1 = x0;
			x0 = x2;
			f2 = fabs(funkcja(x0));
			estymator = fabs(x0 - x1);
			cout << i;
			cout << x2 << cout.width(16);
			cout << estymator << cout.width(24);
			cout << f2 << cout.width(32) << endl;

			if (estymator < e || f2 < e)
			{
				break;
			}
		}
		cout << " \n x" << i << " = " << x2 << endl << endl;
}

int main()
{
	cout.precision(5);
	cout << endl << "Funkcja sin(x/4)*sin(x/4)-x" << endl << endl;

	cout<< "Picarda:";
	Picarda([](double x)->double {return sin(x / 4)*sin(x / 4) - x; }, [](double x)->double {return sin(x / 4)*sin(x / 4); }, 5);

	cout << "Bieskcji:";
	Bisekcji([](double x)->double {return sin(x / 4)*sin(x / 4) - x; }, -15, 15);

	cout << "Newtona:";
	Newtona([](double x)->double {return sin(x / 4)*sin(x / 4) - x; }, [](double x)->double {return (1 / 4)*sin(x / 2) - 1; }, 5);

	cout << "Siecznych:";
	Siecznych([](double x)->double {return sin(x / 4)*sin(x / 4) - x; }, 3, 2);




	cout << endl << "Funkcja tab(2*x)-x-1" << endl << endl;
	
	cout << "Picarda:";
	Picarda([](double x)->double {return tan(2 * x) - x - 1; }, [](double x)->double {return tan(2 * x) - 1; }, 0.1);

	cout << "Bieskcji:";
	Bisekcji([](double x)->double {return tan(2 * x) - x - 1; }, 0, 0.7);

	cout << "Newtona:";
	Newtona([](double x)->double {return tan(2 * x) - x - 1; }, [](double x)->double {return 2 / (cos(2 * x) * cos(2 * x)) - 1; }, -1);

	cout << "Siecznych:";
	Siecznych([](double x)->double {return tan(2 * x) - x - 1; }, -1, -1.5);

	

	system("pause");
	return 0;
}


//liczba iteracji
//wartosc funkcja jest mniejsza ni¿ tolerancja(wartosc bliska 0) (estymator)
//roznica pomiedzy przyblizeniami jest mniejsza ni¿ tolerancja (rezziduum)

//estymator b³edu ró¿nica miêdzy kolejnymi przybli¿eniami
//ressidum wartosc bezwgledna x = 0

//numer iteracji, wartosc, rezdzium etymator do pliku lub wypisuje