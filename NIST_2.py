from math import sqrt
from scipy.special import erfc


def main():
    bits = '11000000110101110101010100010111011010011000000111101011011000100011100100000111100001100101111111110001101101101110010001100111'
    # кол-во единиц и нулей
    f = bits.count('1') /128
    zeros = bits.count('0') 
    runs = [bits[0]]
    for i in range (1,128):
        if bits[i] != bits[i-1]:
            runs.append(bits[i])
    num = len(runs)
    # вероятность
    P = erfc( abs(num-2*128*f*(1-f))/(2*sqrt(2*128)*f1*(1-f)) )
    # уровень значимости (0.01)
    print(P)
    # 0.6032105431220571, получается случайная последовательность
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")

if __name__ == "__main__":
    main()
#тест пройден успешно