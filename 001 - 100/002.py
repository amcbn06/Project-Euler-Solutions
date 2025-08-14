sum = 0
limit = 4000000

a = 1
b = 2
while b < limit:
    if b % 2 == 0:
        sum += b
    a, b = b, a + b

print(sum)
