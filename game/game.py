import time, random
import json

with open('teams.json', "r+", encoding='utf8') as tf:
    teams = json.load(tf)
with open('players.json', "r+", encoding='utf8') as pl:
    players = json.load(pl)


def week(gk, cb, cm, st, gk1, cb2, cm3, st4):
    print("Началась новая неделя, напиши да, если хочешь начать матч:")
    input()
    u = random.randint(0, len(w) - 1)
    print(f"Твой противник на эту неделю - {w[u]}")
    input()
    print("Подсчитаем средний OVR на всех позициях в твоей команде:")
    k_gk = 0
    for i in gk:
        k_gk += players[i]
    k_cb = 0
    for i in cb:
        k_cb += players[i]
    k_cm = 0
    for i in cm:
        k_cm += players[i]
    k_st = 0
    for i in st:
        k_st += players[i]
    t_1 = k_gk // len(gk)
    t_2 = k_cb // len(cb)
    t_3 = k_cm // len(cm)
    t_4 = k_st // len(st)
    input()
    print(f"Вратарь - {t_1}")
    input()
    print(f"Защита - {t_2}")
    input()
    print(f"Полузащита - {t_3}")
    input()
    print(f"Атака - {t_4}")
    print("Теперь подсчитаем тоже самое, но у твоего противника:")
    gk = teams[w[u]]["Goalkeeper"]
    cb = teams[w[u]]["Defenders"]
    cm = teams[w[u]]["Midfielders"]
    st = teams[w[u]]["Strikers"]
    k_gk = 0
    for i in gk:
        k_gk += players[i]
    k_cb = 0
    for i in cb:
        k_cb += players[i]
    k_cm = 0
    for i in cm:
        k_cm += players[i]
    k_st = 0
    for i in st:
        k_st += players[i]
    t1 = k_gk // len(gk)
    t2 = k_cb // len(cb)
    t3 = k_cm // len(cm)
    t4 = k_st // len(st)
    input()
    print(f"Вратарь - {t1}")
    input()
    print(f"Защита - {t2}")
    input()
    print(f"Полузащита - {t3}")
    input()
    print(f"Атака - {t4}")
    schet_you = 0
    schet_prt = 0
    input()
    if t_1 > t1:
        schet_you += 1
        print("Твой вратарь лучше, чем вратарь твоих противников")
    elif t1 > t_1:
        schet_prt += 1
        print("Твой вратарь хуже вратаря противников")
    else:
        print("Твой вратарь такой же сильный, как и вратарь противников")
    input()
    if t_2 > t2:
        schet_you += (t_2 - t2) // 3
        print("Твоя защита лучше, чем защита твоих противников")
    elif t2 > t_2:
        schet_prt += (t2 - t_2) // 3
        print("Твоя защита хуже защиты противников")
    else:
        schet_prt += 1
        schet_you += 1
        print("Твоя защита такая же сильная, как и защита противников")
    input()
    if t_3 > t3:
        schet_you += (t_3 - t3) // 2
        print("Твоя полузащита лучше, чем полузащита твоих противников")
    elif t3 > t_3:
        schet_prt += (t3 - t_3) // 2
        print("Твоя полузащита хуже полузащиты противников")
    else:
        schet_prt += 2
        schet_you += 2
        print("Твоя полузащита такая же сильная, как и полузащита противников")
    input()
    if t_4 > t4:
        schet_you += t_4 - t4
        print("Твоя атака лучше, чем атака твоих противников")
    elif t4 > t_4:
        schet_prt += t4 - t_4
        print("Твоя атака хуже атаки противников")
    else:
        print("Твоя атака такая же сильная, как и атака противников")
    input()
    if schet_you > schet_prt:
        print(f"Ты победил со счетом {schet_you}:{schet_prt}")
    elif schet_you < schet_prt:
        print(f"Ты проиграл со счетом {schet_you}:{schet_prt}")
        print("Внимание!!! Поскольку ваша команда проиграла матч, мы даем вам поддержку")
        input()
        t11 = random.randint(1, 4)
        t22 = 0
        if t11 == 1:
            t22 = random.randint(0, len(gk1) - 1)
            print(f"Мы дадим поддержку вашему вратарю {gk1[t22]}! +1 OVR")
            players[gk1[t22]] += 1
        elif t11 == 2:
            t22 = random.randint(0, len(cb2) - 1)
            print(f"Мы дадим поддержку вашему защитнику {cb2[t22]}! +1 OVR")
            players[cb2[t22]] += 1
        elif t11 == 3:
            t22 = random.randint(0, len(cm3) - 1)
            print(f"Мы дадим поддержку вашему полузащитнику {cm3[t22]}! +1 OVR")
            players[cm3[t22]] += 1
        else:
            t22 = random.randint(0, len(st4) - 1)
            print(f"Мы дадим поддержку вашему нападающему {st4[t22]}! +1 OVR")
            players[st4[t22]] += 1
        print("Вот ваш текущий состав:")
        print(gk1)
        print(cb2)
        print(cm3)
        print(st4)
    else:
        print(f"Ты сыграл вничью со счетом {schet_you}:{schet_prt}")
        print("Поскольку ты сыграл вничью, назначается серия пенальти")
        mass_you = [0, 0, 0, 0, 0]
        mass_prt = [0, 0, 0, 0, 0]
        print("Вратарь сейвит в трех зонах, но ты можешь пробить только в одну")
        for i in range(5):
            if i % 2 == 0:
                print("Вратарь делает выбор...")
                time.sleep(5)
                rw = []
                yut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                random.shuffle(yut)
                rw.append(yut[0])
                yut.remove(yut[0])
                random.shuffle(yut)
                rw.append(yut[0])
                yut.remove(yut[0])
                random.shuffle(yut)
                rw.append(yut[0])
                yut.remove(yut[0])
                print("Теперь тебе предстоит сделать выбор")
                penalty_field()
                pot = int(input("Напиши номер зоны, в которую хочешь ударить: "))
                if pot in yut:
                    print("Ты забил!!!")
                    mass_you[i] = 1
                else:
                    print("К сожалению, ты не забил")
            else:
                print("Бьющий делает выбор...")
                time.sleep(5)
                rw = []
                yut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                random.shuffle(yut)
                rw.append(yut[0])
                yut.remove(yut[0])
                print("Теперь тебе предстоит сделать выбор")
                penalty_field()
                pot = list(
                    map(
                        int,
                        input(
                            "Напиши номера зон, в которых ты будешь сейвить: "
                        ).split(),
                    )
                )
                if yut in pot:
                    print("Ты засейвил!!!")
                else:
                    print("К сожалению, ты не засейвил")
                    mass_prt[i] = 1
            print("На текущий момент следующий счет:")
            for j in range(5):
                if mass_you[j] == 1:
                    print("✅", end="")
                else:
                    print("❌", end="")
            print()
            for j in range(5):
                if mass_prt[j] == 1:
                    print("✅", end="")
                else:
                    print("❌", end="")
            print()
        sm1 = sum(mass_you)
        sm2 = sum(mass_prt)
        if abs(sm2 - sm1) <= 1:
            print("Ваш счет еще может сравняться, серия пенальти продолжается")
            i = 1
            while abs(sm2 - sm1) <= 1:
                if i % 2 == 0:
                    print("Вратарь делает выбор...")
                    time.sleep(5)
                    rw = []
                    yut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    random.shuffle(yut)
                    rw.append(yut[0])
                    yut.remove(yut[0])
                    random.shuffle(yut)
                    rw.append(yut[0])
                    yut.remove(yut[0])
                    random.shuffle(yut)
                    rw.append(yut[0])
                    yut.remove(yut[0])
                    print("Теперь тебе предстоит сделать выбор")
                    penalty_field()
                    pot = int(input("Напиши номер зоны, в которую хочешь ударить: "))
                    if pot in yut:
                        print("Ты забил!!!")
                        sm1 += 1
                    else:
                        print("К сожалению, ты не забил")
                else:
                    print("Бьющий делает выбор...")
                    time.sleep(5)
                    rw = []
                    yut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    random.shuffle(yut)
                    rw.append(yut[0])
                    yut.remove(yut[0])
                    print("Теперь тебе предстоит сделать выбор")
                    penalty_field()
                    pot = list(
                        map(
                            int,
                            input(
                                "Напиши номера зон, в которых ты будешь сейвить: "
                            ).split(),
                        )
                    )
                    if yut in pot:
                        print("Ты засейвил!!!")
                    else:
                        print("К сожалению, ты не засейвил")
                        sm2 += 1
            if sm1 > sm2:
                print(f"Ты выиграл со счетом {sm1}:{sm2}")
            elif sm1 < sm2:
                print(f"Ты проиграл со счетом {sm1}:{sm2}")
                print("Внимание!!! Поскольку ваша команда проиграла матч, мы даем вам поддержку")
                input()
                t11 = random.randint(1, 4)
                t22 = 0
                if t11 == 1:
                    t22 = random.randint(0, len(gk1) - 1)
                    print(f"Мы дадим поддержку вашему вратарю {gk1[t22]}! +1 OVR")
                    players[gk1[t22]] += 1
                elif t11 == 2:
                    t22 = random.randint(0, len(cb2) - 1)
                    print(f"Мы дадим поддержку вашему защитнику {cb2[t22]}! +1 OVR")
                    players[cb2[t22]] += 1
                elif t11 == 3:
                    t22 = random.randint(0, len(cm3) - 1)
                    print(f"Мы дадим поддержку вашему полузащитнику {cm3[t22]}! +1 OVR")
                    players[cm3[t22]] += 1
                else:
                    t22 = random.randint(0, len(st4) - 1)
                    print(f"Мы дадим поддержку вашему нападающему {st4[t22]}! +1 OVR")
                    players[st4[t22]] += 1
                print("Вот ваш текущий состав:")
                print(gk1)
                print(cb2)
                print(cm3)
                print(st4)


