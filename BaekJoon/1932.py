import sys


read = sys.stdin.readline

# n: 삼각형의 크기
n = int(read())
dp = [[0] * n for _ in range(n)]
dp[0][0] = int(read())

for floor in range(1, n):
    nums = list(map(int, read().split()))
    for idx, val in enumerate(nums):
        dp[floor][idx] = val + max(dp[floor - 1][idx - 1], dp[floor - 1][idx])

print(max(dp[-1]))