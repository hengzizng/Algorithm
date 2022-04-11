# 90 min
# 단면의 모든 열에 대해 동일한 특성의 셀들이 K개 이상 연속으로 존재해야만 한다.
# 특정 행을 하나의 특성으로 통일시키는 약을 사용
# 약의 최소 투입 횟수
import sys
sys.stdin = open("TestCase/SWExpertAcademy/2112input.txt")


# 모든 열이 성능 검사를 통과할 수 있는지 확인
def check(film):
    for c in range(W):  # 모든 열 확인
        max_same_len, same_start_r, r = 1, 0, 1
        while r < D:  # 위에서부터 확인
            if film[same_start_r][c] != film[r][c]:
                max_same_len = max(max_same_len, r - same_start_r)
                same_start_r = r
            r += 1
        max_same_len = max(max_same_len, r - same_start_r)
        # 하나의 열이라도 통과하지 못한다면
        if max_same_len < K:
            return False

    return True


# 약품을 투입할 행과 특성을 선택한다.
def select_rows(d, count, start, film):
    if count >= min_selected[0]:
        return

    if count == d:
        # 현재 상태로 성능 검사를 통과할 수 있다면
        if check(film):
            min_selected[0] = min(min_selected[0], count)

        return

    for r in range(start, D):
        origin_row = film[r]

        # 이번에 선택된 행을 모두 0으로 변경한다.
        fill_row(0, r, film)
        select_rows(d, count + 1, r + 1, film)
        # 이번에 선택된 행을 모두 1로 변경한다.
        fill_row(1, r, film)
        select_rows(d, count + 1, r + 1, film)

        film[r] = origin_row


# target_row 인덱스에 해당하는 film 배열의 행을 value로 채운다.
def fill_row(value, target_row, film):
    new_row = [value] * W
    film[target_row] = new_row


T = int(input())  # 테스트 케이스 개수
answers = []
for t in range(1, T + 1):
    # D: 두께(높이), W: 셀(가로), K: 보호필름 성능 합격기준
    D, W, K = map(int, input().split())
    # film: 보호 필름 단면 정보
    film = [list(map(int, input().split())) for _ in range(D)]

    # 약을 투입하지 않았을 때 성능검사 통과 여부 확인
    min_selected = [0]
    if not check(film):  # 성능검사 통과하지 않았다면
        # 약 투입 횟수 1 ~ K-1 의 범위로 확인
        min_selected[0] = K
        for d in range(1, K):
            select_rows(d, 0, 0, film)
            # 성능검사 통과라면 바로 종료
            if min_selected[0] < K:
                break

    answers.append("#")
    answers.append(str(t))
    answers.append(" ")
    answers.append(str(min_selected[0]))
    answers.append("\n")

print("".join(answers))
