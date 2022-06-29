'''
# 풀이 1 > 문자열 사용
import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline


def change(string):
    if string == S:
        result[0] = 1
        return

    if result[0] == 1 or len(string) <= len(S):
        return

    if string[-1] == "A":
        change(string[:-1])
    else:
        change(string[:-1][::-1])


S = read().strip()
T = read().strip()

result = [0]
change(T)
print(result[0])
'''

# 풀이 2 > 리스트 사용
import sys
read = sys.stdin.readline


S = read().strip()
T = list(read().strip())

result = 0
while len(S) <= len(T):
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T.reverse()

    if ''.join(T) == S:
        result = 1
        break

print(result)
