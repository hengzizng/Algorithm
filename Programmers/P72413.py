'''
풀이1 > 다익스트라 사용 (45 min)

정확성  테스트
테스트 1 〉 통과 (0.03ms, 10.3MB)
테스트 2 〉 통과 (0.02ms, 10.3MB)
테스트 3 〉 통과 (0.03ms, 10.2MB)
테스트 4 〉 통과 (0.09ms, 10.3MB)
테스트 5 〉 통과 (0.06ms, 10.3MB)
테스트 6 〉 통과 (0.08ms, 10.3MB)
테스트 7 〉 통과 (0.17ms, 10.3MB)
테스트 8 〉 통과 (0.20ms, 10.3MB)
테스트 9 〉 통과 (0.14ms, 10.4MB)
테스트 10 〉 통과 (0.11ms, 10.4MB)

효율성  테스트
테스트 1 〉 통과 (2.81ms, 10.2MB)
테스트 2 〉 통과 (7.83ms, 10.6MB)
테스트 3 〉 통과 (3.50ms, 10.3MB)
테스트 4 〉 통과 (2.64ms, 10.3MB)
테스트 5 〉 통과 (3.15ms, 10.2MB)
테스트 6 〉 통과 (3.54ms, 10.3MB)
테스트 7 〉 통과 (56.32ms, 15.6MB)
테스트 8 〉 통과 (53.29ms, 15.6MB)
테스트 9 〉 통과 (20.32ms, 15.5MB)
테스트 10 〉 통과 (24.38ms, 15.4MB)
테스트 11 〉 통과 (22.07ms, 15.5MB)
테스트 12 〉 통과 (27.86ms, 12.9MB)
테스트 13 〉 통과 (36.35ms, 13MB)
테스트 14 〉 통과 (30.55ms, 13MB)
테스트 15 〉 통과 (32.09ms, 12.9MB)
테스트 16 〉 통과 (2.21ms, 10.3MB)
테스트 17 〉 통과 (2.23ms, 10.3MB)
테스트 18 〉 통과 (2.96ms, 10.3MB)
테스트 19 〉 통과 (5.66ms, 10.6MB)
테스트 20 〉 통과 (8.94ms, 10.6MB)
테스트 21 〉 통과 (8.23ms, 10.7MB)
테스트 22 〉 통과 (28.07ms, 12.9MB)
테스트 23 〉 통과 (25.67ms, 12.9MB)
테스트 24 〉 통과 (31.66ms, 13MB)
테스트 25 〉 통과 (1.77ms, 10.1MB)
테스트 26 〉 통과 (1.14ms, 10.2MB)
테스트 27 〉 통과 (7.60ms, 10.6MB)
테스트 28 〉 통과 (8.11ms, 10.6MB)
테스트 29 〉 통과 (1.40ms, 10.2MB)
테스트 30 〉 통과 (1.66ms, 10.4MB)
'''

from collections import defaultdict
import heapq

# n: 지점개수, s: 출발지, a/b: 도착지, fares: {지점1, 지점2, 지점1-2의 택시요금}
def solution(n, s, a, b, fares):
    # start - 모든지점 의 최소비용을 구하는 함수
    def get_cost_from_start(start):
        cost_from_start = [float('inf')] * (n + 1)
        pq = []
        
        cost_from_start[start] = 0
        heapq.heappush(pq, (start, 0))
        
        while pq:
            now_spot, now_cost = heapq.heappop(pq)
            
            if now_cost > cost_from_start[now_spot]:
                continue
            
            for next_spot, next_cost in costs[now_spot]:
                next_cost += now_cost
                if next_cost < cost_from_start[next_spot]:
                    cost_from_start[next_spot] = next_cost
                    heapq.heappush(pq, (next_spot, next_cost))
        
        return cost_from_start

    
    costs = defaultdict(list)
    for spot1, spot2, fare in fares:
        costs[spot1].append((spot2, fare))
        costs[spot2].append((spot1, fare))
    
    # 출발지 - 모든지점 의 최소비용을 구한다
    cost_from_s = get_cost_from_start(s)
    
    # A의 도착지 - 모든지점 의 최소비용을 구한다
    cost_from_a = get_cost_from_start(a)
    
    # B의 도착지 - 모든지점 의 최소비용을 구한다
    cost_from_b = get_cost_from_start(b)
    
    # (출발지 - A의 도착지) + (출발지 - B의 도착지) 를 기본으로 두고 가장 싼 비용을 찾는다
    min_cost = cost_from_s[a] + cost_from_s[b]
    for spot in range(1, n + 1):
        min_cost = min(min_cost, cost_from_s[spot] + cost_from_a[spot] + cost_from_b[spot])
    
    return min_cost

