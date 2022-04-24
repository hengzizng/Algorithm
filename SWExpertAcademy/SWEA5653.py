from collections import defaultdict
import sys
sys.stdin = open("TestCase/SWExpertAcademy/5653input.txt")


# 활성화 시작 시각 = 번식된 시각 + 생명력
# 부모 세포가 번식하는 시각(자식 세포가 번식된 시각) = 부모 세포의 (번식된 시각 + 생명력 + 1)
# 죽는 시각 = 번식된 시각 + (생명력 * 2)
def spread_and_die(now_time, alive, dead):
    alive_locations = list(alive.keys())

    for r, c in alive_locations:
        made_time, life_value = alive[(r, c)]

        # 부모 세포가 번식하는 시각(자식 세포가 번식된 시각) = 부모 세포의 (번식된 시각 + 생명력 + 1)
        if now_time == made_time + life_value + 1:
            for dr, dc in drdc:
                nr, nc = r + dr, c + dc

                # 번식하려는 위치에 죽은 세포가 있거나, 이전에 번식한 세포가 있거나, 동시에 번식한 생명력이 더 높은 세포가 있다면 번식 불가
                if (((nr, nc) in dead) or
                        (((nr, nc)) in alive and now_time > alive[(nr, nc)][0]) or
                        ((nr, nc) in alive and now_time == alive[(nr, nc)][0] and life_value <= alive[(nr, nc)][1])):
                    continue

                alive[(nr, nc)] = (now_time, life_value)

        # 죽는 시각 = 번식된 시각 + (생명력 * 2)
        if now_time == made_time + (life_value * 2):
            del alive[(r, c)]
            dead.add((r, c))


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())  # 테스트케이스 수
for t in range(1, T + 1):
    # alive: 죽지 않은 세포들 {(행, 열) : (번식된 시각, 생명력), ...}
    alive = {}
    # dead: 죽은 세포들 {(행, 열), ...}
    dead = set()

    N, M, K = map(int, input().split())
    for r in range(N):
        temp = list(map(int, input().split()))
        for c in range(M):
            if temp[c] > 0:
                alive[(r, c)] = (0, temp[c])

    for k in range(1, K + 1):
        spread_and_die(k, alive, dead)

    print("#%d" % t, len(alive))
