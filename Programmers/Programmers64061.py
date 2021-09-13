# # 테스트 1 〉	통과 (0.02ms, 10.3MB)
# # 테스트 2 〉	통과 (0.03ms, 10.2MB)
# # 테스트 3 〉	통과 (0.02ms, 10.2MB)
# # 테스트 4 〉	통과 (0.80ms, 10.2MB)
# # 테스트 5 〉	통과 (0.02ms, 10.2MB)
# # 테스트 6 〉	통과 (0.02ms, 10.1MB)
# # 테스트 7 〉	통과 (0.08ms, 10.1MB)
# # 테스트 8 〉	통과 (0.28ms, 10.3MB)
# # 테스트 9 〉	통과 (0.23ms, 10.3MB)
# # 테스트 10 〉	통과 (0.28ms, 10.3MB)
# # 테스트 11 〉	통과 (0.54ms, 10.3MB)
# def solution(board, moves):
#     answer = 0
#     bucket = []
    
#     depth = [0] * len(board[0])
#     for col in moves:
#         col -= 1
#         row = depth[col]
        
#         while row < len(board) - 1 and board[row][col] == 0:
#             depth[col] += 1
#             row = depth[col]
        
#         if bucket and bucket[-1] == board[row][col]:
#             bucket.pop()
#             answer += 2
#         elif board[row][col] != 0:
#             bucket.append(board[row][col])
            
#         board[row][col] = 0
        
#     return answer




# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.24ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.09ms, 10.1MB)
# 테스트 9 〉	통과 (0.08ms, 10.1MB)
# 테스트 10 〉	통과 (0.15ms, 10.1MB)
# 테스트 11 〉	통과 (0.16ms, 10.1MB)
from collections import deque


def solution(board, moves):
    heights = [0] * len(board)  # 각 열마다 가장 위 인형의 위치를 저장해둔다
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] > 0:
                heights[col] = row
                break

    stack = deque()
    count = 0
    for move in moves:
        move -= 1
        if heights[move] < len(board):
            doll = board[heights[move]][move]
            if not stack or stack[-1] != doll:
                stack.append(doll)
            else:
                stack.pop()
                count += 2
            heights[move] += 1

    return count

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
print("result", 4)