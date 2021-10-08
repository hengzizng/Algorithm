def solution(rows, columns, queries):
    def print_matrix(matrix):
        for i in range(rows):
            for j in range(columns):
                print(matrix[i][j], end=" ")
            print()
        print()


    def rotate(x1, y1, x2, y2):
        # print("-----------------------")
        temp = matrix[x1][y1]
        min_num = temp

        x, y, d = x1, y1, 0 # d: 방향
        while True:
            nx, ny = x + dxdy[d][0], y + dxdy[d][1]

            if nx < x1 or nx > x2 or ny < y1 or ny > y2:
                d += 1
                if d <= 3:
                    nx, ny = x + dxdy[d][0], y + dxdy[d][1]
                else:
                    break
            
            # print(x, y, matrix[x][y], "에", nx, ny, matrix[nx][ny], "을 저장")
            min_num = min(min_num, matrix[nx][ny])
            matrix[x][y] = matrix[nx][ny]
            # print_matrix(matrix)
            x, y = nx, ny
        matrix[x1][y1 + 1] = temp
        # print_matrix(matrix)
        return min_num


    answer = []

    num = 1
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(num)
            num += 1
    
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 아래, 오른쪽, 위, 왼쪽
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1 # 인덱스 맞춰주기 위해 1씩 뺀다
        answer.append(rotate(x1, y1, x2, y2))

    return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries), [8, 10, 25])

rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries), [1, 1, 5, 3])

rows = 100
columns = 97
queries = [[1,1,100,97]]
print(solution(rows, columns, queries), [1])