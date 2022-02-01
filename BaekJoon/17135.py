# 90 min

# 행 수: N, 열 수: M
# board[N] 에는 성 위치

# 궁수 총 3명
# 궁수는 성(board[N][?])에 위치
# 궁수는 각자 다른 칸
# 궁수 하나당 적 하나 공격 (적은 여러 궁수한테 공격받을 수 O)

# 턴
# 1. 공격 (궁수들 동시공격)
#   1-1. 거리가 D 이하인 적 중 가장 가까운 적
#   1-2. 1을 만족하는 적이 여럿일 때는 가장 왼쪽에 있는 적
#   1-3. 공격받은 적은 게임 제외
# 2. 공격이 끝나면 적이 이동
#   2-1. 아래로 한 칸 이동
#     2-1-1. 성이 있는 칸으로 이동한 경우 게임 제외

# 모든 적이 격자판에서 제외되면 게임 종료

# 궁수의 공격으로 제거할 수 있는 적의 최대 수


from collections import deque
import sys
read = sys.stdin.readline


# 궁수들의 위치 조합을 구하는 함수
def set_attackers(start, count, attackers):
    if count == 3:
        # 궁수들이 위치할 곳을 정하면 게임 시작
        set_board()
        removed_count[1] = 0
        
        # 행만큼 반복하면 모든 적은 무조건 사라진다
        for _ in range(N):
            play_game(attackers)
        removed_count[0] = max(removed_count)

        return
    
    for index in range(start, M):
        attackers[count] = index
        set_attackers(index + 1, count + 1, attackers)


def play_game(attackers):
    # 공격할 적을 구한다
    targets = get_targets(attackers)

    for target in targets:
        if board[target[0]][target[1]] == 1:
            removed_count[1] += 1 # 공격해서 없앤 적의 수를 증가시킨다
            board[target[0]][target[1]] = 0
    
    # 적들이 아래로 이동한다
    move_enemy()


# 각 궁수별로 공격할 적을 찾는 함수
def get_targets(attackers):
    targets = []
    queue = deque()

    for attacker in attackers: # 궁수별로 반복
        queue.append((N, attacker, 0)) # 행 위치, 열 위치, 거리
        visited = set()
        distance, target = N * M, [-1, -1]

        while queue:
            now = queue.popleft()
            
            for dr, dc in drdc:
                nr, nc = now[0] + dr, now[1] + dc

                # 이미 적을 찾았는데 새로 확인할 곳의 거리가 더 멀다면 탐색 종료
                if distance < now[2]:
                    queue.clear()
                    break
                
                if nr < 0 or nr >= N or nc < 0 or nc >= M or now[2] + 1 > D or (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))

                # 빈 칸일 떄
                if board[nr][nc] == 0:
                    queue.append((nr, nc, now[2] + 1))
                    continue
                
                # 적을 찾았을 때
                if now[2] + 1 < distance: # 이번에 적을 새로 찾았다면
                    distance = now[2] + 1
                    target[0], target[1] = nr, nc
                elif now[2] + 1 == distance: # 이미 찾은 적과 거리가 같다면
                    if nc < target[1]: # 더 왼쪽에 있는 적으로 변경
                        target[0], target[1] = nr, nc
        
        if target[0] > -1: # 공격할 적을 찾았을 때만 추가
            targets.append(target)

    return targets


# 적들이 아래로 한 칸 움직이는 함수
def move_enemy():
    for m in range(M):
        for n in range(N - 1, 1 - 1, -1):
            board[n][m] = board[n - 1][m]
    for m in range(M):
        board[0][m] = 0


# board를 초기 상태로 다시 세팅한다
def set_board():
    for n in range(N):
        for m in range(M):
            board[n][m] = init_board[n][m]


drdc = [[0, -1], [-1, 0], [0, 1]]

# [0]: 궁수의 공격으로 제거할 수 있는 적의 최대 수, [1]: 이번에 제거한 적의 수
removed_count = [0, 0]

# N: 행 수, M: 열 수, D: 공격 거리 제한
N, M, D = map(int, read().split())
init_board, board = [], [[0] * M for _ in range(N)] # 0: 빈 칸, 1: 적이 있는 칸
for n in range(N):
    init_board.append(list(map(int, read().split())))

set_attackers(0, 0, [0] * 3)

print(removed_count[0])