def penalty_field():
    print(
        """                   _________________
                  |     |     |     |
                  |  1  |  2  |  3  |
                  |_____|_____|_____|
                  |     |     |     |
                  |  4  |  5  |  6  |
                  |_____|_____|_____|
                  |     |     |     |
                  |  7  |  8  |  9  |
                  |_____|_____|_____|"""
    )


def f(i, s):
    print(f"{i} - {s}")


print("Привет, выбери, за какой клуб будешь играть:")
print("На выбор у тебя будет 200 клубов:")
f(1, "Манчестер Сити")
f(2, "Реал Мадрид")
f(3, "Бавария")
f(4, "Ливерпуль")
f(5, "Рома")
f(6, "ПСЖ")
f(7, "Вильреал")
f(8, "Челси")
f(9, "Интер")
f(10, "Манчестер Юнайтед")
w = [
    "Манчестер Сити",
    "Реал Мадрид",
    "Бавария",
    "Ливерпуль",
    "Рома",
    "ПСЖ",
    "Вильреал",
    "Челси",
    "Интер",
    "Манчестер Юнайтед",
]
y = int(input("Введи номер того клуба, за который хочешь играть: "))
wqert = w[y - 1]
print(wqert)
w.remove(w[y - 1])
print(f"Ты выбрал играть за {wqert}")
print("Вот твой стартовый состав:")
gk1 = teams[wqert]["Goalkeeper"]
cb2 = teams[wqert]["Defenders"]
cm3 = teams[wqert]["Midfielders"]
st4 = teams[wqert]["Strikers"]
print(f"Вратарь - {gk1}")
print(f"Защитники - {cb2}")
print(f"Полузащитники - {cm3}")
print(f"Нападающие - {st4}")
while True:
    gk = teams[wqert]["Goalkeeper"]
    cb = teams[wqert]["Defenders"]
    cm = teams[wqert]["Midfielders"]
    st = teams[wqert]["Strikers"]
    week(gk, cb, cm, st, gk1, cb2, cm3, st4)
