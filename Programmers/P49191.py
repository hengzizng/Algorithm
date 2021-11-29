from collections import deque, defaultdict


def solution(n, results):
    def dfs(node, graph):
        stack = deque([node])
        checked = set([node])
        count = 0
        
        while stack:
            now_node = stack.pop()
            
            for next_node in graph[now_node]:
                if next_node not in checked:
                    checked.add(next_node)
                    stack.append(next_node)
                    count += 1
        
        return count
    
    
    wins, loses = defaultdict(list), defaultdict(list) # key에 해당하는 선수가 이긴/진 선수 목록
    for winner, loser in results:
        wins[winner].append(loser)
        loses[loser].append(winner)
        
    answer = 0
    for player in range(1, n + 1):
        # player에 해당하는 선수보다 순위가 높은 선수의 수 + 낮은 선수의 수가 총 선수의 수 - 1 이라면
        # 정확하게 순위를 매길 수 있다.
        if dfs(player, wins) + dfs(player, loses) == n - 1:
            answer += 1

    return answer