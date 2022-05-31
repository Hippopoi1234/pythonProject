from itertools import islice, count
import time

def is_prime(n):
    return n > 1 and all(n % k for k in islice(count(2), int(n ** 0.5 - 1)))

def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n ** 2


generator = prime_generator()

l, r = map(int, input().split())
start_time = time.monotonic()
i = generator.__next__()
c = 0
while i < l:
    i = generator.__next__()
while i <= r:
    i = generator.__next__()
    c += 1
print('Время выполнения: ', time.monotonic() - start_time)
print(c)
