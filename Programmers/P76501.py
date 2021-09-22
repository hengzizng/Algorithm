def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        total += absolutes[i] * (1 if signs[i] else -1)

    return total


absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes, signs), 9)