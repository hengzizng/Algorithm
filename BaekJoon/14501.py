import sys
read = sys.stdin.readline


def set_max_price(today, price):
    for index in range(today, N):  # 오늘부터 N-1 일까지
        next_day = index + TnP[index][0]  # 이번 상담을 했을 때 완료 날짜
        if next_day <= N:  # 이번 상담의 완료 날짜가 퇴사 전이면
            new_price = price + TnP[index][1]
            max_price[0] = max(max_price[0], new_price)
            set_max_price(next_day, new_price)


N = int(read())  # 퇴사까지 남은 일 수
TnP = [list(map(int, read().split())) for _ in range(N)]  # [일 수, 금액]
max_price = [0]

set_max_price(0, 0)
print(*max_price)
