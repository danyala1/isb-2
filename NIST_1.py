from math import sqrt
from scipy.special import erfc


def main():
    bits = '11000000110101110101010100010111011010011000000111101011011000100011100100000111100001100101111111110001101101101110010001100111'
    # кол-во единиц и нулей 
    ones = bits.count('1')
    zeros = bits.count('0')
    summ = ones+zeros*(-1)
    # статистика теста
    S = summ/sqrt(128)
    # Вероятность равна
    P = erfc(S / sqrt(2))
    # уровень значимости проверка (0.01)
    print(P)
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")
#0.7236736098317631
if __name__ == "__main__":
    main()
# Тест пройден успешно