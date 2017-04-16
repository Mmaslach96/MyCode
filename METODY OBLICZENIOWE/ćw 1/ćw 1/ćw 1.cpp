// ConsoleApplication4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	int n = 0, m = 0, i = 0;
	long double g = 1.0;
	double e = 1.0;
	float f = 1.0;

	while (1 + e > 1) {
		e = e / 2;
		n++;
		cout << e << endl;
	}
	cout << "Liczba bitow mantysy dla double=" << n - 1 << endl;

	cout << "=================" << endl;

	while (1 + f > 1) {
		f = f / 2;
		m++;
		cout << f << endl;
	}
	cout << "Liczba bitow mantysy dla floata=" << m - 1 << endl;

	cout << "=================" << endl;

	while (1 + g > 1) {
		g = g / 2;
		i++;
		cout << g << endl;
	}
	cout << "Liczba bitow mantysy dla long double=" << i - 1 << endl;

	cout << "=================" << endl;

	cout << "Dlugosc long double:" << sizeof(long double) << endl;
	cout << "Dlugosc double:" << sizeof(double) << endl;
	cout << "Dlugosc float:" << sizeof(float) << endl;

	system("Pause");
}

