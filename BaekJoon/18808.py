import sys
read = sys.stdin.readline


# 스티커를 노트북에 붙인다.
# start: 스티커를 붙일 왼쪽 위 좌표
def attach(start, sticker):
    for r, c in sticker:
        notebook[start[0] + r][start[1] + c] = 1


# 스티커를 노트북에 붙일 수 있는 왼쪽 위 좌표를 반환한다.
# 스티커를 붙일 수 없는 경우, (-1, -1) 반환
def check(sticker):
    for r in range(N):
        for c in range(M):
            can_attach = True
            for nr, nc in sticker:
                nr, nc = r + nr, c + nc
                if nr < 0 or nr >= N or nc < 0 or nc >= M or notebook[nr][nc] == 1:
                    can_attach = False
                    break
            if can_attach:
                return (r, c)
    return (-1, -1)


# 스티커를 90도 회전시킨 결과를 반환한다
def rotate(sticker):
    # 90도 회전
    # r' = c
    # c' = (세로길이) - 1 - r
    rotated = []
    for r, c in sticker:
        rotated.append((c, R - 1 - r))
    return rotated


# N: 노트북 세로 길이, M: 노트북 가로 길이, K: 스티커 개수
N, M, K = map(int, read().split())
# 노트북 현재 상태
notebook = [[0] * M for _ in range(N)]
# 스티커를 붙인 칸의 수
attached_count = 0
for _ in range(K):
    # 스티커 정보
    sticker = []
    # R: 스티커 세로 길이, C: 스티커 가로 길이
    R, C = map(int, read().split())
    for r in range(R):
        temp = list(read().split())
        for c in range(C):
            if temp[c] == '1':
                sticker.append((r, c))

    # 스티커를 붙인다.
    for _ in range(4): # 4번까지 회전
        start = check(sticker)
        if start == (-1, -1):
            sticker = rotate(sticker)
            R, C = C, R
        else:
            attach(start, sticker)
            attached_count += len(sticker)
            break

print(attached_count)
