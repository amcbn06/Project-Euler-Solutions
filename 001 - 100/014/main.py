dp = {}

dp[1] = 0

def solve(n):
    if n not in dp:
        if n % 2 == 0:
            dp[n] = solve(n // 2) + 1
        else:
            dp[n] = solve(3 * n + 1) + 1
    return dp[n]

answer = 1

for i in range(2, 1000000):
    if dp[answer] < solve(i):
        answer = i

print(answer)