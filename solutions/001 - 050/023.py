upper = 28123

d = [0] * upper

for i in range(1, upper):
    for j in range(2 * i, upper, i):
        d[j] += i

abundant = []

for i in range(1, upper):
    if d[i] > i:
        abundant.append(i)

check = [False] * upper

for x in abundant:
    for y in abundant:
        if x + y < upper:
            check[x + y] = True
        else:
            break

sum = 0

for i in range(1, upper):
    if not check[i]:
        sum += i

print(sum)