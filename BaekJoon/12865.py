import sys
read = sys.stdin.readline

# N: 물품의 수, K: 최대 무게
N, K = map(int, read().split())
item_info = [tuple(map(int, read().split())) for _ in range(N)]

d = [0] * (K + 1)
# W: 각 물건의 무게, V: 각 물건의 가치
for W, V in item_info:
    # max_weight: 최대 수용 무게
    for max_weight in range(K, -1, -1):
        if W <= max_weight and d[max_weight] < d[max_weight - W] + V:
            d[max_weight] = d[max_weight - W] + V

print(d[K])
