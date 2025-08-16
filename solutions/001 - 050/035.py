limit = 1000000

sieve = [True] * limit
sieve[0] = sieve[1] = False

for i in range(2, int(limit**0.5) + 1):
    if sieve[i]:
        for j in range(i * i, limit, i):
            sieve[j] = False

count = 0

for i in range(2, limit):
    rotations = [int(str(i)[j:] + str(i)[:j]) for j in range(len(str(i)))]
    if all(sieve[x] for x in rotations):
        count += 1

print(count)