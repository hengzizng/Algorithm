T = int(input())
answers = []

zero = [0] * 41
one = [0] * 41
zero[0] = 1
one[1] = 1
for _ in range(T):
    N = int(input())

    for i in range(2, N + 1):
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]
    
    answers.append([zero[N], one[N]])

for answer in answers:
    print(answer[0], answer[1])