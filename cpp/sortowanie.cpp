/*
 * sortowanie.cpp
 */

#include <iostream>
#include <cstdlib>
using namespace std;

void wypelnij(int tab[], int roz) {
    srand(time(NULL)); // INICJACJIA generatora liczb pseudolosowych
    for(int i = 0; i < roz; i++) {
        //~cout << rand() << endl;
        tab[i] = rand() % 101;
    }
}

void zamien1(int &a, int &b) {
    cout << a << " " << b << endl;
    int tmp = a;
    a = b;
    b = tmp;
    cout << a << " " << b << endl;
}

void drukuj(int tab[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
}

void sort_bubble(int tab[], int n) {
    for (;;) {
        for (;;) {
            //~if (tab[i] > tab[i+1])
                //~zamien1(tab[i], tab[i+1]);
        }
    }
}

int main(int argc, char **argv)
{
	int roz = 20;
    int tab[roz];
    wypelnij(tab, roz);
    drukuj(tab, roz);
    tab[0] = 7;
    tab[1] = 5;
    zamien1(tab[0], tab[1]);
    cout << tab[0] << " " << tab[1];
	return 0;
}

