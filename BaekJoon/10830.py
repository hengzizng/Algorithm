import sys
read = sys.stdin.readline


# matrix1과 matrix2를 곱한 결과를 return
def multiply(matrix1, matrix2):
    result = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for a in range(N):
                result[r][c] += matrix1[r][a] * matrix2[a][c]
            result[r][c] %= 1000
    return result


# A의 time제곱을 구해 return
def get_result(time):
    # A의 time제곱을 이미 구했다면 바로 return
    if time in martix:
        return martix[time]

    martix[time] = multiply(get_result(time // 2), get_result(time // 2))
    # time이 홀수일 경우 A를 한번 더 곱해준다
    # ex) 5일 경우 윗 줄에서 구한 결과는 multiply(2, 2) 이므로, 이 결과에 A를 한번 더 곱한다.
    if time % 2 == 1:
        martix[time] = multiply(martix[time], A)

    return martix[time]


# N: 행렬의 크기, B: 제곱 횟수
N, B = map(int, read().split())
# A: B제곱할 행렬
# 초기값이 1000일 경우가 있으므로 입력받을 때 1000으로 나눈다
A = [list(map(lambda x: int(x) % 1000, read().split())) for _ in range(N)]
# martix[X]: A를 X제곱한 결과
martix = {}
martix[1] = A

for row in get_result(B):
    print(*row)
