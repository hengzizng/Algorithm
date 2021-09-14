# m: 열 수, n: 행 수, puddles: [[열, 행], ...]
def solution(m, n, puddles):
    village = [[0] * (m + 1) for _ in range(n + 1)]
    
    if len(puddles) > 0 and len(puddles[0]) > 1:
        for j, i in puddles:
            village[i][j] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j == 1 and i == 1 and village[i][j] != -1:
                village[i][j] = 1
                continue
            
            if village[i][j] == -1:
                village[i][j] = 0
                continue
                
            village[i][j] += village[i - 1][j] + village[i][j - 1]
    
    return village[-1][-1] % 1000000007

print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
# 아래 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)
print(solution(4, 3, [[1, 2], [2, 1]]), 0)