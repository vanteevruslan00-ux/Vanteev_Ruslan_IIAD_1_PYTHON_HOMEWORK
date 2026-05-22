# Вантеев Руслан ИИАД_1
text = input('Введите строку: ')

first_h = text.index('h')

last_h = text.rindex('h')


middle = text[first_h + 1:last_h]

reversed_middle = middle[::-1]

result = text[:first_h + 1] + reversed_middle + text[last_h:]

print(f'Развёрнутая последовательность между первым и последним h: {reversed_middle}')
