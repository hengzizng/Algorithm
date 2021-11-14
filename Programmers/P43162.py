def solution(n, computers):
    def union(a, b):
        a = find(a)
        b = find(b)
        
        parents[b] = a
        
    def find(target):
        while target != parents[target]:
            parents[target] = parents[parents[target]]
            target = parents[target]
            
        return target
    
    
    parents = list(range(n))
    for com1 in range(n):
        for com2 in range(n):
            if computers[com1][com2] == 1:
                union(com1, com2)
    
    networks = set()
    for com in range(n):
        networks.add(find(com))
    
    return len(networks)