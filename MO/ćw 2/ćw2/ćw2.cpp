// ConsoleApplication4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

double tab1[3900] = { 0 };  // log(x)
double tab2[3900] = { 0 };  // x
double tab3[3900] = { 0 };  // wd
double tab4[3900] = { 0 };  // blad wzgledny
double tab5[3900] = { 0 };  // wartos przyblizona
double tab6[3900] ;  // f(x) taylorem
double tab7[3900] ;  // blad wzgledny(taylor)
double tab8[3900];
double tab9[3900];

void blad(double x, double wd, int i) 
{
	double wp,blad;
	wp = (1 - exp(-x))/x;
	blad = abs((wp-wd)/wd);
	tab4[i] = blad;
	tab5[i] = wp;
}

void bladTaylor(double tab6, double wd, int i)
{
	tab7[i] = abs((tab6 - wd) / wd);
}

double szeregTaylora(double x, int n)
{	
	double suma = 1.0; 
	double silnia = 1.0;
	double potega = 1.0;  

	if (x > 0)
	{
		for (int i = 2; i <= n; ++i)
		{

			silnia = silnia * i;
			potega = potega*x;
			suma = suma + (potega/ silnia);
		}
		return suma;
	}
	return 1 / szeregTaylora(-x, n);
}



int main()
{
	int i = 0;
	ifstream plik;
	plik.open("plik.txt");

	while (!plik.eof())
	{
		plik >> tab1[i] >> tab2[i] >> tab3[i];
		i++;
	}

	for (i = 0; i < 3900; i++)
	{
		blad(tab2[i], tab3[i], i);
		tab6[i] = szeregTaylora(-tab2[i], 70);
		bladTaylor(tab6[i], tab3[i], i);
	}
	for (i = 0; i < 3900; i++)
	{
		if (tab4[i] != 0 && tab2[i]<1e-5)
		{
			tab8[i] = tab6[i];
			tab9[i] = tab7[i];
		}
		else
		{
			tab8[i] = tab5[i];
			tab9[i] = tab4[i];
		}
	}



	/*cout << "       x        |         Wd          |          Wp          |       Blad wzgledny        |            Taylor          |        Blad wzgledny(Taylor)" << endl;
	cout << "------------------------------------------------------------------------------------------------------------------------------------------------------------" << endl;
	for (i = 0; i < 3900; i++)
	{
			
		cout.width(7);
		cout << tab2[i];
		cout.width(14);
		cout << tab3[i];
		cout.width(21);
		cout << tab5[i];
		cout.width(28);
		cout << tab4[i];
		cout.width(35);
		cout << tab6[i];
		cout.width(42);
		cout << tab7[i] << endl;
		cout << endl;
	}*/
	cout << " Hybryda f(x)   |  Hybryda b³¹d wzglêdny   " << endl;
	for (i = 0; i < 3900; i++)
	{
		cout.width(15);
		cout << tab8[i];
		cout.width(30);
		cout << tab9[i] << endl;
	}
	system("Pause");
}

