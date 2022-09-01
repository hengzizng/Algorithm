from collections import defaultdict
import sys
read = sys.stdin.readline


# no: 직원번호
def get_time(no):
    if not juniors[no]:
        return 0

    # no의 부하직원들이 각 자신의 부하직원들에게 전달하는 시간 => 내림차순 정렬
    times = []
    for junior in juniors[no]:
        times.append(get_time(junior))
    times.sort(reverse=True)

    # no의 부하직원들에게 전달하는 시간을 포함
    time = 0
    for i in range(len(juniors[no])):
        time = max(time, times[i] + i + 1)

    return time


# 직원 수
N = int(read())
# 상사 정보 (seniors[no]: no직원의 상사)
seniors = list(map(int, read().split()))
# 부하직원 정보 (juniors[no]: no직원의 부하직원 리스트)
juniors = defaultdict(list)
for no in range(N):
    juniors[seniors[no]].append(no)

print(get_time(0))
