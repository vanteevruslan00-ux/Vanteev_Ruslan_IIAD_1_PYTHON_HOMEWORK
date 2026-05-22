# Вантеев Руслан ИИАД_1
def sum_n(n):
    x = n
    res = 0
    while n > 0:
        res += (n%10)
        n //= 10
    print("сумма цифр в", x, ":", res)
    return res

def dif(n):
    x = n
    k = 0
    while n > 0:
        k += 1
        n //= 10
    print("количесто цифр в", x, ":", k)
    return k
m = int(input('Введите число: '))
print("разность суммы цифр и количества цифр в числе", m, ":", sum_n(m) - dif(m))
