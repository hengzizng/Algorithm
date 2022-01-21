import sys
read = sys.stdin.readline


# 어떤 물감을 섞을건지 선택 방법 1 > 2676ms
def combination(start, count, R, G, B):
    # 마지막으로 선택된 물감을 섞는다
    if count > 0:
        R, G, B = R + RGB[start - 1][0], G + RGB[start - 1][1], B + RGB[start - 1][2]
    
    # 선택된 물감이 0~1개일 때는 값 구할 필요 없다
    if count >= 2:
        min_diff[0] = min(min_diff[0], abs((R // count) - Rg) + abs((G // count) - Gg) + abs((B // count) - Bg))

    if count == mix_count or start == N:
        return

    for index in range(start, N):
        # 물감을 선택한다
        combination(index + 1, count + 1, R, G, B)


# # 어떤 물감을 섞을건지 선택 방법 2 > 2816ms
# def combination(index, count, R, G, B):
#     if count == mix_count or index == N:
#         return

#     # 이번 인덱스의 물감을 섞지 않는다
#     combination(index + 1, count, R, G, B)

#     # 이번 인덱스의 물감을 섞는다
#     count += 1
#     R, G, B = R + RGB[index][0], G + RGB[index][1], B + RGB[index][2]
#     if count >= 2: # 선택된 물감이 0~1개일 때는 값 구할 필요 없다
#         min_diff[0] = min(min_diff[0], abs((R // count) - Rg) + abs((G // count) - Gg) + abs((B // count) - Bg))

#     combination(index + 1, count, R, G, B)
    

N = int(read())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, read().split())))
Rg, Gg, Bg = map(int, read().split())

min_diff = [255 * 3]
mix_count = N if N < 7 else 7 # 섞는 물감의 개수는 2 ~ 7개
combination(0, 0, 0, 0, 0)

print(min_diff[0])