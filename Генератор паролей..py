import random

a = int(input("Количество паролей для генерации: "))
b = int(input("Количество символов в пароле: "))
c = int(input("Включать ли цифры 0123456789 (1 - да, 0 - нет): "))
d = int(input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz (1 - да, 0 - нет): "))
e = int(input("Включать ли символы !#$%&*+-=?@^_ (1 - да, 0 - нет): "))
f = int(input("Исключать ли неоднозначные символы il1Lo0O (1 - да, 0 - нет): "))
j = int(input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (1 - да, 0 - нет): "))
chars = ''
g = ''
if c == 1:
    chars += "0123456789"
if d == 1:
    chars += "abcdefghijklmnopqrstuvwxyz"
if e == 1:
    chars += "!#$%&*+-=?@^_"
if f == 1:
    chars.replace("i", "")
    chars.replace("l", "")
    chars.replace("1", "")
    chars.replace("L", "")
    chars.replace("o", "")
    chars.replace("0", "")
    chars.replace("O", "")
if j == 1:
    chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for h in range(a):
    for i in range(b):
        g+=chars[random.randint(0, len(chars)-1)]
    print(g)
    g = ''