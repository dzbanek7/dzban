/*
 * Garnuszek.lpierwsza.cpp
 */

#include <iostream>
using namespace std;

bool lpierwsza1(int n) {
    
    if(n < 2)
        return false;
    for(int i = 2; i * i <= n; i++)
        if(n % i == 0)
            return false;
    return true;
}

int main(int argc, char **argv)
{
	int n;
    
    cout << "Podaj liczbę: ";
    cin >> n;
    
    if(lpierwsza1(n))
        cout << "Liczba " << n << " należy do liczb pierwszych " << endl;
    else
        cout << "Liczba " << n << " należy do liczb złożonych " << endl;
    
    
    
    
	return 0;
}

