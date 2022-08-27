from collections import defaultdict
import sys
read = sys.stdin.readline


# 공의 수 (최대 색상 개수)
N = int(read())
# balls: 크기 오름차순 공 정보 [(크기, 색, 공 번호), ...]
balls = []
for no in range(N):
    color, size = map(int, read().split())
    balls.append((size, color, no))

# balls 공 크기 오름차순 정렬
balls.sort()

# total: 현재 인덱스까지의 모든 공들 크기의 합
total = 0
# sum_by_color: 현재 공까지의 각 색상별 공들 크기의 합
sum_by_color = defaultdict(int)
# answer[no]: no 공을 가진 플레이어가 잡을 수 있는 모든 공들의 크기 합
answer = [''] * N

# same_size: [크기가 같은 모든 공의 크기 합, 크기와 색상 모두 같은 공의 크기 합]
same_size = [0, 0]
# 공 크기 오름차순으로 누적합을 구함
for i in range(N):
    size, color, no = balls[i]

    # 같은 크기의 공은 잡아먹지 못하므로 빼줌
    if i > 0 and balls[i - 1][0] == size:
        same_size[0] += size
        # 같은 색상, 같은 크기의 공은 중복으로 빠지기 때문에 더해줌
        if balls[i - 1][1] == color:
            same_size[1] += size
        else:
            same_size[1] = 0
    else:
        same_size[0] = 0
        same_size[1] = 0
    answer[no] = str(total - sum_by_color[color] - same_size[0] + same_size[1])

    total += size
    sum_by_color[color] += size

# 출력
print('\n'.join(answer))

'''
import sys

input = sys.stdin.readline

n = int(input())
ball = []
for i in range(n):
    c, s = map(int, input().split())
    ball.append((c, s, i))
# 공의 크기 순으로 오름차순 정렬 (작은공 -> 큰공)
ball.sort(key=lambda x: x[1])
color_cnt = [0] * 200001
ans = [0] * n
total = 0

j = 0
for i in range(n):
    # i번째 공보다 작은 j번째 공의 크기, 색상 정보를 저장
    # ball[i]의 ans를 저장할 것이므로 해당 공보다 작은 ball[j]의 정보를 저장한다
    while ball[j][1] < ball[i][1]:
        color_cnt[ball[j][0]] += ball[j][1]
        total += ball[j][1]
        j += 1
    ans[ball[i][2]] = total - color_cnt[ball[i][0]]

for num in ans:
    print(num)
'''
