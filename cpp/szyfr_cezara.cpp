/*
 * szyfr_cezara.cxx
 */

#include <iostream>
using namespace std;

#define MAKS 100

void deszyfruj(char tekst[], int klucz, int n){
    klucz%= 26;

    for(int i=0;i<n;i++){
        int litera= (int) tekst[i];
        if(litera!=32){
        litera-=klucz;

        if(litera<97){
            litera+=26;
        }
        tekst[i]=(char)litera;

    }
    cout<<tekst[i];
}


}



void szyfruj(char tb[], int klucz) {
    klucz = klucz % 26;
    int i = 0;
    int kod = 0;
    while (tb[i] != '\0') {
        kod = (int)tb[i];
        if (tb[i] == ' ') {
            ;
        } else if (kod < 91) {
            kod += klucz;
            if (kod > 90) kod -= 26;
        } else {
            kod += klucz;
            if (kod > 122) kod -= 26;
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
    //int n=cin.gcount()-1;
    szyfruj(tekst, klucz);
    //~deszyfruj(tekst, klucz, n);
	return 0;
}

