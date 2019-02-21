/*
 * szyfr_cezara.cpp 
 */

using namespace std;

#include <iostream>
#include <string.h>
#define MAKS 100

void deszyfruj(char tb[], int klucz){
    klucz = klucz % 26;
    int i = 0;
    int kod = 0;
    while (tb[i] != '\0'){
        kod = (int)tb[i] - klucz;
        if (tb[i] == ' '){
            kod += klucz;
        } else if (kod > 122){
            kod += 26;
        }
        cout << (char)kod;
        tb[i]= (char)kod;
        i++;
    }
    cout << endl;
    }

void szyfruj(char tb[], int klucz){
   int ile = strlen(tb);
   //ile znakow uzupelnic kropkami i uzupeklnic tekst tyki kropkami
}

int main(int argc, char **argv)
{
	char tekst[MAKS];
    int klucz = 0;
    
    cout << "Podaj tekst w małych literach: " << endl;
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(tekst, klucz);
    deszyfruj(tekst, klucz);
	return 0;
}
