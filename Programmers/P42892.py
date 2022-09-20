from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


def solution(nodeinfo):
    def search(x_idx, y_idx, min_x, max_x):
        y = y_list[y_idx]
        x, node = x_by_y[y][x_idx]

        # 이번 노드가 자식 노드가 될 수 없는 경우
        if x < min_x or x > max_x:
            return False

        # 전위 순회: 부모 -> 왼쪽 자식 -> 오른쪽 자식
        result[0].append(node)

        # 이번 노드가 리프 노드가 아닌 경우
        if y_idx + 1 < len(y_list):
            child_y = y_list[y_idx + 1]  # 이번 노드의 자식 y좌표
            for child_x_idx in range(len(x_by_y[child_y])):
                child_node = x_by_y[child_y][child_x_idx][1]

                # 왼쪽 서브 트리
                if search(child_x_idx, y_idx + 1, min_x, x - 1):
                    tree[node][0] = child_node
                # 오른쪽 서브 트리
                elif search(child_x_idx, y_idx + 1, x + 1, max_x):
                    tree[node][1] = child_node

        # 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 부모
        result[1].append(node)

        return True

    tree = {}  # tree[node]: node의 [왼쪽, 오른쪽] 서브 트리
    y_list = set()  # y좌표 목록
    x_by_y = defaultdict(list)  # y좌표별 (x좌표, 노드번호) 목록
    for node, xy in enumerate(nodeinfo, 1):
        tree[node] = [0, 0]
        y_list.add(xy[1])
        x_by_y[xy[1]].append((xy[0], node))

    y_list = sorted(list(y_list), reverse=True)  # y좌표 내림차순 정렬
    for y in y_list:
        x_by_y[y].sort()  # 각 y좌표별로 x좌표 오름차순 정렬

    # 탐색 시작
    result = [[], []]
    search(0, 0, 0, 100000)

    return result


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
      [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
print([[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]])
print("-------")
print(solution([[0, 0]]))
print([[1], [1]])
print("-------")
print(solution([[0, 0], [100000, 1000000]]))
print([[2, 1], [1, 2]])
