# Вантеев Руслан ИИАД_1
star_spisok = [3070, 2060, 3090, 3070, 3090, 3080, 2040, 3090, 2050]
def video(lst):
    print("старый список видеокарт:", lst)
    max_el = max(lst)
    new_lst = [x for x in lst if x != max_el]
    print("Новый список видеокарт:", new_lst)
video(star_spisok)
