def solution(n):
    answer = ''

    while n > 0:
        n -= 1
        answer = "124"[n % 3] + answer
        n //= 3

    return answer


print("1 ->", solution(1), 1)
print("2 ->", solution(2), 2)
print("3 ->", solution(3), 4)
print("4 ->", solution(4), 11)
print("5 ->", solution(5), 12)
print("6 ->", solution(6), 14)