a = int(input("Сколько дел тебе надо сделать? "))
b = []
for i in range(a):
    b.append(input())
for i in enumerate(b, 1):
    print(str(i[0]) + ")", i[1])
while not len(b) == 0:
    d = input("Хочешь ли ты удалить задачу? ")
    if d == "да":
        c = int(input("Номер задачи, которую надо удалить ")) - 1
        b.remove(b[c])
        for i in enumerate(b, 1):
            print(str(i[0]) + ")", i[1])
    g = input("Хочешь ли ты добавить задачу? ")
    if g == "да":
        b.append(input())
