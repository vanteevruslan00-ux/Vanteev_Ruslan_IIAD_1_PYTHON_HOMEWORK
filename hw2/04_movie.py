# Вантеев Руслан ИИАД_1
import sys
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorites = []
n = int(input("Введите количество фильмов: "))
if n > len(films):
    print("Нет такого количества фильмов")
    sys.exit()
for i in range(n):
    found = False
    title = input("Введите название фильма: ")
    for film in films:
        if film.lower() == title.lower():
            found = True
            break
    if found: favorites.append(title)
    else: print("Ошибка: фильма", title, "у нас нет :(")
if favorites: print(f"ваш список любимых фильмов:", ",".join(favorites))
else: print("Ваш список любимых фильмов пуст")
