/*
 * suma-cyfr.cpp
 * 
 * Copyright 2018  <>
 */

#include <iostream>
using namespace std;

int sumuj_cyfry1(int liczba) {
    
    int suma = 0;
    
    while (liczba > 0) {
    
        suma += liczba % 10;
        liczba = liczba / 10;
        
    }

    return suma;
}

def sumuj_cyfry2(liczba) {
    
        
    
}


int main(int argc, char **argv)
{
	int liczba = 0;  //deklaracja i inicjacja
    //liczba = 0;  //inicjacja
    
    while (liczba < 10) {
        
        cout << "Podaj minimum liczbę dwucyfrową: ";
        cin >> liczba;
    }
    
    cout << "Suma: " << sumuj_cyfry1(liczba) << endl;
    
    return 0;
}

