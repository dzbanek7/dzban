/*
 * znaki.cpp
 */


#include <iostream>
using namespace std;

void zamien_znaki(char tb[]. int roz) {
        for(int i = 0; i < roz; i++) {
            //zamień małe na duże;
            kod_ascii 'a' = 97
            kod ascii 'A' = 65
            97 - 65 = 32
            (char)(kod_ascii - 32)
            todo: implementacja
        }
}

void licz_znaki(char tb[], int roz) {
    int i = 0;
    int cyfry, literyD, literyM, reszta;
    cyfry = literyD = literyM = reszta = 0;
    int znak_kod = 0; // kod ASCII badanego znaku
    
    while (tb[i] != '\0') {
        znak_kod = (int)tb[i];
        if (znak_kod > 64 && znak_kod < 91)
            literyD++;
        else if (znak_kod > 96 && znak_kod < 123)
            literyM++;
        else if (znak_kod > 47 && znak_kod < 58)
            cyfry++;
        else 
            reszta++;

        
        i++; //inkrementacja index-u
    }
    cout << "Duże: " << literyD << endl;
    cout << "Małe: " << literyM << endl;
    cout << "Cyfry: " << cyfry << endl;
    cout << "Reszta: " << reszta << endl;
}

int main(int argc, char **argv)
{   
    const int rozmiar = 20;
    char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    licz_znaki(znaki, cin.gcount());
    return 0;
}

