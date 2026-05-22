# Вантеев Руслан ИИАД_1
lst = [x for x in range(15)]
k = int(input("Введите число сдвига: "))

n = len(lst)
k = k % n

lst.reverse()
lst[:k] = lst[:k][::-1]
lst[k:] = lst[k:][::-1]

print(lst)
