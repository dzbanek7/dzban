/*
 * nieparzyste.cpp
 */


#include <iostream>

using namespace std;

int wypisz(int n) {
    int i = 1;
    for(i =! n; i++){
        i = i + 2;
    }
    return i;
}


int main(int argc, char **argv)
{
	int n;
    cout << "Podaj dowolną liczbę naturalną:";
    cin >> n;
    cout << "liczby: " << wypisz(n) << endl;
	return 0;
}

