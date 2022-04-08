input()
a = input()
b = {}
s = ""
for i in a:
    b[i] = a.count(i)
# if max(b.values()) > (len(a) // 2) + 1:
#     print("NO")
#     exit()
val = list(b.values())
key = list(b.keys())
# print("YES")
indexing = 0
while sum(val) != 0:
    indexing = 0
    if len(s) != 0 and s[-1] != key[val.index((max(val)))]:
        s += key[val.index((max(val)))]
        indexing = val.index((max(val)))
    else:
        if len(s) == 0:
            s += key[val.index((max(val)))]
            indexing = val.index((max(val)))
        else:
            for g in range(len(key)):
                if key[g] != s[-1]:
                    s += key[g]
                    indexing = g
                    break
    val[indexing] -= 1
    if val[indexing] == 0:
        val.remove(val[indexing])
        key.remove(key[indexing])
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        print("NO")
        exit()
if len(s) != len(a):
    print("NO")
else:
    print("YES")
    print(s)
