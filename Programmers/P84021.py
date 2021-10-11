from collections import deque


def solution(game_board, table):    
    def rotate(puzzle): # 퍼즐조각을 시계 방향으로 회전시키는 함수
        rotated = set()
        min_row, min_col = 50, 50 # 찾은 위치들을 왼쪽 위로 옮겨주기 위해 사용
        
        for row, col in puzzle:
            rotated.add((col, -1 * row))
            min_row, min_col = min(min_row, col), min(min_col, (-1 * row))
            
        # 찾은 위치들을 왼쪽 위로 옮긴다
        moved = set()
        for row, col in rotated:
            moved.add((row - min_row, col - min_col))
        
        return moved
    
    def find(row, col, ver): # bfs를 사용해 퍼즐조각 하나 / 빈 칸들을 찾는 함수
        size = len(table)
        min_row, min_col = 50, 50 # 찾은 위치들을 왼쪽 위로 옮겨주기 위해 사용
        target = set() # 나중에 빈 칸과의 비교를 쉽게 하기 위해 집합으로 둔다
        
        queue = deque([(row, col)])
        visit(row, col, ver)
        
        while queue:
            row, col = queue.popleft()
            target.add((row, col))
            min_row, min_col = min(min_row, row), min(min_col, col)
            
            for dr, dc in drdc:
                dr, dc = row + dr, col + dc
                
                if 0 <= dr < size and 0 <= dc < size and condition(dr, dc, ver):
                    queue.append((dr, dc))
                    visit(dr, dc, ver)
        
        # 찾은 위치들을 왼쪽 위로 옮긴다
        moved = set()
        for row, col in target:
            moved.add((row - min_row, col - min_col))
        
        return moved
    
    def condition(row, col, ver): # ver에 따라 해당 위치가 조건에 맞는지 확인
        result = False
        
        if ver == 0: # table에서 퍼즐을 찾음
            if table[row][col] == 1:
                result = True
        else: # game_board에서 빈 칸을 찾음
            if game_board[row][col] == 0:
                result = True
        
        return result
    
    def visit(row, col, ver): # ver에 따라 방문 처리를 해준다.
        if ver == 0: # 퍼즐 찾을 때
            table[row][col] = 0
        else: # 빈칸 찾을 때
            game_board[row][col] = 1
    
    def match(blank, puzzles): # 모든 퍼즐을 돌며 빈 칸에 맞는 것이 있는지 체크해서 있다면 채운 칸 수 반환
        for index, puzzle in enumerate(puzzles):
            if used[index]: # 이미 사용한 퍼즐이면 사용할 수 없다
                continue

            for _ in range(4):
                if blank == puzzle:
                    used[index] = True
                    return len(blank)
                puzzle = rotate(puzzle)
            
        return 0
    
    
    drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    size = len(table)
    
    # 모든 퍼즐을 찾는다.
    puzzles = []
    for row in range(size):
        for col in range(size):
            if condition(row, col, 0):
                puzzles.append(find(row, col, 0))
                
    used = [False] * len(puzzles)
    
    # 모든 빈 칸을 찾으며 퍼즐 중에 맞는 것이 있는지 체크한다.
    answer = 0
    for row in range(size):
        for col in range(size):
            if condition(row, col, 1):
                blank = find(row, col, 1)
                answer += match(blank, puzzles)
    
    return answer