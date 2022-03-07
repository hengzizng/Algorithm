from collections import defaultdict
import sys
read = sys.stdin.readline

# R연산: 행 수 >= 열 수 일때, 행별로 정렬
# C연산: 행 수 < 열 수 일때, 열별로 정렬

# 정렬
# - 등장횟수 오름차순, 숫자 오름차순
# - 0은 무시
# - 정렬한 데이터가 100개 초과이면 앞의 100개를 제외하고 나머지는 버린다
# - 배열의 크기가 달라질 수 있으므로 나머지 행/열 의 뒤에 0으로 채워 크기를 맞춰준다


def R(A):  # R연산
    col_len = 0  # 새로 바뀐 열 크기

    for row in range(size[0]):
        # 각 행별로 숫자들의 등장횟수를 구한다.
        counts = defaultdict(int)
        for col in range(size[1]):
            val = A[row][col]
            if val > 0:  # 수를 정렬할 때 0은 무시
                counts[val] += 1

        # 등장횟수 오름차순, 숫자 오름차순으로 정렬
        sorted_data = []
        for num, count in counts.items():
            sorted_data.append((count, num))
        sorted_data.sort()

        # 정렬한 데이터를 A에 넣는다
        index = 0
        for count, num in sorted_data:
            A[row][index] = num
            A[row][index + 1] = count
            index += 2
            if index == 100:
                break

        # 나머지 행들을 0으로 채워준다
        for col in range(index, 100):
            A[row][col] = 0

        col_len = max(col_len, index)

    size[1] = col_len


def C(A):  # R연산
    row_len = 0  # 새로 바뀐 열 크기

    for col in range(size[1]):
        # 각 열별로 숫자들의 등장횟수를 구한다.
        counts = defaultdict(int)
        for row in range(size[0]):
            val = A[row][col]
            if val > 0:  # 수를 정렬할 때 0은 무시
                counts[val] += 1

        # 등장횟수 오름차순, 숫자 오름차순으로 정렬
        sorted_data = []
        for num, count in counts.items():
            sorted_data.append((count, num))
        sorted_data.sort()

        # 정렬한 데이터를 A에 넣는다
        index = 0
        for count, num in sorted_data:
            A[index][col] = num
            A[index + 1][col] = count
            index += 2
            if index == 100:
                break

        # 나머지 행들을 0으로 채워준다
        for row in range(index, 100):
            A[row][col] = 0

        row_len = max(row_len, index)

    size[0] = row_len


r, c, k = map(int, read().split())  # A[r][c]가 k가 되어야 한다
r, c = r - 1, c - 1  # 인덱스를 맞춰준다
A = [[0] * 100 for _ in range(100)]
size = [3, 0]  # 행 수, 열 수

for row in range(size[0]):
    temp = read().strip().split()
    size[1] = len(temp)
    for col in range(size[1]):
        A[row][col] = int(temp[col])


time = 0  # A[r][c]가 k가 되기 위한 최소 시간
while A[r][c] != k and time <= 100:
    if size[0] >= size[1]:  # R연산
        R(A)
    else:  # C연산
        C(A)

    time += 1

print(-1 if time == 101 else time)
