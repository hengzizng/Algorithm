import sys
read = sys.stdin.readline


def convert(word):
    if word == S:
        result[0] = 1
        return

    if len(word) <= len(S) or result[0] == 1:
        return

    if word[-1] == 'A':
        convert(word[:-1])
    if word[0] == 'B':
        convert(word[:0:-1])


result = [0]
S = read().strip()
T = read().strip()

convert(T)

print(*result)
