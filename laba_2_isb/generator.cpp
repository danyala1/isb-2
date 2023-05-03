#include <iostream>
#include <random>
#include <bitset>
using namespace std;
int main()
{
    random_device rd;
    mt19937_64 generator(rd());

    bitset<128>  bits;
    for (int i = 0; i < 128; i++) {
        bits[i] = generator() & 1;
    }

    cout << "Random number: " << bits.to_string() << std::endl;

    return 0;
}
//Random number: 11110001001110111010000111010110000001100000101111011000101000101001010010101101101011000110001001110100001000000111010000011101