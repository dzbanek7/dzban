/*
 * figury.cpp
 */


#include <iostream>

using namespace std;

void prostokat2(a, b, znak) {
    
    
    int  = 0;
    for (int i = 0; i < a - 1 i++) {
        for (int j = 0; j - 1; j++) {
                if (i != j && i != k && j != k) {
                    cout << i << j << k << " "; 
                    ile++;
                }
        }
    }
    return ile;
}

int main(int argc, char **argv)
{
	int a, b; // deklaracja 
    a = b = 0; // inicjacja 
    //int a = 0; // definicja 
    cout << "Podaj bok 1: ";
    cin >> a;
    cout << "Podaj bok 2: ";
    cin >> b;
    
    char znak;
    cout << "Podaj znak: ";
    cin >> znak;
    
    prostokat2(a, b, znak);
	return 0;
}

