import sys
read = sys.stdin.readline


N, K = map(int, read().split())
numbers = list(range(1, N + 1))

k = 0
permutation = []
while numbers:
    k = (k + K - 1) % len(numbers)
    permutation.append(str(numbers.pop(k)))
    
print("<" + ", ".join(permutation) + ">")