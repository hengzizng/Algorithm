from re import M
import sys
read = sys.stdin.readline

cups = list(range(4))

# M: 컵의 위치를 바꾼 횟수
M = int(read())
for _ in range(M):
    cup1, cup2 = map(int, read().split())
    cups[cup1], cups[cup2] = cups[cup2], cups[cup1]

for no in range(1, 3 + 1):
    if cups[no] == 1:
        print(no)
        break