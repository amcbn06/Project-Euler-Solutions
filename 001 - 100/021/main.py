limit = 10000

d = [0] * limit

for i in range(1, limit):
    for j in range(2 * i, limit, i):
        d[j] += i

sum = 0

for i in range(1, limit):
    if d[i] < limit and d[i] != i and d[d[i]] == i:
        sum += i

print(sum)