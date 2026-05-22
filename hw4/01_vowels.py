# Вантеев Руслан ИИАД_1
def extract_vowels(text):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    vowels_list = [char.lower() for char in text if char in vowels]
    return vowels_list, len(vowels_list)


text = input('Введите текст: ')
vowels_list, count = extract_vowels(text)

print(f'\nСписок гласных букв: {vowels_list}')
print(f'Длина списка: {count}')
