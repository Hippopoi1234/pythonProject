n, m = map(int, input().split())
office = []
for i in range(2 * n + 1):
    office.append(list(input()))
graf_from_office = []
for i in office:
    temp_list = []
    for j in i:
        if j == "#":
            temp_list.append(0)
        else:
            temp_list.append(1)
    graf_from_office.append(temp_list)
print(graf_from_office)
# матрица смежности
# a = [[0, 1, 1, 0, 0],
#      [1, 0, 0, 1, 1],
#      [1, 0, 0, 0, 1],
#      [0, 1, 0, 0, 0],
#      [0, 1, 1, 0, 0]]
# # список ребер
# b = [[1, 2],
#      [1, 3],
#      [2, 4],
#      [2, 5],
#      [3, 5]]
# # список смежности
# c = [[2, 3],
#      [1, 4, 5],
#      [1, 5],
#      [2],
#      [2, 3]]
# for i in a:
#     print(i)
# print()
# for i in b:
#     print(i)
# print()
# for i in c:
#     print(i)
