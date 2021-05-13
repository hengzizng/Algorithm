import sys


read = sys.stdin.readline

n = int(read())
# dp: [[i까지 최대합, i번째 수 첫번째로 포함]]
dp = [[0] * 2 for _ in range(n)]
for i in range(n):
    wine = int(read())
    if i < 2:
        dp[i][0] = dp[i - 1][0] + wine
        dp[i][1] = wine
    else:
        dp[i][0] = max(dp[i - 1][1] + wine, dp[i - 1][0])
        dp[i][1] = max(dp[i - 2]) + wine

print(max(dp[-1]))