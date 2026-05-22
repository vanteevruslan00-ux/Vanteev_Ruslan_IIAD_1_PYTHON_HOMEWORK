# Вантеев Руслан ИИАД_1
lst_1 = [1, 5, 3]
lst_2 = [1, 5, 1, 5]
lst_3 = [1, 3, 1, 5, 3, 3]

lst_1.extend(lst_2)
count_5 = lst_1.count(5)

print(f"Кол-во цифр 5 при первом объединении: {count_5}")

while 5 in lst_1:
    lst_1.remove(5)
lst_1.extend(lst_3)
count_3 = lst_1.count(3)

print(f"Кол-во цифр 3 при втором объединении: {count_3}")
print(f"Итоговый список: {lst_1}")
