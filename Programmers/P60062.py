from heapq import heappush, heappop


def solution(n, weak, dist):
    # 위치가 속한 집합의 대표값을 찾는다.
    def find(spot):
        while spot != parent[spot]:
            parent[spot] = parent[parent[spot]]
            spot = parent[spot]
        return spot
    
    # 두 위치를 한 집합에 넣는다.
    def union(distance, spot1, spot2):
        parent1 = find(spot1)
        parent2 = find(spot2)
        parent[parent2] = parent1
        
        # 두 위치가 이미 같은 집합이었다면
        if parent1 == parent2:
            return
        
        # 두 집합이 합쳐졌다면 두 개의 대표값 중 하나 제거
        parent_set.remove(parent2)
        distance_by_parent[parent1] += distance_by_parent.pop(parent2) + distance
        
    
    # 현재 만들어진 집합들을 모두 방문할 수 있는지
    def is_valid():
        # 방문해야 할 위치 집합이 친구 수보다 많다면
        if len(parent_set) > len(dist):
            return False
        
        # 방문해야 할 위치 집합별 거리 중 친구들이 방문할 수 없는 거리가 있다면
        distance_list = sorted(list(distance_by_parent.values()))
        for i in range(len(distance_list)):
            if dist[i] < distance_list[i]:
                return False

        return True
    
    
    dist.sort(reverse=True) # 각 친구의 이동 거리 내림차순 정렬
    
    parent = {} # 각 위치가 속한 집합의 대표값
    parent_set = set() # 만들어진 집합들의 대표값 집합
    distance_by_parent = {} # 각 집합별 거리
    # 초기화
    for spot in weak:
        parent[spot] = spot
        parent_set.add(spot)
        distance_by_parent[spot] = 0
    
    # 각 위치에서 다른 모든 위치까지의 최소 거리를 구한다.
    distances = [] # (거리, 위치1, 위치2)
    for i in range(len(weak)):
        for j in range(i + 1, len(weak)):
            spot1, spot2 = weak[i], weak[j]
            
            distance = min(spot2 - spot1, spot1 + n - spot2)
            heappush(distances, (distance, spot1, spot2))
    
    # 거리가 짧은 순으로 반복해서 집합을 만들다가 모든 위치를 방문했다면 중단
    friend_count = n
    while distances:
        distance, spot1, spot2 = heappop(distances)
        union(distance, spot1, spot2)
        
        # 방문 가능한 상태라면 친구 수 갱신
        if is_valid():
            friend_count = min(friend_count, len(parent_set))
        
        # if len(parent_set) == 1:
        #     break
    
    return -1 if friend_count == n else friend_count