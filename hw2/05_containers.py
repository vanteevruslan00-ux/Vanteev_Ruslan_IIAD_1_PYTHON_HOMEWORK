# Вантеев Руслан ИИАД_1
containers = []
k = int(input("Введите количество контейнеров: "))
for i in range(k):
    weight = int(input("ведите вес контейнера(в килограммах): "))
    if weight > 200:
        print("Вес контейнера должен быть меньше 200 килограмм")
    else:
        containers.append(weight)
containers.sort(reverse=True)
new_container = int(input("Введите вес нового контейнера: "))
flag = False
for i in range(len(containers)):
    if new_container > containers[i]:
        containers.insert(i, new_container)
        print("Номер, который получит контейнер: ", i+1)
        flag = True
        break
if flag == False:
    containers.append(new_container)
    print("Номер, который получит контейнер: ", (len(containers)))
print(containers)
    
