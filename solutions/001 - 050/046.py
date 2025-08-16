limit = 100000
sieve = [True] * limit
sieve[0] = sieve[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, limit, i):
            sieve[j] = False

primes =  [i for i, is_prime in enumerate(sieve) if is_prime]

check = [False] * limit

for prime in primes:
    for i in range(int(((limit - prime) // 2) ** 0.5)):
        check[prime + 2 * i * i] = True

for i in range(3, limit, 2):
    if not sieve[i] and not check[i]:
        print(i)
        break