# Вантеев Руслан ИИАД_1
skates_count = int(input('Кол-во коньков: '))
skates = [int(input(f'Размер {i+1}-й пары: ')) for i in range(skates_count)]

people_count = int(input('\nКол-во людей: '))
people = [int(input(f'Размер ноги {i+1}-го человека: ')) for i in range(people_count)]

skates.sort()
people.sort()

happy_people = 0
skate_idx = 0

for person_size in people:

    while skate_idx < len(skates) and skates[skate_idx] < person_size:
        skate_idx += 1
    
    if skate_idx < len(skates):
        happy_people += 1
        skate_idx += 1

print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {happy_people}')
