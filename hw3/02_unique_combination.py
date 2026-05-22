# Вантеев Руслан ИИАД_1
def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged or list2[j] != merged[-1]:
                merged.append(list2[j])
            j += 1
        else:
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
            j += 1
    while i < len(list1):
        if not merged or list1[i] != merged[-1]:
            merged.append(list1[i])
        i += 1
    while j < len(list2):
        if not merged or list2[j] != merged[-1]:
            merged.append(list2[j])
        j += 1
    return merged
print("Тест 0: пример")
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)

print("Тест 1: Пустые списки")
print(merge_sorted_lists([], []))                    
print(merge_sorted_lists([1, 2, 3], []))             
print(merge_sorted_lists([], [4, 5, 6]))             

print("Тест 2: С дубликатами внутри списков")
print(merge_sorted_lists([1, 1, 2, 3, 3], [2, 3, 4, 4]))  

print("Тест 3: Полностью одинаковые списки")
print(merge_sorted_lists([1, 2, 3], [1, 2, 3]))           

print("Тест 4: Один список короче другого")
print(merge_sorted_lists([1, 5, 10], [2, 3, 4, 6, 7, 8, 9]))  

print("Тест 5: Отрицательные числа")
print(merge_sorted_lists([-5, -3, 0, 2], [-4, -1, 1, 3]))  
