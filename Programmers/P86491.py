'''
# 효율성을 개선한 풀이
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.07ms, 10.2MB)
# 테스트 12 〉	통과 (0.11ms, 10.2MB)
# 테스트 13 〉	통과 (0.35ms, 10.3MB)
# 테스트 14 〉	통과 (0.64ms, 10.4MB)
# 테스트 15 〉	통과 (0.98ms, 10.5MB)
# 테스트 16 〉	통과 (1.49ms, 10.6MB)
# 테스트 17 〉	통과 (2.18ms, 10.8MB)
# 테스트 18 〉	통과 (2.52ms, 10.8MB)
# 테스트 19 〉	통과 (2.54ms, 11.4MB)
# 테스트 20 〉	통과 (3.09ms, 11.4MB)
def solution(sizes):
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)
'''

# 내 풀이
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (0.16ms, 10.3MB)
# 테스트 11 〉	통과 (0.31ms, 10.2MB)
# 테스트 12 〉	통과 (0.46ms, 10.3MB)
# 테스트 13 〉	통과 (1.60ms, 10.3MB)
# 테스트 14 〉	통과 (3.67ms, 10.5MB)
# 테스트 15 〉	통과 (4.53ms, 10.3MB)
# 테스트 16 〉	통과 (10.01ms, 10.8MB)
# 테스트 17 〉	통과 (10.64ms, 11MB)
# 테스트 18 〉	통과 (12.71ms, 10.9MB)
# 테스트 19 〉	통과 (17.88ms, 11.4MB)
# 테스트 20 〉	통과 (14.40ms, 11.2MB)
def solution(sizes):
    width, height = [0, 0], [0, 0] # 현재까지 만들 수 있는 가장 작은 지갑의 가로, 세로 길이 : [이번 명함 정방향, 눕힌 방향]
    
    for w, h in sizes:
        # 이번 명함을 정방향으로 둘 때, 이번 명함까지 담을 수 있는 가장 작은 지갑의 크기를 구한다
        w1, h1 = max(w, width[0]), max(h, height[0])
        w2, h2 = max(w, width[1]), max(h, height[1])
        area1, area2 = w1 * h1, w2 * h2
        
        # 이번 명함을 눕혀서 둘 때, 이번 명함까지 담을 수 있는 가장 작은 지갑의 크기를 구한다
        w3, h3 = max(h, width[0]), max(w, height[0])
        w4, h4 = max(h, width[1]), max(w, height[1])
        area3, area4 = w3 * h3, w4 * h4
        
        if area1 < area2:
            width[0], height[0] = w1, h1
        else:
            width[0], height[0] = w2, h2

        if area3 < area4:
            width[1], height[1] = w3, h3
        else:
            width[1], height[1] = w4, h4
    
    return min(width[0] * height[0], width[1] * height[1])