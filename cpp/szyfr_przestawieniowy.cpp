/*
 * szyfr_cezara.cxx
 */

#include <iostream>
#include <string.h> // strlen()
using namespace std;

#define MAKS 100

void deszyfruj(){

}



void szyfruj(char tb[], int klucz) {
    int ile = strlen(tb);
    // ile znaków uzupełnić kropkami, uzupełnić tekst kropkami
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
    //int n=cin.gcount()-1;
    szyfruj(tekst, klucz);
    //~deszyfruj(tekst, klucz, n);
	return 0;
}

