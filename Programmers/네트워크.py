# Union-Find 사용
def solution(n, computers):
    def find(target):
        while target != network[target]:
            network[target] = network[network[target]]
            target = network[target]
        return target
    
    def union(computer1, computer2):
        computer1 = find(computer1)
        computer2 = find(computer2)
        
        network[max(computer1, computer2)] = min(computer1, computer2)
    
    
    network = list(range(n))
    
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union(i, j)
                
    for i in range(n):
        find(i)
    
    return len(set(network))