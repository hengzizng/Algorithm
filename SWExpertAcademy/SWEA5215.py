# 63,860 kb
# 메모리
# 630 ms
# 실행시간
# 869
# 코드길이

import sys
sys.stdin = open("TestCase/SWExpertAcademy/5215input.txt")


def combination(count, score, calorie):
    if calorie > L:
        return

    if count == N:
        max_scores[tc] = max(max_scores[tc], score)
        return
    
    isSelected[count] = True
    combination(count + 1, score + ingredients[count][0], calorie + ingredients[count][1])
    isSelected[count] = False
    combination(count + 1, score, calorie)


T = int(input()) # 테스트케이스 수
max_scores = [0] * T # 최대 맛의 점수
for tc in range(T):
    N, L = map(int, input().split(" ")) # 재료의 수, 제한 칼로리

    ingredients = [] # 음식 재료들
    for n in range(N):
        T, K = map(int, input().split()) # 맛의 점수, 칼로리
        ingredients.append([T, K]) # 점수는 높고, 칼로리는 낮아야 한다.
    isSelected = [False] * N
    combination(0, 0, 0)

for tc, max_score in enumerate(max_scores, 1):
    print("#" + str(tc) + " " + str(max_score))

