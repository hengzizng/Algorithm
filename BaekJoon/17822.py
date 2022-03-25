from collections import deque
import sys
read = sys.stdin.readline


def get_total():
    # 원판 위의 모든 숫자의 개수와 합을 반환
    total_count, total_sum = 0, 0
    for i in range(1, N + 1):
        for j in range(M):
            if numbers[i][j] > 0:
                total_count += 1
                total_sum += numbers[i][j]

    return total_count, total_sum


def rotate(x, d, k):
    # 원판 번호 x 부터 N번까지 x 씩 증가시키면서 모두 회전
    for i in range(x, N + 1, x):
        temp = []
        for j in range(M):
            temp.append(numbers[i][j])

        for j in range(M):
            if d == 0:  # 시계 방향 회전
                numbers[i][j] = temp[(j + (M - k)) % M]
            else:  # 반시계 방향 회전
                numbers[i][j] = temp[(j + k) % M]


def check(i, j, visited):
    num = numbers[i][j]

    queue = deque([(i, j)])
    checked = set([(i, j)])
    visited[i][j] = True

    while queue:
        now = queue.popleft()

        # 인접한 수들을 확인 (인덱스가 0일 때 M-1 와도 인접함!)
        for di, dj in didj:
            ni, nj = di + now[0], (dj + now[1]) % M
            if 1 <= ni <= N and numbers[ni][nj] == num and not visited[ni][nj]:
                checked.add((ni, nj))
                visited[ni][nj] = True
                queue.append((ni, nj))

    # len(checked) > 1 이라면 인접한 같은 숫자가 있는 경우
    if len(checked) > 1:
        for i, j in checked:
            numbers[i][j] = 0
        return 1
    return 0


# N: 가장 큰 원의 반지름(원판의 개수), M: 한 원판에 적힌 정수 개수, T: 회전 횟수
N, M, T = map(int, read().split())
# 인접한 숫자 확인을 위한 방향 벡터
didj = [[-1, 0], [1, 0], [0, M-1], [0, 1]]

# numbers: 각 원판에 적힌 숫자들
# 1번째 -> M번째 : 12시 방향부터 시작해서 시계 방향
numbers = [[]]
for i in range(1, N + 1):
    numbers.append([])
    temp = read().split()
    for j in range(M):
        numbers[i].append(int(temp[j]))

# 원판의 회전
for _ in range(T):
    # x: x의 배수인 원판 번호(반지름), d: 방향(0: 시계, 1: 반시계), k: 회전시킬 칸 수
    x, d, k = map(int, read().split())
    rotate(x, d, k)

    is_exist_same = 0
    total_count, total_sum = get_total()
    if total_count == 0:  # 원판에 수가 하나도 없으면
        break
    else:  # 원판에 수가 남아있으면
        visited = [[False] * M for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(M):
                if numbers[i][j] == 0:
                    continue
                is_exist_same += check(i, j, visited)

    # is_exist_same == 0 이라면 인접한 같은 숫자가 없는 경우
    total_count, total_sum = get_total()
    if is_exist_same == 0 and total_count > 0:
        avg = total_sum / total_count
        for i in range(1, N + 1):  # 원판별 확인
            for j in range(M):  # 위치별 숫자 확인
                if numbers[i][j] == 0:
                    continue

                if numbers[i][j] < avg:
                    numbers[i][j] += 1
                elif numbers[i][j] > avg:
                    numbers[i][j] -= 1

total_count, total_sum = get_total()

print(total_sum)
