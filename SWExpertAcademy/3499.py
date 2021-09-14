# 60,980 kb
# 메모리
# 166 ms
# 실행시간
# 502
# 코드길이

import sys
sys.stdin = open("TestCase/SWExpertAcademy/3499input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(input().split(" "))
    shuffled = ["" for _ in range(N)]

    left = 0
    right = N // 2 + (0 if N % 2 == 0 else 1)
    index, flag = 0, -1
    while index < N:
        if flag == -1:
            shuffled[index] = cards[left]
            left += 1
        else:
            shuffled[index] = cards[right]
            right += 1
        flag *= -1
        index += 1

    print("#" + str(tc) + " " + " ".join(shuffled))