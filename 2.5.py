from random import *

print("Давай проверим твои знания в умножении, делении, в сложении, а таке в вычитании")
kda = 0
knot = 3
zizni = 3
while not (zizni <= 0):
    k = randint(1, 4)
    if k == 1:
        a = 10
        b = 3
        while not a % b == 0:
            a = randint(1, 10)
            b = randint(1, 10)
        else:
            print("А сможешь правильно посчитать, сколько будет", str(a) + ":" + str(b))
            c = int(input())
            if a // b == c:
                print("Верно!!!")
                kda += 1
            else:
                print("Не повезло, -1 жизнь.")
                zizni -= 1
    elif k == 2:
        a = randint(1, 10)
        b = randint(1, 10)
        print("А сможешь правильно посчитать, сколько будет", str(a) + "×" + str(b))
        c = int(input())
        if a * b == c:
            print("Верно!!!")
            kda += 1
        else:
            print("Не повезло, -1 жизнь.")
            zizni -= 1
    elif k == 3:
        a = randint(1, 10)
        b = randint(1, 10)
        print("А сможешь правильно посчитать, сколько будет", str(a) + "+" + str(b))
        c = int(input())
        if a + b == c:
            print("Верно!!!")
            kda += 1
        else:
            print("Не повезло, -1 жизнь.")
            zizni -= 1
    elif k == 4:
        a = 0
        b = 10
        while not (a - b > 0):
            a = randint(1, 10)
            b = randint(1, 10)
        else:
            print("А сможешь правильно посчитать, сколько будет", str(a) + "-" + str(b))
            c = int(input())
            if a - b == c:
                print("Верно!!!")
                kda += 1
            else:
                print("Не повезло, -1 жизнь.")
                zizni -= 1
else:
    print("У тебя кончились жизни.")
    print("Ты ответил(а) на", kda, "вопросов верно")
