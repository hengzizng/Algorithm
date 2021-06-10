N = int(input())

if N < 3:
    print(1)
else:
    d = [0] * (N + 1)
    d[1] = 1
    d[2] = 1

    for i in range(3, N + 1):
        d[i] = d[i - 1] + d[i - 2]
    
    print(d[N])