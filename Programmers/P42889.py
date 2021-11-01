# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.15ms, 10.4MB)
# 테스트 3 〉	통과 (1.75ms, 10.5MB)
# 테스트 4 〉	통과 (9.24ms, 11MB)
# 테스트 5 〉	통과 (20.08ms, 15MB)
# 테스트 6 〉	통과 (0.23ms, 10.3MB)
# 테스트 7 〉	통과 (1.28ms, 10.4MB)
# 테스트 8 〉	통과 (9.12ms, 10.9MB)
# 테스트 9 〉	통과 (20.12ms, 15MB)
# 테스트 10 〉	통과 (9.15ms, 11MB)
# 테스트 11 〉	통과 (9.54ms, 10.9MB)
# 테스트 12 〉	통과 (13.23ms, 11.4MB)
# 테스트 13 〉	통과 (15.38ms, 11.4MB)
# 테스트 14 〉	통과 (0.04ms, 10.2MB)
# 테스트 15 〉	통과 (5.12ms, 10.6MB)
# 테스트 16 〉	통과 (3.50ms, 10.2MB)
# 테스트 17 〉	통과 (6.45ms, 10.6MB)
# 테스트 18 〉	통과 (3.42ms, 10.3MB)
# 테스트 19 〉	통과 (1.04ms, 10.3MB)
# 테스트 20 〉	통과 (4.63ms, 10.3MB)
# 테스트 21 〉	통과 (8.98ms, 11MB)
# 테스트 22 〉	통과 (20.83ms, 18.1MB)
# 테스트 23 〉	통과 (18.51ms, 11.7MB)
# 테스트 24 〉	통과 (18.42ms, 11.6MB)
# 테스트 25 〉	통과 (0.02ms, 10.4MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.3MB)
# def solution(N, stages):
#     # user_in_step : stage에 도전 중인(클리어하지 못한) 사용자 수
#     user_in_step = [0] * (N + 1)
    
#     # complete : 마지막 stage까지 클리어 한 사용자 수
#     complete = 0
#     for stage in stages:
#         if stage == N + 1:
#             complete += 1
#             continue
#         user_in_step[stage] += 1
    
#     # divisor : 실패율을 구하기 위해 나누는 수(스테이지에 도달한 사용자 수)
#     divisor = complete
#     for i in range(N, 1 - 1, -1):
#         divisor += user_in_step[i]
#         if divisor != 0:
#             user_in_step[i] /= divisor
        
#     # user_in_step의 인덱스는 0~N으로 이루어져있기 때문에 인덱스 0 삭제
#     del user_in_step[0]
    
#     stages = [_ for _ in range(1, N+1)]
#     answer = list(zip(user_in_step, stages))
#     answer = sorted(answer, key = lambda x: (-x[0], x[1]))    
    
#     return list(zip(*answer))[1]



# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.14ms, 10.2MB)
# 테스트 3 〉	통과 (1.98ms, 10.6MB)
# 테스트 4 〉	통과 (14.16ms, 11MB)
# 테스트 5 〉	통과 (32.96ms, 15.1MB)
# 테스트 6 〉	통과 (0.19ms, 10.2MB)
# 테스트 7 〉	통과 (1.29ms, 10.4MB)
# 테스트 8 〉	통과 (14.11ms, 10.9MB)
# 테스트 9 〉	통과 (34.16ms, 15.1MB)
# 테스트 10 〉	통과 (15.38ms, 10.9MB)
# 테스트 11 〉	통과 (14.12ms, 10.8MB)
# 테스트 12 〉	통과 (23.53ms, 11.4MB)
# 테스트 13 〉	통과 (22.80ms, 11.4MB)
# 테스트 14 〉	통과 (0.04ms, 10.3MB)
# 테스트 15 〉	통과 (8.95ms, 10.7MB)
# 테스트 16 〉	통과 (4.76ms, 10.4MB)
# 테스트 17 〉	통과 (9.04ms, 10.6MB)
# 테스트 18 〉	통과 (4.52ms, 10.4MB)
# 테스트 19 〉	통과 (0.99ms, 10.3MB)
# 테스트 20 〉	통과 (6.40ms, 10.4MB)
# 테스트 21 〉	통과 (12.85ms, 10.9MB)
# 테스트 22 〉	통과 (40.33ms, 18.4MB)
# 테스트 23 〉	통과 (29.45ms, 11.7MB)
# 테스트 24 〉	통과 (27.17ms, 11.7MB)
# 테스트 25 〉	통과 (0.01ms, 10.3MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.3MB)
from collections import defaultdict


def solution(N, stages):
    # not_clear = {stage : stage에 도전 중인 user 수}
    # 1:1 2:3 3:2 4:1 5:0 6:1
    not_clear = defaultdict(int)
    
    # arrived = {stage : stage에 도달한 user 수}
    # 1:8 2:7 3:4 4:2 5:1 6:1
    arrived = defaultdict(int)
    
    for stage in stages:
        not_clear[stage] += 1
        arrived[stage] += 1
    
    add_value = arrived[N + 1]
    for stage in range(N, 1 - 1, -1):
        arrived[stage] += add_value
        add_value = arrived[stage]
    
    for_sort = []
    for stage in range(1, N + 1):
        temp = arrived[stage]
        for_sort.append((0 if temp == 0 else not_clear[stage] / temp, -1 * stage))
    for_sort.sort(reverse = True)
    
    return list(map(lambda x: -1 * x[1], for_sort))