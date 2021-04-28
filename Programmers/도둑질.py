def solution(money):
    # d: [첫 번째 마을을 털었을 때, 첫 번째 마을을 안털었을 때]
    d = [[0] * 2 for _ in range(len(money))]
    
    d[0][0] = money[0]
    d[1][0] = max(money[0], money[1])
    d[1][1] = money[1]
    for i in range(2, len(money)):
        if i == len(money) - 1:
            d[i][0] = max(d[i - 1][0], d[i - 2][0] + money[i] - money[0], d[i - 2][0])
        else:
            d[i][0] = max(d[i - 1][0], d[i - 2][0] + money[i])
        d[i][1] = max(d[i - 1][1], d[i - 2][1] + money[i])
        
    return max(d[-1])


print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)