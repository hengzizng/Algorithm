import sys
read = sys.stdin.readline


T = int(read())
for _ in range(T):
    n = int(read())
    sticker = [list(map(int, read().split())) for _ in range(2)]

    # 위 선택, 아래 선택, 아무것도 선택하지 않음
    before = [sticker[0][0], sticker[1][0], 0]
    for i in range(1, n):
        now = [sticker[0][i], sticker[1][i], 0]
        now[0] += max(before[1], before[2])
        now[1] += max(before[0], before[2])
        now[2] += max(before)
        before = now

    print(max(before))
