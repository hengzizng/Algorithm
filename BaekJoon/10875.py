import sys
read = sys.stdin.readline


drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북동남서
SIZE = 2 * int(read()) + 1  # 격자의 실제 크기
N = int(read())  # 방향 회전 수

time, end_time = 0, -1  # 현재 시각, 종료 시각
snake = set()  # 뱀의 위치
r, c, d = SIZE // 2, SIZE // 2 - 1, 1  # 뱀의 머리 정보 [행, 열, 방향]

for _ in range(N):
    time_str, d_str = read().strip().split()
    
    # 이미 뱀이 죽었다면
    if end_time > -1:
        continue

    # 방향 전환하기 전까지 계속 이동
    for _ in range(int(time_str)):
        time += 1
        nr, nc = r + drdc[d][0], c + drdc[d][1]
        if nr < 0 or nr >= SIZE or nc < 0 or nc >= SIZE or (SIZE * nr + nc) in snake:
            end_time = time
            break

        # 뱀의 머리 이동
        r, c = nr, nc
        snake.add(SIZE * r + c)

    # 방향 전환
    d = (d + (3 if d_str == 'L' else 1)) % 4

print(end_time)