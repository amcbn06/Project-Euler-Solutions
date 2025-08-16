answer = 1
n = 20

for i in range(n + 1, 2 * n + 1):
    answer *= i

for i in range(1, n + 1):
    answer //= i

print(answer)