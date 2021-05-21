array1 = []
for i in range(3, 10, 2):
    for j in range(1, 10, 2):
        array1.append(i * j)
print(array1)

array2 = [i * j for i in range(3, 10, 2) for j in range(1, 10, 2)]
print(array2)