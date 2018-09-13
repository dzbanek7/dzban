/*
 * szablon.cpp
 */


#include <iostream>

using namespace std;

int dodaj(int a, int b)
{
        return a + b;
}

int roznica(int a, int b)
{
        return a - b;
}

int iloczyn(int a, int b)
{
        return a * b;
}

int iloraz(int a, int b)
{
        return a / b;
}

int main(int argc, char **argv)
{
	float a, b; //deklaracja zmiennej
    a = b = 0; //inicjacja zmiennej
    
    cout << "Podaj 1. liczbę: ";
    cin >> a;
    cout << a << endl;
    
    cout << "Podaj 2. liczbę: ";
    cin >> b;
    cout << b << endl;
    
    cout << "Suma: " << dodaj(a, b) << endl;
    cout << "Różnica: " << roznica(a, b) << endl;
    cout << "Iloczyn: " << iloczyn(a, b) << endl;
    cout << "Iloraz: " << iloraz(a, b) << endl;
    
    
    
	return 0;
}

