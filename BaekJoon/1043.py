from collections import defaultdict
import sys
read = sys.stdin.readline


# person이 참석하는 파티를 진실을 말하는 파티로 설정
def set_true(person):
    # person이 참석하는 모든 파티 반복
    for party_no in party_by_person[person]:
        # 거짓을 말하도록 되어있다면 변경해준다.
        if not true_party[party_no]:
            true_party[party_no] = True
            # 진실을 말하도록 변경된 파티에 참석한 모든 사람별 반복
            for attendant in people_by_party[party_no]:
                # 참석한 사람이 참석하는 모든 파티를 진실을 말하는 파티로 설정
                set_true(attendant)


# N: 사람 수, M: 파티 수
N, M = map(int, read().split())
# 진실을 아는 사람들 번호
true = list(map(int, read().split()))[1:]
# 파티별로 참석하는 사람들 리스트
people_by_party = []
# 사람별로 참석하는 파티 번호 리스트
party_by_person = defaultdict(list)
# 파티별로 진실을 말해야 하는지 여부
true_party = [False] * M

for m in range(M):
    # 파티에 오는 사람들 번호
    people = list(map(int, read().split()))[1:]
    people_by_party.append(people)
    for person in people:
        party_by_person[person].append(m)

for person in true:
    set_true(person)

count = 0
for m in range(M):
    if not true_party[m]:
        count += 1
print(count)
