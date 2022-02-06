def find(target):
    while target != friends[target]:
        friends[target] = friends[friends[target]]
        target = friends[target]

    return target


def union(x, y):
    x = find(x)
    y = find(y)

    if A[x] < A[y]:
        friends[y] = x
    else:
        friends[x] = y


# N: 학생 수, M: 친구관계 수, k: 준석이가 가진 돈
N, M, k = map(int, input().split())
# A: 각각의 학생이 원하는 친구비
A = list(map(int, input().split()))

friends = list(range(N))
for _ in range(M):
    v, w = map(int, input().split())
    union(v - 1, w - 1)

checked = set()
answer = 0
for i in range(N):
    friend = find(i)
    if friend in checked:
        continue

    if answer + A[friend] <= k:
        answer += A[friend]
        checked.add(friend)
    else:
        answer = "Oh no"
        break

print(answer)
