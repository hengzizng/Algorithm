import sys

read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))

flag = True # True면 증가, False면 감소
maxLen = 1
sameLen = 0
nowLen = 1
for i in range(1, N):
    if nums[i - 1] == nums[i]:
        sameLen += 1
        nowLen += 1
    elif nums[i - 1] < nums[i]:
        if flag:
            nowLen += 1
        else:
            nowLen = sameLen + 2
        flag = True
        sameLen = 0
    else:
        if flag:
            nowLen = sameLen + 2
        else:
            nowLen += 1
        flag = False
        sameLen = 0
        
    maxLen = max(maxLen, nowLen)

print(maxLen)