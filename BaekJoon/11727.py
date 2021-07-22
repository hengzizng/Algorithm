n = int(input())

x, y = 1, 3
for i in range(3, n + 1):
    x, y = y, (2 * x + y) % 10007

if n == 1:
    print(x)
else:
    print(y)