import sys
sys.stdin = open("TestCase/SWExpertAcademy/2805input.txt")

# 61,236 kb
# 메모리
# 237 ms
# 실행시간
# 444
# 코드길이

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = []
    for r in range(N):
        farm.append(list(map(int, list(input()))))

    half = N // 2
    profit = 0
    for r in range(half):
        for c in range(half - r, half + r + 1):
            profit += farm[r][c]
    for r in range(half, N):
        for c in range(r - half, N - (r - half)):
            profit += farm[r][c]
    
    print('#' + str(tc), profit)
