from collections import defaultdict, deque
import sys
sys.stdin = open("TestCase/BaekJoon/1967input.txt", "r")
read = sys.stdin.readline


def getDiameter(leafs):
    distances = defaultdict(list)
    diameter = 0
    visited = leafs
    queue = deque()

    for leaf in leafs:
        track = set([leaf])
        queue.append((leaf, 0, track))

    while queue:
        node, weight, track = queue.popleft()

        for next_weight, next_node in linked[node]:
            if distances[node]:
                next_weight += max(distances[node])
            else:
                next_weight += weight
                
            if next_node not in visited and next_node not in track:
                visited.add(next_node)
                track.add(next_node)
                queue.append((next_node, next_weight, track))
            print("node", node, "next_node", next_node, "next_weight", next_weight)
            distances[next_node].append(next_weight)

    print(distances)
    
    return diameter


n = int(read()) # 노드의 개수
linked = defaultdict(list)
leafs = set(range(1, n + 1))
for _ in range(n - 1):
    parent, child, weight = map(int, read().split())
    linked[parent].append((weight, child))
    linked[child].append((weight, parent))
    if parent in leafs:
        leafs.remove(parent)

diameter = 0
diameter = getDiameter(leafs)
# for leaf in leafs:
#     diameter = max(diameter, getDiameter(leaf))

print(diameter)
