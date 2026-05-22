# Вантеев Руслан ИИАД_1
def caesar_cipher(text, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    
    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_lower = char.lower()
            
            old_index = alphabet.index(char_lower)
            new_index = (old_index + shift) % len(alphabet)
            new_char = alphabet[new_index]
            
            result += new_char.upper() if is_upper else new_char
        else:
            result += char
    
    return result


message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

encrypted = caesar_cipher(message, shift)
print(f'Зашифрованное сообщение: {encrypted}')
