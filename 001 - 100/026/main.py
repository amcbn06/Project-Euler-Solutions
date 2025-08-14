limit = 1000

def phi(x):
    result = x
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1
    if x > 1:
        result -= result // x
    return result

def find_recurring_cycle(x):
    while x % 2 == 0:
        x //= 2
    while x % 5 == 0:
        x //= 5
    
    # n = smallest integer such that 10^n ≡ 1 (mod x)
    # n divides phi(x)
    
    y = phi(x)
    n = y

    for i in range(1, int(y ** 0.5) + 1):
        if y % i == 0:
            if pow(10, i, x) == 1:
                n = min(n, i)
            if pow(10, y // i, x) == 1:
                n = min(n, y // i)

    return n

d, length = 1, 0

for i in range(1, limit):
    cur_length = find_recurring_cycle(i)
    if cur_length > length:
        length = cur_length
        d = i

print(d, length)