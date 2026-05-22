# Вантеев Руслан ИИАД_1
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    
    action = input("Гость пришёл или ушёл? ").strip().lower()
    
    if action == "пора спать":
        break
    
    if action not in ["пришёл", "ушёл"]:
        print("Пожалуйста, введите 'пришёл', 'ушёл' или 'Пора спать'")
        continue
    
    name = input("Имя гостя: ").strip()
    
    if action == "пришёл":
        if len(guests) < 6:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    
    elif action == "ушёл":
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"Гостя с именем {name} нет на вечеринке")

print("\nВечеринка закончилась, все легли спать.")
