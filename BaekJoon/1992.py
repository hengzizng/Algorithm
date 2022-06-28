import sys
read = sys.stdin.readline


def compress(start_r, start_c, size):
    start_val = video[start_r][start_c]  # 확인할 영상의 가장 왼쪽 위 값
    all_same = True  # 모두 0이거나 1인지 여부

    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            if video[r][c] != start_val:
                all_same = False
                break

    # 확인할 영상의 크기가 1이거나 모두 같은 값이면
    if size == 1 or all_same:
        result = start_val
    else:
        size = size // 2

        result = "("
        result += compress(start_r, start_c, size)
        result += compress(start_r, start_c + size, size)
        result += compress(start_r + size, start_c, size)
        result += compress(start_r + size, start_c + size, size)
        result += ")"

    return result


N = int(read())
video = [list(read().strip()) for _ in range(N)]

print(compress(0, 0, N))
