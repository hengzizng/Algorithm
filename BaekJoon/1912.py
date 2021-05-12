n = int(input())
sequence = list(map(int, input().split()))

# Solution 1 > 메모리 38756KB 시간 232ms
'''
# sums: [해당 순서까지의 최대값, 해당 순서를 무조건 포함한 최대값]
sums = [[0] * 2 for _ in range(n)]
sums[0] = [sequence[0], sequence[0]]
for i, num in enumerate(sequence):
    if i == 0:
        continue
    sums[i][0] = max(sums[i - 1][0], sums[i - 1][1], sums[i - 1][1] + num)
    sums[i][1] = max(num, sums[i - 1][1] + num)

print(max(sums[-1]))
'''

# Solution 2 > 메모리 36992KB 시간 132ms
# 음수로만 이루어진 수열
if max(sequence) < 0:
    print(max(sequence))
# 양수로만 이루어진 수열
elif min(sequence) >= 0:
    print(sum(sequence))
else:
    sums = [0] * n
    for i, num in enumerate(sequence):
        sums[i] = max(num, sums[i - 1] + num)
    print(max(sums))