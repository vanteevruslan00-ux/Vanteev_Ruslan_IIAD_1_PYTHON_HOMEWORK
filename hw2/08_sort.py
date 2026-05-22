# Вантеев Руслан ИИАД_1
def quicksort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    pivot = arr[mid]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    quicksort(arr, left, j)
    quicksort(arr, i, right)


arr = [1, 4, -3, 0, 10]

print("Изначальный список:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Отсортированный список:", arr)
