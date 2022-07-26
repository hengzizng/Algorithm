import sys
read = sys.stdin.readline


# 전구 상태 배열 복사
def get_copied(bulbs):
    copied = []
    for bulb in bulbs:
        copied.append(bulb)
    return copied


# 목표 상태와 같은지 여부 판단
def is_same(bulbs):
    for i in range(N):
        if bulbs[i] != target[i]:
            return False
    return True


# 전구의 상태를 바꾼다
def switch(bulbs, i):
    bulbs[i - 1] = bulbs[i - 1] ^ 1
    bulbs[i] = bulbs[i] ^ 1
    if i + 1 < N:
        bulbs[i + 1] = bulbs[i + 1] ^ 1


# 전구 수
N = int(read())
# 전구들의 현재 상태 (bulbs2는 맨 앞 전구의 상태를 바꾼다)
bulbs1 = list(map(int, list(read().strip())))
bulbs2 = get_copied(bulbs1)
bulbs2[0] = bulbs2[0] ^ 1
bulbs2[1] = bulbs2[1] ^ 1
# 만들고 싶은 전구들의 상태
target = list(map(int, list(read().strip())))
# 스위치를 누른 횟수
count, count1, count2 = -1, 0, 1

# 두 번째 스위치부터 마지막 스위치까지 확인
for i in range(1, N):
    # 왼쪽 스위치가 목표 상태와 다르다면 이번 스위치를 변경
    if bulbs1[i - 1] != target[i - 1]:
        switch(bulbs1, i)
        count1 += 1
    if bulbs2[i - 1] != target[i - 1]:
        switch(bulbs2, i)
        count2 += 1

if is_same(bulbs1):
    count = count1
if is_same(bulbs2):
    if count == -1:
        count = count2
    else:
        count = min(count1, count2)

print(count)
