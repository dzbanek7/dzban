/*
 * Garnuszek_petle_cw01.cpp
 */

#include <iostream>
using namespace std;

int cw1() {
    // dla i, które na poczatku równa się 10 i jest mniejsze od 99 zwiekszamy i o 1. Następnie dzielimy i modulo przez 2, gdy ten wynik jest równy 0, to suma= 0 + wartości i
    int suma = 0;

    for(int i = 10; i <= 99; i++)
    {
           if ( i % 2 == 0 ) suma=suma+i;         
    }
    
    return suma;
}

void cw2() {
    int a;
    int b;
    int c;
    cin >> a;
    cin >> b;
    cin >> c;
    while(a+b!=c) {
    a = b;
    b = c;
    cin >> c;    
    }
    cout << c;    
}

int main(int argc, char **argv)
{
    //~cout << "Suma wszystkich parzystych liczb dwucyfrowych to: " << cw1() << endl;
	cw2();
    return 0;
}

