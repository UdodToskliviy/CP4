arr = []

print("Введите длину массива")
lenght = int(input())
print("Введите поочерёдно " + str(lenght) + " элементов массива")
for i in range(lenght):
    arr.append(int(input()))

print("Введите delta")
delta = int(input())

_min = 0
for i in range(lenght):
    if i == 0:
        _min =arr[i]
    else:
        if arr[i] < _min:
            _min = arr[i]

ans = 0
for i in range(lenght):
    if arr[i] - _min == delta:
        ans += 1

print(ans)
