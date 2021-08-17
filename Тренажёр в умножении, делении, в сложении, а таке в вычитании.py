from random import *

print("Давай проверим твои знания в умножении, делении, в сложении, а таке в вычитании")
kda = 0
knot = 3
zizni = 3
money = 0
fge = 0
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
                money+=50
            else:
                print("Не повезло, -1 жизнь.")
                zizni -= 1
            print("Хочешь ли ты купить что - то из этого: 1) +1 жизнь - 50, 2) пропустить вопрос - 100, 3) помощь - 200, 4) закончить экзамен - 1000")
            d = int(input())
            if d == 1:
                if money>=50:
                    zizni+=1
                else:
                    print("Тебе не хватает,", 50-money)
            if d == 2:
                if money>=100:
                    continue
                else:
                    print("Тебе не хватает,", 100-money)
            if d == 4:
                if money>=1000:
                    fge+=1
                    break

                else:
                    print("Тебе не хватает,", 1000-money)
            if d == 3:
                if money>=200:
                    print(a//b)
                else:
                    print("Тебе не хватает,", 200-money)
        if fge>=1:
            break
    elif k == 2:
        a = randint(1, 10)
        b = randint(1, 10)
        print("А сможешь правильно посчитать, сколько будет", str(a) + "×" + str(b))
        c = int(input())
        if a * b == c:
            print("Верно!!!")
            kda += 1
            money+=50
        else:
            print("Не повезло, -1 жизнь.")
            zizni -= 1
        print(
            "Хочешь ли ты купить что - то из этого: 1) +1 жизнь - 50, 2) пропустить вопрос - 100, 3) помощь - 200, 4) закончить экзамен - 1000")
        d = int(input())
        if d == 1:
            if money >= 50:
                zizni += 1
            else:
                print("Тебе не хватает,", 50 - money)
        if d == 2:
            if money >= 100:
                continue
            else:
                print("Тебе не хватает,", 100 - money)
        if d == 4:
            if money >= 1000:
                fge += 1
                break

            else:
                print("Тебе не хватает,", 1000 - money)
        if d == 3:
            if money >= 200:
                print(a * b)
            else:
                print("Тебе не хватает,", 200 - money)
    if fge >= 1:
        break
    elif k == 3:
        a = randint(1, 10)
        b = randint(1, 10)
        print("А сможешь правильно посчитать, сколько будет", str(a) + "+" + str(b))
        c = int(input())
        if a + b == c:
            print("Верно!!!")
            kda += 1
            money+=50
        else:
            print("Не повезло, -1 жизнь.")
            zizni -= 1
        print(
            "Хочешь ли ты купить что - то из этого: 1) +1 жизнь - 50, 2) пропустить вопрос - 100, 3) помощь - 200, 4) закончить экзамен - 1000")
        d = int(input())
        if d == 1:
            if money >= 50:
                zizni += 1
            else:
                print("Тебе не хватает,", 50 - money)
        if d == 2:
            if money >= 100:
                continue
            else:
                print("Тебе не хватает,", 100 - money)
        if d == 4:
            if money >= 1000:
                fge += 1
                break

            else:
                print("Тебе не хватает,", 1000 - money)
        if d == 3:
            if money >= 200:
                print(a + b)
            else:
                print("Тебе не хватает,", 200 - money)
    if fge >= 1:
        break
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
                money+=50
            else:
                print("Не повезло, -1 жизнь.")
                zizni -= 1
            print(
                "Хочешь ли ты купить что - то из этого: 1) +1 жизнь - 50, 2) пропустить вопрос - 100, 3) помощь - 200, 4) закончить экзамен - 1000")
            d = int(input())
            if d == 1:
                if money >= 50:
                    zizni += 1
                else:
                    print("Тебе не хватает,", 50 - money)
            if d == 2:
                if money >= 100:
                    continue
                else:
                    print("Тебе не хватает,", 100 - money)
            if d == 4:
                if money >= 1000:
                    fge += 1
                    break

                else:
                    print("Тебе не хватает,", 1000 - money)
            if d == 3:
                if money >= 200:
                    print(a - b)
                else:
                    print("Тебе не хватает,", 200 - money)
        if fge >= 1:
            break
else:
    print("У тебя кончились жизни.")
    print("Ты ответил(а) на", kda, "вопросов верно")
