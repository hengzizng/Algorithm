import sys
read = sys.stdin.readline


# A 배열 - H: 행 수, W: 열 수
# B 배열 - H + X: 행 수, W + Y: 열 수
H, W, X, Y = map(int, read().split())
B = [list(map(int, read().split())) for _ in range(H + X)]

A = [[B[r][c] for c in range(W)] for r in range(H)]

for r in range(H):
    for c in range(W):
        if r - X >= 0 and c - Y >= 0:
            A[r][c] -= A[r - X][c - Y]
    print(*A[r])
