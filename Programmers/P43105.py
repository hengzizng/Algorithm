def solution(triangle):
    d = [[0] * len(triangle) for _ in range(len(triangle[-1]))]
    d[0][0] = triangle[0][0]
    
    for i in range(len(triangle) - 1):
        for j in range(i + 1):
            d[i + 1][j] = max(d[i + 1][j], d[i][j] + triangle[i + 1][j])
            d[i + 1][j + 1] = max(d[i + 1][j + 1], d[i][j] + triangle[i + 1][j + 1])
    
    return max(d[-1])