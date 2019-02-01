/*
 * dec2bin.cpp
 */


#include <iostream>
using namespace std;

void dec2bin(int l, int tab[9]) {
    int lbin = 0;
    
}

int dec2bin(int l)
{
    int lbin = 0;
    int i = 1;
    
    while (l > 0)
    {
        lbin += (l%2)*i;
        l = l/2;
        i *= 10;
    }
    return lbin;
}
    
void dec2dec(int tab[]) {
    ;
}

int main(int argc, char **argv)
{
	
	return 0;
}

