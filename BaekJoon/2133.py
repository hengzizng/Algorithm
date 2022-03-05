N = int(input())
dp = [1, 0, 3, 0]

for width in range(4, N + 1):
    val = dp[width - 2] * 3
    for i in range(4, width + 1, 2):
        val += dp[width - i] * 2
    dp.append(val)

print(dp[N])
