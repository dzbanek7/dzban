/*
 * znaki.cpp
 */


#include <iostream>
using namespace std;

void licz_znaki(char tb[], int roz) {
    //~for(int i = 0; i < roz; i++) {
        //~cout << tb[i];
    //~}
    int i = 0;
    int biale, inter, reszta;
    biale = inter = reszta = 0;
    while (tb[i] != '\0') {
        //~if (tb[i] == ' ' || tb[i] == '\t') biale++;
        //~else if (tb[i] == ',' || tb[i] == '.') inter++;
        //~else reszta++;
        switch (tb[i]) {
            case ' ':
            case '\t':
                biale++;
            break;
            case ',':
            case '.':
                inter++;
            break;
            default:
                reszta++;

        }
        i++; //inkrementacja index-u
    }
    cout << "Białych: " << biale << endl;
    cout << "Interpu: " << inter << endl;
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

