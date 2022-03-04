# 파이썬 정답 코드
# 28776KB	324ms
'''
import sys
input = sys.stdin.readline

a = [[]]
n, m, k = map(int, input().split())
graph = [[{} for _ in range(n+1)] for _ in range(n+1)]
nutrition = [[5] * (n + 1) for _ in range(n + 1)]
dead = []
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(n):
    a.append([0] + list(map(int, input().split())))

for _ in range(m):
    r, c, age = map(int, input().split())
    graph[r][c][age] = 1

def springSummerWinter():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j]:
                temp = {}
                dead = 0
                for age in sorted(graph[i][j].keys()):
                    num = graph[i][j][age]
                    if nutrition[i][j] - (age * num) >= 0:
                        nutrition[i][j] -= (age * num)
                        temp[age+1] = num
                    else:
                        survived = nutrition[i][j] // age
                        if not survived:
                            dead += age // 2 * num
                            continue
                        nutrition[i][j] -= age * survived
                        dead += age // 2 * (num - survived)
                        temp[age+1] = survived
                graph[i][j] = temp
                nutrition[i][j] += dead
            nutrition[i][j] += a[i][j]

def fall():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j]:
                num = 0
                for age in graph[i][j].keys():
                    if age % 5 == 0:
                        num += graph[i][j][age]
                if num:
                    for idx in range(8):
                        ni = i + di[idx]
                        nj = j + dj[idx]
                        if 0 < ni <= n and 0 < nj <= n:
                            if 1 not in graph[ni][nj].keys():
                                graph[ni][nj][1] = num
                            else: graph[ni][nj][1] += num

def count():
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            cnt += sum(graph[i][j].values())
    return cnt

for year in range(k):
    springSummerWinter()
    fall()

print(count())
'''


# 한 칸에 여러 개의 나무 위치 가능
# 처음 각 칸에는 5만큼의 양분이 있다

# 나무의 사계절
# 봄 : 자신의 나이만큼 양분을 먹고, 나이 1 증가
#      한 칸에 여러 개 있으면 어린 나무부터 양분을 먹는다
#      만약 양분이 부족하면 양분을 아예 못먹고 즉시 죽는다
# 여름 : 봄에 죽은 나무가 양분으로 변한다 (나무의 나이 // 2)
# 가을 : 나이가 5의 배수인 나무가 인접한 8개의 칸에 나이가 1로 번식
# 겨울 : 각 칸에 A[r][c] 만큼 양분 추가

# 나이가 어린 순 정렬 전제
# --- 각 위치별로 반복 ---
# is_lack - True: 양분 부족, False: 양분 부족하지 않음
#   False: 한 위치에서 나이가 어린 순으로 양분을 먹고, 나이 1 증가
#          나이가 5의 배수라면 breed_trees에 추가
#   True: add_val += 나이 // 2
# land[r][c] += add_val + A[r][c]
# --- 각 위치별로 반복 종료 ---
# breed_trees 번식


# K년이 지난 후 살아있는 나무의 개수


import sys
read = sys.stdin.readline


# 봄, 여름, 겨울
def do(r, c):
    add_val = 0  # 현재 위치에서 죽은 나무가 양분이 되어 더할 수
    new_trees = {}  # 이번 작업이 끝난 뒤 (r, c) 에 위치한 나무들의 수

    ages = sorted(tree_count[r][c].keys())  # 나이 오름차순으로 정렬
    for age in ages:  # 나이별로 반복
        count = tree_count[r][c][age]  # 나이가 age인 나무 수
        alive_count = min(land[r][c] // age, count)  # 나이가 age인 살 수 있는 나무 수

        add_val += (age // 2) * (count - alive_count)  # 나무들이 죽었을 때 변한 양분
        land[r][c] -= age * alive_count  # 살아있는 나무들이 양분 흡수

        new_trees[age + 1] = alive_count
        if (age + 1) % 5 == 0:
            breed_trees.append((r, c, alive_count))

    tree_count[r][c] = new_trees

    return add_val


# 나무가 번식할 수 있는 위치를 구하기 위한 배열
drdc = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

# N: 땅의 크기, M: 나무의 수, K: 연도 수
N, M, K = map(int, read().split())
land = [[5] * N for _ in range(N)]
# tree_count[r][c][age]: [r, c] 에 위치한 나이가 age인 나무들의 수
tree_count = [[{} for _ in range(N)] for _ in range(N)]


# A: 겨울에 추가할 양분
A = [list(map(int, read().split())) for _ in range(N)]
for _ in range(M):
    # [x, y]: 나무의 위치, z: 나무의 나이
    x, y, z = map(int, read().split())
    tree_count[x - 1][y - 1][z] = 1


for _ in range(K):
    # 각 위치별로 반복
    breed_trees = []  # 번식할 나무들
    for r in range(N):
        for c in range(N):
            add_val = do(r, c)
            land[r][c] += add_val + A[r][c]

    # 가을 - 나무 번식
    for r, c, count in breed_trees:
        for dr, dc in drdc:
            dr, dc = r + dr, c + dc
            if 0 <= dr < N and 0 <= dc < N:
                if 1 in tree_count[dr][dc]:
                    tree_count[dr][dc][1] += count
                else:
                    tree_count[dr][dc][1] = count

alive_count = 0
for i in range(N):
    for j in range(N):
        alive_count += sum(tree_count[i][j].values())
print(alive_count)
