T = int(input())
min_fix_counts = []
for _ in range(T):
    nums = input().strip()
    flag = '0'
    min_fix_count = 0
    for num in nums:
        if num != flag:
            min_fix_count += 1
            flag = num
    min_fix_counts.append(min_fix_count)

for t in range(1, T + 1):
    print("#" + str(t) + " " + str(min_fix_counts[t - 1]))