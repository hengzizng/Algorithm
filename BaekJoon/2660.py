from collections import defaultdict, deque
import sys
read = sys.stdin.readline


# BFS로 person 회원의 점수를 구해서 반환
def get_score(person):
    queue = deque([(person, 0)])
    visited = set([person])

    while queue:
        person, score = queue.popleft()

        for friend in friends[person]:
            if friend not in visited:
                queue.append((friend, score + 1))
                visited.add(friend)

    return score


# 회원의 수 ( <= 50 )
people_count = int(read())
# 친구 관계를 저장
friends = defaultdict(list)
while True:
    friend1, friend2 = map(int, read().split())
    friends[friend1].append(friend2)
    friends[friend2].append(friend1)

    # 입력 종료
    if friend1 == -1:
        break

# 점수별 회원번호 리스트
people_by_score = [[] for _ in range(people_count + 1)]
for person in range(1, people_count + 1):
    # person 회원의 점수를 구해 점수에 맞는 위치에 저장한다.
    people_by_score[get_score(person)].append(person)

# 점수 오름차순으로 확인
for score, people in enumerate(people_by_score):
    # 점수가 score인 사람이 존재한다면 출력 후 종료
    if people:
        print(score, len(people))
        print(*people)
        break
