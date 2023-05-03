import math
import scipy
from scipy.special import gammaincc


def main():
    bits = '11000000110101110101010100010111011010011000000111101011011000100011100100000111100001100101111111110001101101101110010001100111'

    num_blocks = 128 // 8
    mas_count = []
    for i in range(16):
        block = bits[i * 8: (i + 1) * 8]
        one = 0
        max_one_in_block = 0
        max_run = 0
        for bit in block:
            if bit == '1':
                one += 1
                max_one_in_block = max(max_one_in_block, one)
            else:
                one = 0
        max_run = max(max_run, max_one_in_block)
        mas_count.append(max_run)
    print(mas_count)
    v1 = sum(x <= 1 for x in mas_count)
    v2 = sum(x == 2 for x in mas_count)
    v3 = sum(x == 3 for x in mas_count)
    v4 = sum(x > 4 for x in mas_count)
    k0 = 0.2148
    k1 = 0.3672
    k2 = 0.2305
    k3 = 0.1875
    X = ((v1-16*k0)**2)/(16*k0)+((v2-16*k1)**2)/(16*k1) + \
        ((v3-16*k2)**2)/(16*k2)+((v4-16*k3)**2)/(16*k3)
    P=gammaincc(3/2,X/2)
    print(P)
    #0.1689840897545613
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")
    
if __name__ == "__main__":
    main()
#Тест пройден успешно