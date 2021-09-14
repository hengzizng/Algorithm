# Level 1 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    def get_rank(count):
        if count == 6:
            return 1
        elif count == 5:
            return 2
        elif count == 4:
            return 3
        elif count == 3:
            return 4
        elif count == 2:
            return 5
        else:
            return 6


    # 0을 제외한 나머지 숫자들 중에서 몇 개를 맞췄는지 확인
    win_nums = set(win_nums)
    lotto_count, zero_count = 0, 0
    for lotto in lottos:
        if lotto == 0:
            zero_count += 1
        elif lotto in win_nums:
            lotto_count += 1

    return [get_rank(lotto_count + zero_count), get_rank(lotto_count)]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))