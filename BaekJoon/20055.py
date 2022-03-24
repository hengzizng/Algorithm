from collections import deque
import sys
read = sys.stdin.readline


# 벨트가 한 칸 회전한다.
def rotate():
    A.appendleft(A.pop())
    robots.appendleft(robots.pop())
    # 회전 후 내리는 위치에 로봇이 있다면 로봇을 없애준다
    robots[N - 1] = False


# 로봇이 벨트 회전 방향으로 한 칸 이동한다.
def move():
    for index in range(N - 2, 0 - 1, -1):  # up <- down 순으로 각 칸별로 확인
        if robots[index] and not robots[index + 1] and A[index + 1] >= 1:  # 움직일 수 있으면
            robots[index] = False  # 현재 위치에서
            add_robot(index + 1)  # 다음 위치로 이동

            if index + 1 == N - 1:  # 로봇이 내리는 위치로 움직였으면
                robots[index + 1] = False


# index 위치에 로봇을 추가한다.
def add_robot(index):
    if A[index] >= 1:
        robots[index] = True
        A[index] -= 1  # 내구도 감소

        if A[index] == 0:
            zero_count[0] += 1


# N: 벨트의 길이 2, K: 종료 조건 (내구도가 K개 이상이면 종료)
N, K = map(int, read().split())
# A: 각 칸의 내구도
A = deque(map(int, read().split(" ")))
# 로봇이 위치해있는지 여부
robots = deque([False] * N)
# 내구도가 0인 칸의 개수
zero_count = [0]

step = 0
while zero_count[0] < K:
    rotate()
    move()
    add_robot(0)

    step += 1

print(step)
