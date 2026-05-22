# Вантеев Руслан ИИАД_1
n = int(input('Кол-во чисел: '))
sequence = []
for i in range(n):
    num = int(input('Число: '))
    sequence.append(num)

print(f'\nПоследовательность: {sequence}')

def is_palindrome(arr):
    return arr == arr[::-1]

numbers_to_add = []

for i in range(len(sequence)):
    suffix = sequence[i:]
    
    if is_palindrome(suffix):
        numbers_to_add = sequence[:i][::-1]
        break

print(f'Нужно приписать чисел: {len(numbers_to_add)}')
print(f'Сами числа: {numbers_to_add}')

result_sequence = sequence + numbers_to_add
print(f'Симметричная последовательность: {result_sequence}')
