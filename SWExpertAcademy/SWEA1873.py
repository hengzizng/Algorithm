import sys
sys.stdin = open("TestCase/SWExpertAcademy/1873input.txt")

def shoot():
    dx, dy = tank[0] + dxdy[tank[2]][0], tank[1] + dxdy[tank[2]][1]
    while 0 <= dx < H and 0 <= dy < W:
        if game_map[dx][dy] == '#':
            return
        elif game_map[dx][dy] == '*':
            game_map[dx][dy] = '.'
            return
        dx += dxdy[tank[2]][0]
        dy += dxdy[tank[2]][1]

def move(direction):
    tank[2] = direction
    game_map[tank[0]][tank[1]] = '.'
    dx, dy = tank[0] + dxdy[tank[2]][0], tank[1] + dxdy[tank[2]][1]
    if 0 <= dx < H and 0 <= dy < W and game_map[dx][dy] == '.':
        tank[0] = dx
        tank[1] = dy
    game_map[tank[0]][tank[1]] = directions[tank[2]]


dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
directions = ['^', 'v', '<', '>']
tank = [-1, -1, -1]
T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    game_map = []
    for h in range(H):
        game_map.append(list(input().strip()))
        for w in range(W):
            if game_map[h][w] == '^':
                tank[0] = h
                tank[1] = w
                tank[2] = 0
            elif game_map[h][w] == 'v':
                tank[0] = h
                tank[1] = w
                tank[2] = 1
            elif game_map[h][w] == '<':
                tank[0] = h
                tank[1] = w
                tank[2] = 2
            elif game_map[h][w] == '>':
                tank[0] = h
                tank[1] = w
                tank[2] = 3

    C = int(input())
    command = input()
    for c in range(C):
        if command[c] == 'S':
            shoot()
        elif command[c] == 'U':
            move(0)
        elif command[c] == 'D':
            move(1)
        elif command[c] == 'L':
            move(2)
        elif command[c] == 'R':
            move(3)

    print('#' + str(tc), end=" ")
    for h in range(H):
        print(''.join(game_map[h]))