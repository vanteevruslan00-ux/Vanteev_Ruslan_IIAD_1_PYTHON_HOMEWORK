# Вантеев Руслан ИИАД_1
numbers = [x for x in range(15)]
new_numbers = []
print("Исходный список:", numbers)
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        new_numbers.append(numbers[i])
print(new_numbers)
