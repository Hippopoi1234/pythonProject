a = int(input())
b = int(input())
dict1 = {(0, 0): "love all", (0, 1): "love 15", (0, 2): "love 30", (0, 3): "love 40", (1, 0): "15 love",
         (1, 1): "15 all", (1, 2): "15 30", (1, 3): "15 40", (2, 0): "30 love", (2, 1): "30 15", (2, 2): "30 all",
         (2, 3): "30 40", (3, 0): "40 love", (3, 1): "40 15", (3, 2): "40, 30"}
k = 0
for i in dict1.items():
    if i[0][0] == a and i[0][1] == b:
        print(i[1])
        k = 1
        break
if k==0:
    if a == b:
        print("deuce")
    elif a>b:
        print("advantage in")
    else:
        print("advantage out")