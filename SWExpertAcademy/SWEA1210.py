import sys
sys.stdin = open("TestCase/SWExpertAcademy/1210input.txt")

dxdy = [[0, -1], [0, 1], [-1, 0]]
LEN = 100
for _ in range(10):
    tc = input()

    ladders = []
    now = [-1, -1]
    for r in range(LEN):
        ladders.append(list(input().strip().split()))
        for c in range(LEN):
            if ladders[r][c] == '2':
                now[0] = r
                now[1] = c
    
    while now[0] > 0:
        ladders[now[0]][now[1]] = 0
        for dx, dy in dxdy:
            dx += now[0]
            dy += now[1]
            if 0 <= dx < LEN and 0 <= dy < LEN and ladders[dx][dy] == '1':
                now[0] = dx
                now[1] = dy
                break
    
    print("#" + tc, now[1])