limit = 200

coins = [1, 2, 5, 10, 20, 50, 100, 200]

# dp[i][j] = the number of ways to make change for amount j using the first i types of coins
dp = [[0] * (limit + 1)] * len(coins)

dp[0] = [1] * (limit + 1)

for i in range(1, len(coins)):
    dp[i] = dp[i - 1]
    for j in range(coins[i], limit + 1):
        dp[i][j] += dp[i][j - coins[i]]

print(dp[len(coins) - 1][limit])