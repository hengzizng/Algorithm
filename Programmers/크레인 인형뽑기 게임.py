def solution(board, moves):
    answer = 0
    bucket = []
    
    depth = [0] * len(board[0])
    for col in moves:
        col -= 1
        row = depth[col]
        
        while row < len(board) - 1 and board[row][col] == 0:
            depth[col] += 1
            row = depth[col]
        
        if bucket and bucket[-1] == board[row][col]:
            bucket.pop()
            answer += 2
        elif board[row][col] != 0:
            bucket.append(board[row][col])
            
        board[row][col] = 0
        
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves), 4)