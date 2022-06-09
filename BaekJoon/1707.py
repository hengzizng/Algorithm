from collections import deque, defaultdict
import sys
read = sys.stdin.readline


def is_bipartite_graph(start, visit, graph):
    queue = deque([(start, 1)])  # 노드번호, 노드 색(분류)
    visit[start] = 1

    while queue:
        node, type = queue.popleft()

        type *= -1

        for next_node in graph[node]:
            if visit[next_node] == 0:  # 아직 방문하지 않은 정점이라면
                visit[next_node] = type
                queue.append((next_node, type))
            else:  # 방문한 정점이라면
                if visit[next_node] != type:  # 방문한 정점인데 노드 분류가 이번과 다르다면
                    return "NO"

    return "YES"


answers = []
K = int(read())  # 테스트 케이스 수
for _ in range(K):
    V, E = map(int, read().split())

    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, read().split())
        graph[u].append(v)
        graph[v].append(u)

    answer = "YES"
    visit = [0] * (V + 1)
    for node in range(1, V + 1):  # 모든 정점이 연결되어있지 않을 수도 있기 때문에 전부 확인해준다
        if visit[node] == 0:  # 방문하지 않은 정점만 확인한다
            answer = is_bipartite_graph(node, visit, graph)
            if answer == "NO":  # 이미 하나의 이분그래프가 아닌 그래프를 찾았다면 더 볼 필요 X
                break
    answers.append(answer)

for answer in answers:
    print(answer)
