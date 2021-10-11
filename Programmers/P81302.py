from collections import deque


def solution(places):
    def check(r, c, place):
        queue = deque([(r, c, 0)])
        visited = set()
        
        while queue:
            r, c, dist = queue.popleft()
            visited.add((r, c)) # 방문 체크를 여기서 해줘야 한다 (한 지점으로 갈 수 있는 경로는 여러개이기 때문에)
            
            for dr, dc in drdc:
                dr, dc = dr + r, dc + c
                if 0 <= dr < N and 0 <= dc < N and (dr, dc) not in visited and place[r][c] != 'X' and dist < 2:
                    if place[dr][dc] == 'P': # 다음에 갈 수 있는 곳에 사람이 있다면 무조건 불가능
                        return False
                    
                    queue.append((dr, dc, dist + 1))
                    
        return True
    
    
    
    drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    N = 5
    
    answer = []
    for place in places:
        follow_rule = True
        for r in range(N):
            for c in range(N):
                if place[r][c] == 'P':
                    if not check(r, c, place):
                        follow_rule = False
        
        if follow_rule:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer