/*
 * tabliczka.cxx
 */
 
#include <iostream>
#include <iomanip>

using namespace std;

void tabliczka(int x, int y) { 
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j<= y; j++) {
            cout << setw(4) << i * j << " ";
        }
        cout << endl;
    }
}

int main(int argc, char **argv)
{
	int a, b; // deklaracja 
    a = b = 0; // inicjacja 
    //int a = 0; // definicja 
    cout << "Podaj zakres 1: ";
    cin >> a;
    cout << "Podaj zakres 2: ";
    cin >> b;
    tabliczka(a, b);
	return 0;
}

