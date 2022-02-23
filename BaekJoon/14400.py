import sys
read = sys.stdin.readline


n = int(read())  # 고객 수
customers_x, customers_y = [], []
for _ in range(n):
    x, y = map(int, read().split())
    customers_x.append(x)
    customers_y.append(y)

customers_x.sort()
customers_y.sort()

middle_index = n // 2
middle_x, middle_y = customers_x[middle_index], customers_y[middle_index]

distance_sum = 0
for index in range(n):
    distance_sum += abs(customers_x[index] - middle_x) + \
        abs(customers_y[index] - middle_y)

print(distance_sum)
