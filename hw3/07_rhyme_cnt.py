# Вантеев Руслан ИИАД_1
n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {k}-й человек\n')

people = list(range(1, n + 1))
current_index = 0

while len(people) > 1:
    print(f'Текущий круг людей: {people}')
    print(f'Начало счёта с номера {people[current_index]}')
    
    remove_index = (current_index + k - 1) % len(people)
    removed_person = people.pop(remove_index)
    
    print(f'Выбывает человек под номером {removed_person}\n')
    
    current_index = remove_index if remove_index < len(people) else 0

print(f'Остался человек под номером {people[0]}')
