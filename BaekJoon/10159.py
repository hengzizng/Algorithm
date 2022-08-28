from collections import defaultdict, deque
import sys
read = sys.stdin.readline


# 물건 no보다 가볍거나 무거운 물건의 수 반환
def get_count(no):
    queue = deque([(no, 0), (no, 1)])
    checked = set([no])

    while queue:
        # now_no: 물건번호, light_or_heavy: 다음으로 가벼운/무거운 물건으로 이동
        now_no, light_or_heavy = queue.popleft()

        # 물건 now_no보다 가벼운 물건
        if light_or_heavy == 0:
            for next_no in light[now_no]:
                if next_no not in checked:
                    queue.append((next_no, light_or_heavy))
                    checked.add(next_no)
        # 물건 now_no보다 무거운 물건
        else:
            for next_no in heavy[now_no]:
                if next_no not in checked:
                    queue.append((next_no, light_or_heavy))
                    checked.add(next_no)

    return len(checked) - 1


# N: 전체 물건 개수, M: 측정 결과 수
N, M = int(read()), int(read())
# light[no] / heavy[no]: no보다 가벼운/무거운 물건들 리스트
light = defaultdict(list)
heavy = defaultdict(list)
for _ in range(M):
    # no1 무게 > no2 무게
    no1, no2 = map(lambda x: int(x) - 1, read().split())
    light[no1].append(no2)
    heavy[no2].append(no1)

for no in range(N):
    print(N - 1 - get_count(no))
