def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print("%3d" % val, end="")
        print()


# 전체 행렬 회전
def rotateB():
    for r in range(N):
        for c in range(N):
            matrixB[c][N - 1 - r] = matrixA[r][c]


# 부분 행렬 회전 (재귀)
def rotate(start_r, start_c, size):
    for r in range(size):
        for c in range(size):
            matrixB[start_r + c][start_c + size - 1 - r] = matrixA[start_r + r][start_c + c]


# 행렬을 부분행렬로 나눈다
# divide(부분행렬 한 변 길이, 현재 나눈 행렬의 한 변 길이, 현재 부분행렬의 시작 행, 현재 부분행렬의 시작 열)
def divide(target_size, size, start_r, start_c):  # 행렬을 부분행렬로 나눈다
    if size == target_size:
        print("부분 행렬 회전 시작 값:", start_r, start_c, size)
        rotate(start_r, start_c, size)
        return

    size //= 2
    divide(target_size, size, start_r, start_c)
    divide(target_size, size, start_r + size, start_c)
    divide(target_size, size, start_r, start_c + size)
    divide(target_size, size, start_r + size, start_c + size)


# 부분 행렬 회전 (for loop)
# def rotate(size):
#     # matrixA 의 행과 열 인덱스
#     start_r, start_c, end_r, end_c = 0, 0, size, size

#     while start_r < N:
#         c_index = end_c - 1  # matrixB의 열 인덱스
#         for r in range(start_r, end_r):
#             r_index = start_r  # matrixB의 행 인덱스
#             for c in range(start_c, end_c):
#                 matrixB[r_index][c_index] = matrixA[r][c]
#                 r_index += 1
#             c_index -= 1

#         if start_c + size == N:
#             start_c, end_c = 0, size
#             start_r, end_r = start_r + size, end_r + size
#         else:
#             start_c, end_c = start_c + size, end_c + size


N = 8
matrixA, matrixB = [], []
for r in range(N):
    matrixA.append([])
    matrixB.append([])
    for c in range(N):
        matrixA[r].append(r * N + c + 1)
        matrixB[r].append(r * N + c + 1)

print_matrix(matrixB)
print("----------->")
divide(2, N, 0, 0)
print_matrix(matrixB)
