import players, time, random

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
                  |_____|_____|_____|""")


def f(i, s):
    print(f"{i} - {s}")


print("Привет, выбери, за какой клуб будешь играть:")
print("На выбор у тебя будет 200 клубов:")
f(1, "Манчестер сити")
f(2, "Реал мадрид")
w = ["Манчестер Сити", "Реал Мадрид"]
y = int(input("Введи номер того клуба, за который хочешь играть: "))
if y == 1:
    w.remove("Манчестер Сити")
    print("Ты выбрал играть за Манчестер Сити")
    print("Вот твой стартовый состав:")
    gk = players.man_city["Goalkeeper"]
    cb = players.man_city["Defenders"]
    cm = players.man_city["Midfielders"]
    st = players.man_city["Strikers"]
    print(f"Вратарь - {gk}")
    print(f"Защитники - {cb}")
    print(f"Полузащитники - {cm}")
    print(f"Нападающие - {st}")
    while True:
        gk = players.man_city["Goalkeeper"]
        cb = players.man_city["Defenders"]
        cm = players.man_city["Midfielders"]
        st = players.man_city["Strikers"]
        time.sleep(0)
        print("Началась новая неделя, напиши да, если хочешь начать матч:")
        input()
        u = random.randint(0, len(w) - 1)
        print(f"Твой противник на эту неделю - {w[u]}")
        print("Подсчитаем средний OVR на всех позициях в твоей команде:")
        k_gk = 0
        for i in gk:
            k_gk += i[1]
        k_cb = 0
        for i in cb:
            k_cb += i[1]
        k_cm = 0
        for i in cm:
            k_cm += i[1]
        k_st = 0
        for i in st:
            k_st += i[1]
        t_1 = k_gk // len(gk)
        t_2 = k_cb // len(cb)
        t_3 = k_cm // len(cm)
        t_4 = k_st // len(st)
        print(f"Вратарь - {t_1}")
        print(f"Защита - {t_2}")
        print(f"Полузащита - {t_3}")
        print(f"Атака - {t_4}")
        print("Теперь подсчитаем тоже самое, но у твоего противника:")
        if w[u] == "Манчестер Сити":
            gk = players.man_city["Goalkeeper"]
            cb = players.man_city["Defenders"]
            cm = players.man_city["Midfielders"]
            st = players.man_city["Strikers"]
        elif w[u] == "Реал Мадрид":
            gk = players.real_madrid["Goalkeeper"]
            cb = players.real_madrid["Defenders"]
            cm = players.real_madrid["Midfielders"]
            st = players.real_madrid["Strikers"]
        k_gk = 0
        for i in gk:
            k_gk += i[1]
        k_cb = 0
        for i in cb:
            k_cb += i[1]
        k_cm = 0
        for i in cm:
            k_cm += i[1]
        k_st = 0
        for i in st:
            k_st += i[1]
        t1 = k_gk // len(gk)
        t2 = k_cb // len(cb)
        t3 = k_cm // len(cm)
        t4 = k_st // len(st)
        print(f"Вратарь - {t1}")
        print(f"Защита - {t2}")
        print(f"Полузащита - {t3}")
        print(f"Атака - {t4}")
        schet_you = 0
        schet_prt = 0
        if t_1 > t1:
            schet_you += 1
            print("Твой вратарь лучше, чем вратарь твоих противников")
        elif t1 > t_1:
            schet_prt += 1
            print("Твой вратарь хуже вратаря противников")
        else:
            print("Твой вратарь такой же сильный, как и вратарь противников")
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
        if t_4 > t4:
            schet_you += (t_4 - t4)
            print("Твоя атака лучше, чем атака твоих противников")
        elif t4 > t_4:
            schet_prt += (t4 - t_4)
            print("Твоя атака хуже атаки противников")
        else:
            print("Твоя атака такая же сильная, как и атака противников")
        if schet_you > schet_prt:
            print(f"Ты победил со счетом {schet_you}:{schet_prt}")
        elif schet_you < schet_prt:
            print(f"Ты проиграл со счетом {schet_you}:{schet_prt}")
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
                    pot = list(map(int, input("Напиши номера зон, в которых ты будешь сейвить: ").split()))
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
                        pot = list(map(int, input("Напиши номера зон, в которых ты будешь сейвить: ").split()))
                        if yut in pot:
                            print("Ты засейвил!!!")
                        else:
                            print("К сожалению, ты не засейвил")
                            sm2 += 1
                if sm1 > sm2:
                    print(f"Ты выиграл со счетом {sm1}:{sm2}")
                elif sm1 < sm2:
                    print(f"Ты проиграл со счетом {sm1}:{sm2}")
if y == 2:
    w.remove("Реал Мадрид")
    print("Ты выбрал играть за Реал Мадрид")
    print("Вот твой стартовый состав:")
    gk = players.real_madrid["Goalkeeper"]
    cb = players.real_madrid["Defenders"]
    cm = players.real_madrid["Midfielders"]
    st = players.real_madrid["Strikers"]
    print(f"Вратарь - {gk}")
    print(f"Защитники - {cb}")
    print(f"Полузащитники - {cm}")
    print(f"Нападающие - {st}")
    while True:
        gk = players.real_madrid["Goalkeeper"]
        cb = players.real_madrid["Defenders"]
        cm = players.real_madrid["Midfielders"]
        st = players.real_madrid["Strikers"]
        time.sleep(0)
        print("Началась новая неделя, напиши да, если хочешь начать матч:")
        input()
        u = random.randint(0, len(w) - 1)
        print(f"Твой противник на эту неделю - {w[u]}")
        print("Подсчитаем средний OVR на всех позициях в твоей команде:")
        k_gk = 0
        for i in gk:
            k_gk += i[1]
        k_cb = 0
        for i in cb:
            k_cb += i[1]
        k_cm = 0
        for i in cm:
            k_cm += i[1]
        k_st = 0
        for i in st:
            k_st += i[1]
        t_1 = k_gk // len(gk)
        t_2 = k_cb // len(cb)
        t_3 = k_cm // len(cm)
        t_4 = k_st // len(st)
        print(f"Вратарь - {t_1}")
        print(f"Защита - {t_2}")
        print(f"Полузащита - {t_3}")
        print(f"Атака - {t_4}")
        print("Теперь подсчитаем тоже самое, но у твоего противника:")
        if w[u] == "Манчестер Сити":
            gk = players.man_city["Goalkeeper"]
            cb = players.man_city["Defenders"]
            cm = players.man_city["Midfielders"]
            st = players.man_city["Strikers"]
        elif w[u] == "Реал Мадрид":
            gk = players.real_madrid["Goalkeeper"]
            cb = players.real_madrid["Defenders"]
            cm = players.real_madrid["Midfielders"]
            st = players.real_madrid["Strikers"]
        k_gk = 0
        for i in gk:
            k_gk += i[1]
        k_cb = 0
        for i in cb:
            k_cb += i[1]
        k_cm = 0
        for i in cm:
            k_cm += i[1]
        k_st = 0
        for i in st:
            k_st += i[1]
        t1 = k_gk // len(gk)
        t2 = k_cb // len(cb)
        t3 = k_cm // len(cm)
        t4 = k_st // len(st)
        print(f"Вратарь - {t1}")
        print(f"Защита - {t2}")
        print(f"Полузащита - {t3}")
        print(f"Атака - {t4}")
        schet_you = 0
        schet_prt = 0
        if t_1 > t1:
            schet_you += 1
            print("Твой вратарь лучше, чем вратарь твоих противников")
        elif t1 > t_1:
            schet_prt += 1
            print("Твой вратарь хуже вратаря противников")
        else:
            print("Твой вратарь такой же сильный, как и вратарь противников")
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
        if t_4 > t4:
            schet_you += (t_4 - t4)
            print("Твоя атака лучше, чем атака твоих противников")
        elif t4 > t_4:
            schet_prt += (t4 - t_4)
            print("Твоя атака хуже атаки противников")
        else:
            print("Твоя атака такая же сильная, как и атака противников")
        if schet_you > schet_prt:
            print(f"Ты победил со счетом {schet_you}:{schet_prt}")
        elif schet_you < schet_prt:
            print(f"Ты проиграл со счетом {schet_you}:{schet_prt}")
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
                    pot = list(map(int, input("Напиши номера зон, в которых ты будешь сейвить: ").split()))
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
                    pot = list(map(int, input("Напиши номера зон, в которых ты будешь сейвить: ").split()))
                    if yut in pot:
                        print("Ты засейвил!!!")
                    else:
                        print("К сожалению, ты не засейвил")
                        sm2 += 1
            if sm1 > sm2:
                print(f"Ты выиграл со счетом {sm1}:{sm2}")
            elif sm1 < sm2:
                print(f"Ты проиграл со счетом {sm1}:{sm2}")
