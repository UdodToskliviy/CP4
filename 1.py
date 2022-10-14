arr = []



print("Введите длину массива")
lenght = int(input())
print("Введите поочерёдно " + str(lenght) + " элементов массива")
for i in range(lenght):
    arr.append(float(input()))




_max = 0
for i in range(lenght):
    if i == 0:
        _max = arr[i]
    else:
        if arr[i] > _max:
            _max = arr[i]

check = 0

for i in range(lenght):
    if check == 1:
        arr[i] = 0
    if arr[i] == _max:
        check = 1



print(arr)
