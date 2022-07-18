import sys
read = sys.stdin.readline


def check():
    # 선생님별로 반복
    for r, c in teachers:
        # 방향별로 반복
        for d in range(4):
            nr, nc = r, c
            while 0 <= nr < N and 0 <= nc < N:
                # 선생님이 한명이라도 학생 마주치면 실패
                if hallway[nr][nc] == 1:
                    return False
                # 벽 만나면 다른 방향 확인
                if hallway[nr][nc] == -1:
                    break
                nr += drdc[d][0]
                nc += drdc[d][1]

    return True


# 장애물을 설치한다.
def set_obstacle(count, start):
    # 이미 가능한 조건을 찾았으면 더이상 장애물을 설치하며 확인할 필요 X
    if can_avoid[0]:
        return

    # 3개의 장애물을 설치했으면 모든 학생들이 감시를 피할 수 있는지 확인한다.
    if count == 3:
        if check():
            can_avoid[0] = True
        return

    for index in range(start, N * N):
        # 빈 칸에만 장애물 설치
        if hallway[index // N][index % N] == 0:
            hallway[index // N][index % N] = -1
            set_obstacle(count + 1, index + 1)
            hallway[index // N][index % N] = 0


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
N = int(read())  # 복도 크기
hallway = []  # 복도 상태 (0: 빈 칸, 1: 학생, 2: 선생님, -1: 장애물)
teachers = []  # 선생님들의 위치
for r in range(N):
    hallway.append(list(read().strip().split(" ")))
    for c in range(N):
        if hallway[r][c] == 'X':
            hallway[r][c] = 0
        elif hallway[r][c] == 'S':
            hallway[r][c] = 1
        else:
            hallway[r][c] = 2
            teachers.append((r, c))

can_avoid = [False]  # 모든 학생들이 감시를 피할 수 있는지 여부
set_obstacle(0, 0)
print("YES" if can_avoid[0] else "NO")
