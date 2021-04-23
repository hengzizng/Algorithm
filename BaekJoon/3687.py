answers = []

nums = ['0', '1', '2', '6', '8']
TC = int(input())
min_dp = [''] * 101
min_dp[2] = '1'
min_dp[3] = '7'
min_dp[4] = '4'
min_dp[5] = '2'
min_dp[6] = '6'
min_dp[8] = '10'
min_dp[10] = '22'
min_dp[11] = '20'
min_dp[17] = '200'
max_dp = [0] * 101
for _ in range(TC):
    n = int(input())

    for i in range(7, n + 1):
        if min_dp[i] == '':
            min_dp[i] = min_dp[i - 7] + '8'

    max_dp[n] = ('1' if n % 2 == 0 else '7')
    if n // 2 > 1:
        max_dp[n] += '1' * ((n // 2) - 1)

    answers.append([min_dp[n], max_dp[n]])

for answer in answers:
    print(answer[0], answer[1])