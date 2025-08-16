dp = [[]]

with open('001 - 100/018.txt', 'r') as f:
    dp = [[int(x) for x in line.split()] for line in f.read().split('\n')]

for i in range(1, len(dp)):
    for j in range(i + 1):
        prv = 0
        if j < i:
            prv = dp[i - 1][j]
        if j > 0:
            prv = max(prv, dp[i - 1][j - 1])
        dp[i][j] += prv

print(max(dp[-1]))