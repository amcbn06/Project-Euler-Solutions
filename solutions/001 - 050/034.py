limit = 10000000

factorial = [1] * 10

for i in range(2, 10):
    factorial[i] = factorial[i - 1] * i

total = 0

for i in range(3, limit):
    sum = 0
    for digit in str(i):
        sum += factorial[int(digit)]
    if sum == i:
        total += i

print(total)
