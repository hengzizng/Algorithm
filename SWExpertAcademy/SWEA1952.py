def set_ticket(month, fee):
    if fee > min_fee[0]:
        return

    if month >= 12:
        min_fee[0] = fee
        return

    # 이용 계획이 0이라면 이용권 구매하지 않을 수도 있음
    if plan[month] == 0:
        set_ticket(month + 1, fee)
    # 1일 이용권
    set_ticket(month + 1, fee + fees[0] * plan[month])
    # 1달 이용권
    set_ticket(month + 1, fee + fees[1])
    # 3달 이용권
    set_ticket(month + 3, fee + fees[2])


T = int(input())
for t in range(1, T + 1):
    fees = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_fee = [fees[3]]

    set_ticket(0, 0)

    print("#", end="")
    print(t, end=" ")
    print(min_fee[0])
