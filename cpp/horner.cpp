/*
 * horner.cpp
 * W(x) = 2 x^3 + 3x^2 + 5x + 4 => 6
 * W(x) = x(2x^2 + 3x + 5) + 4 
 * w(x) = x(x(2x+ 3) + 5) + 4 => 3
 * 
 */

#include <iostream>
using namespace std;

void drukujw(int st, float tb[]) {
    // 2x^3 + 3x^2 + 5x + 4 
    int i;
    for(i = 0; i < st; i++) 
        cout << tb[i] << "x^" << st-i << " + ";
    cout << tb[i] << endl;
        
    }

float horner_it(float x, int stopien, float tbwsp[]){
    // x(x(2x+ 3) + 5) + 4
    float wynik;
    wynik = tbwsp[0];
    
    for(int i = 1; i < stopien + 1; i++)
        wynik = wynik * x + tbwsp[i];
    
    
    
    return wynik;
     }
// horner_re(2, 3, tbwsp);
// horner_re(2, 2, tbwsp) * 2 + 4
// horner_re(2, 1, tbwsp) * 2 + 5
// horner_re(2, 0, tbwsp) * 2 + 3
// 2
// 2 * 2 + 3 = 7
// 7 * 2 + 5 = 19
// 19 * 2 + 4 = 42
// 42


float horner_re(float x, int stopien, float tbwsp[]) {
    // x(x(2x+ 3) + 5) + 4
    if (stopien == 0)
        return tbwsp[0];
    return horner_re(x, stopien - 1, tbwsp) * x + tbwsp[stopien];
}


int main(int argc, char **argv)
{
    int stopien = 0;
    float *tbwsp; // wspaźnik typu rzeczywistego rozpoznać można po * (wspaxnik zawiera adres pamięci)
    float x =0;
	cout << "Stopień wielomianu: ";
    cin >> stopien;
    
    tbwsp = new float [stopien + 1];
    //cout << tbwsp;
    
    for(int i=0; i <= stopien; i++){
        cout << "Podaj współczynnik przy najwyższej potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
        }
    
    cout << "Argument:  ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "wynosi: " << horner_it(x, stopien, tbwsp);
    cout << "wynosi: " << horner_re(x, stopien, tbwsp);
    
	return 0;
}
