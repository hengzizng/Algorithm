import sys
read = sys.stdin.readline


# M: 벌집의 크기, N: 일 수
M, N = map(int, read().split())
# 왼쪽 아래 -> 왼쪽 위 -> 오른쪽 위 순서대로 가장 왼쪽 열, 가장 위쪽 행의 값
# zero + one = 2 * M - 1 인 경우를 위해 2 * M개로 둔다
values = [0] * (2 * M)
# 일별로 반복
for _ in range(N):
    # zero개는 0만큼, one개는 1만큼, two개는 2만큼 성장
    zero, one, two = map(int, read().split())

    # 누적합을 위해 시작 위치에만 1을 더해준다.
    values[zero] += 1
    values[zero + one] += 1

# 누적합으로 실제 더해질 값들을 구한다.
value = 0
for i in range(2 * M - 1):
    # 초기에 주어진 1도 같이 더해준다.
    values[i] += value + 1
    # 누적합에서는 초기값 1을 빼준다.
    value = values[i] - 1

temp = values[M:-1]
for r in range(M - 1, 0 - 1, -1):
    print(values[r], *temp)
