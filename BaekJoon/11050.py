def get_factorial(number):
    if factorial[number] == 0:
        factorial[number] = number * get_factorial(number - 1)
    
    return factorial[number]

N, K = map(int, input().split())

factorial = [0] * (N + 1)
factorial[0] = 1
factorial[1] = 1

print(get_factorial(N) // (get_factorial(K) * get_factorial(N - K)))
