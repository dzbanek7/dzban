/*
 * szyfr_cezara.cxx
 */

#include <iostream>
using namespace std;

#define MAKS 100

//~void deszyfruj(char tb[], int klucz) {
    //~klucz = klucz % 26;
    //~int i = 0;
    //~int kod = 0;
    //~while (tb[i] != '\0') {
        //~;
    //~}
//~}



void szyfruj(char tb[], int klucz) {
    klucz = klucz % 26;
    int i = 0;
    int kod = 0;
    while (tb[i] != '\0') {
        kod = (int)tb[i] + klucz;
        if (tb[i] == ' ') {
            kod -= klucz;
        } else if(kod > 122) {
            kod -= 26;
        }
        cout << (char)kod;
        tb[i] = (char)kod;
        i++;
    }
    cout << endl;
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

