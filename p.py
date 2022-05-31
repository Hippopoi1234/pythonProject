input()
c = list(map(int, input().split()))
# c = [3, 6, 2, 1]
# c = [7, 3, 1, 4, 2]
# c = [1, 4, 5, 2, 8, 16, 1]

def getel(l):
    if len(l) > 1:
        return max(l[0] + getel(l[2:]), l[0] + getel(l[3:]))
    elif len(l) == 1:
        return l[0]
    else:
        return 0

print(max(getel(c[:]), getel(c[1:])))