'''
풀이2 > 플로이드 워셜 사용 (45 min)

정확성  테스트
테스트 1 〉 통과 (0.06ms, 10.3MB)
테스트 2 〉 통과 (0.08ms, 10.3MB)
테스트 3 〉 통과 (0.06ms, 10.3MB)
테스트 4 〉 통과 (0.18ms, 10.3MB)
테스트 5 〉 통과 (0.32ms, 10.2MB)
테스트 6 〉 통과 (0.46ms, 10.3MB)
테스트 7 〉 통과 (0.35ms, 10.3MB)
테스트 8 〉 통과 (0.74ms, 10.3MB)
테스트 9 〉 통과 (0.99ms, 10.4MB)
테스트 10 〉 통과 (1.34ms, 10.4MB)

효율성  테스트
테스트 1 〉 통과 (138.81ms, 10.5MB)
테스트 2 〉 통과 (460.07ms, 11.1MB)
테스트 3 〉 통과 (1038.62ms, 11.5MB)
테스트 4 〉 통과 (1027.48ms, 11.5MB)
테스트 5 〉 통과 (1053.55ms, 11.4MB)
테스트 6 〉 통과 (1057.89ms, 11.4MB)
테스트 7 〉 통과 (1100.36ms, 13.8MB)
테스트 8 〉 통과 (1117.67ms, 14.1MB)
테스트 9 〉 통과 (1118.77ms, 12.9MB)
테스트 10 〉 통과 (1118.60ms, 12.9MB)
테스트 11 〉 통과 (1145.21ms, 12.9MB)
테스트 12 〉 통과 (1084.15ms, 12.9MB)
테스트 13 〉 통과 (1109.09ms, 12.8MB)
테스트 14 〉 통과 (1081.15ms, 12.9MB)
테스트 15 〉 통과 (1085.91ms, 12.8MB)
테스트 16 〉 통과 (1034.10ms, 11.4MB)
테스트 17 〉 통과 (1054.92ms, 11.4MB)
테스트 18 〉 통과 (1029.36ms, 11.3MB)
테스트 19 〉 통과 (1068.05ms, 11.5MB)
테스트 20 〉 통과 (1066.36ms, 11.7MB)
테스트 21 〉 통과 (1094.26ms, 11.7MB)
테스트 22 〉 통과 (1100.77ms, 12.8MB)
테스트 23 〉 통과 (1090.38ms, 12.7MB)
테스트 24 〉 통과 (1096.74ms, 12.8MB)
테스트 25 〉 통과 (1046.10ms, 11.2MB)
테스트 26 〉 통과 (998.29ms, 11MB)
테스트 27 〉 통과 (882.39ms, 10.6MB)
테스트 28 〉 통과 (977.78ms, 10.6MB)
테스트 29 〉 통과 (133.33ms, 10.4MB)
테스트 30 〉 통과 (138.03ms, 10.3MB)
'''

from collections import defaultdict
import heapq

# n: 지점개수, s: 출발지, a/b: 도착지, fares: {지점1, 지점2, 지점1-2의 택시요금}
def solution(n, s, a, b, fares):
    min_costs = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for spot1, spot2, fare in fares:
        min_costs[spot1][spot2] = fare
        min_costs[spot2][spot1] = fare
    
    for waypoint in range(1, n + 1):
        min_costs[waypoint][waypoint] = 0
        for spot1 in range(1, n + 1):
            for spot2 in range(1, n + 1):
                if min_costs[spot1][waypoint] + min_costs[waypoint][spot2] < min_costs[spot1][spot2]:
                    min_costs[spot1][spot2] = min_costs[spot1][waypoint] + min_costs[waypoint][spot2]
                    
    min_cost = min_costs[s][a] + min_costs[s][b]
    for spot in range(1, n + 1):
        min_cost = min(min_cost, min_costs[s][spot] + min_costs[a][spot] + min_costs[b][spot])
    
    return min_cost