# матрица смежности
a = [[0, 1, 1, 0, 0],
     [1, 0, 0, 1, 1],
     [1, 0, 0, 0, 1],
     [0, 1, 0, 0, 0],
     [0, 1, 1, 0, 0]]
# список ребер
b = [[1, 2],
     [1, 3],
     [2, 4],
     [2, 5],
     [3, 5]]
# список смежности
c = [[2, 3],
     [1, 4, 5],
     [1, 5],
     [2],
     [2, 3]]
for i in a:
    print(i)
print()
for i in b:
    print(i)
print()
for i in c:
    print(i)
