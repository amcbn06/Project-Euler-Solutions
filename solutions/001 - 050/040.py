limit = 200000

d = ""

for i in range(1, limit):
    d += str(i)

print(len(d))

product = 1

for i in range(7):
    product *= int(d[int(10 ** i) - 1])

print(product)