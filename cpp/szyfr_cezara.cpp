/*
 * szyfr_cezara.cxx
 */

#include <iostream>
using namespace std;

#define MAKS 100

void szyfruj(char tekst[], int klucz) {
    int kod = 0;
    for(int i = 0; i < MAKS; i++) {
        kod = (int)tekst[i];
        
    }
}

int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;
    cout << "Podaj tekst: ";
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    cout << "Szyfr cezara do tekstu: " << endl;
    szyfruj(tekst, klucz);
	return 0;
}

