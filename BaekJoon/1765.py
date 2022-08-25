import sys
read = sys.stdin.readline


def find(student):
    while student != friends[student]:
        friends[student] = friends[friends[student]]
        student = friends[student]

    return student


def union(student1, student2):
    student1 = find(student1)
    student2 = find(student2)

    friends[student2] = student1


n = int(read())  # 학생 수
m = int(read())  # 인간관계 수
friends = list(range(n + 1))  # 친구 정보
enemies = [[] for _ in range(n + 1)]  # 원수 정보

for _ in range(m):
    relation, p, q = read().strip().split()
    student1, student2 = int(p), int(q)
    if relation == 'F':  # 친구
        union(student1, student2)
    else:
        # student1의 원수는 student2의 친구
        for enemy in enemies[student1]:
            union(enemy, student2)
        # student2의 원수는 student1의 친구
        for enemy in enemies[student2]:
            union(enemy, student1)
        enemies[student1].append(student2)
        enemies[student2].append(student1)

team = set()
for student in range(1, n + 1):
    team.add(find(student))

print(len(team))
