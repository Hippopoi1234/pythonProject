numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
           (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]


def sorted1():
    a = []
    for i in numbers:
        a.append(max(i) + min(i))
    a.sort()
    b = []
    for i in range(len(a)):
        for j in range(len(numbers)):
            if max(numbers[j])+min(numbers[j])==a[i]:
                b.append(numbers[j])
    print(b)

sorted1()
