arr1 = []
print("Введите длину массива 1")
lenght1 = int(input())
print("Введите поочерёдно " + str(lenght1) +  " элементов массива 1")
for i in range(lenght1):
    arr1.append(int(input()))



arr2 = []
print("Введите длину массива 2")
lenght2 = int(input())
print("Введите поочерёдно " +str(lenght2) + " элементов массива 2")
for i in range(lenght2):
    arr2.append(int(input()))



set1 = set(arr1)
set2 = set(arr2)

print(list(set1&set2))
