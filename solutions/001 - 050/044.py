limit = 5000

pentagonal = [i * (3 * i - 1) // 2 for i in range(limit)]

check = set(pentagonal)

answer = 10 ** 10

for j in range(1, limit):
    for k in range(j + 1, limit):
        sum = pentagonal[j] + pentagonal[k]
        difference = pentagonal[k] - pentagonal[j]
        if sum in check and difference in check:
            answer = min(answer, difference)

print(answer)