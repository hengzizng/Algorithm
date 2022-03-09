# 구역: 격자의 각 칸, 선거구: 여러 개의 구역이 모인 집합
# 0 <= x < N - (d1 + d2) , d1 <= y < N - d2
# 1 <= d1, d2 < N

import sys
read = sys.stdin.readline


def calc(x, y, d1, d2):
    r, lc, rc = 0, y, y  # 행, 왼쪽 경계선 열, 오른쪽 경계선 열
    area_sum = [0] * 5  # 각 선거구의 인구 수의 합

    while r < N:
        if r < x:  # 경계선을 만나기 전 1,2 구역
            area_sum[0] += row_sum[r][lc]
            area_sum[1] += row_sum[r][N-1] - row_sum[r][rc]
        elif r >= x + d1 + d2:  # 경계선이 가장 아래 부분 3,4 구역
            area_sum[2] += row_sum[r][lc - 1]
            if r == x + d1 + d2:
                area_sum[3] += row_sum[r][N-1] - row_sum[r][rc]
            else:
                area_sum[3] += row_sum[r][N-1] - row_sum[r][rc - 1]
        else:  # 경계선이 존재하는 행
            if r < x + d1:  # 1 구역
                area_sum[0] += row_sum[r][lc - 1]
                lc -= 1
            elif r > x + d1:  # 3 구역
                area_sum[2] += row_sum[r][lc - 1]
                lc += 1
            else:  # 1구역 3구역 경계
                area_sum[2] += row_sum[r][lc - 1]
                lc += 1

            if r < x + d2:  # 2 구역
                area_sum[1] += row_sum[r][N-1] - row_sum[r][rc]
                rc += 1
            elif r > x + d2:  # 4 구역
                area_sum[3] += row_sum[r][N-1] - row_sum[r][rc]
                rc -= 1
            else:  # 2구역 4구역 경계
                area_sum[1] += row_sum[r][N-1] - row_sum[r][rc]
                rc -= 1

        area_sum[4] += row_sum[r][N-1]
        r += 1

    area_sum[4] -= sum(area_sum[:4])
    min_diff[0] = min(min_diff[0], max(area_sum) - min(area_sum))


N = int(read())  # 시의 크기
city = [list(map(int, read().split())) for _ in range(N)]  # 재현시의 각 구역별 인구
row_sum = []  # 각 위치별 맨 왼쪽부터의 합
for r in range(N):
    row_sum.append([])
    for c in range(N):
        row_sum[r].append(city[r][c])
        if c >= 1:
            row_sum[r][c] += row_sum[r][c - 1]
    row_sum[r].append(0)

min_diff = [float('inf')]  # 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차

for d1 in range(1, N):  # d1 선택
    for d2 in range(1, N - d1):  # d2 선택
        for x in range(0, N - (d1 + d2)):  # x 선택
            for y in range(d1, N - d2):  # y 선택
                calc(x, y, d1, d2)

print(*min_diff)
