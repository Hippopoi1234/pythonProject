a = int(input())  # сколько блюд
b = list(map(int, input().split()))  # стоимости блюд в меню
c = int(input())  # стоимость бизнес-ланча
d = list(map(int, input().split()))  # номера блюд в бизнес-ланче
e = int(input())  # количество заказанных блюд
k = list(map(int, input().split()))  # номера заказанных блюд

s = {}  # стоимости блюд
for i in range(len(b)):
    s[i + 1] = b[i]
print(s)
f = set(k)  # множество заказанных блюд
g = set(d)  # множество блюд в бизнес-ланче
ff = list(f.intersection(g))
res = 0
while ff != []:
    ssum = 0
    for key, val in s.items():
        if key in ff:
            ssum += val
            k.remove(key)
    f = set(k)
    ff = list(f.intersection(g))
    res += min(ssum, c)

for i in k:
    res += s[i]

print(res)

# summary = 0
# while ff != set():
#     for i in ff:
#         k.remove(i)
#     f.difference_update(ff)
#     ff = f.intersection(g)
#     summary += c
# for i in k:
#     if i in d:
#         if c > b[i - 1]:
#             summary += b[i - 1]
#         else:
#             summary += c
#     else:
#         summary += b[i - 1]
# print(summary)
