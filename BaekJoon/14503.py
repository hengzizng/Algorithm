import sys
read = sys.stdin.readline


def clean(r, c, d, count, area):
    fail_count = 0

    # 1. 현재 위치를 청소한다
    area[r][c] = 2
    count += 1

    while True:
        nd = (d + 3) % 4
        nr, nc = r + drdc[nd][0], c + drdc[nd][1]

        if area[nr][nc] == 0: 
            # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
            # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행
            return clean(nr, nc, nd, count, area)
        else:
            # b. 왼쪽 방향에 청소할 공간이 없다면
            # 그 뱡향으로 회전하고 2번으로 돌아간다
            d = nd
            fail_count += 1

        # c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는
        # 바라보는 방향을 유지한 채로 한 칸 후진하고 2번으로 돌아간다
        if fail_count == 4:
            nr, nc = r - drdc[d][0], c - drdc[d][1]
            # 주의> 뒤쪽 방향이 벽일 때만 후진 불가능 (청소된 곳이어도 후진 가능)
            # d. 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다
            if area[nr][nc] == 1:
                return count
            fail_count = 0
            r, c = nr, nc

# 1. 현재 위치 청소
# 2. 왼쪽으로 회전
# 2-1. 아직 청소하지 않은 공간이면 한칸 전진 -> 1 진행
# 2-2. 청소할 공간이 없으면 -> 2 진행
# 2-3. 이번 방향이 네번째 불가능이면 한칸 후진 -> 2 진행
# 2-4. 후진도 못하면 작동 중지

# 0: 북, 1: 동, 2: 남, 3: 서
drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# N: 행 수, M: 열 수
N, M = map(int, read().split())
# 로봇청소기 정보 - r: 행 위치, c: 열 위치, d: 방향
r, c, d = map(int, read().split())

area = []
for _ in range(N):
    area.append(list(map(int, read().split())))

print(clean(r, c, d, 0, area))