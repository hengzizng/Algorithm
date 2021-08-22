# 58,620 kb
# 메모리
# 168 ms
# 실행시간
# 594
# 코드길이

import sys
sys.stdin = open("SWExpertAcademy/1228input.txt")

for tc in range(1, 10 + 1):
    N = int(input()) # 원본 암호문의 길이
    nums = list(input().split(" "))[:10]
    input() # 명령어의 개수
    commands = list(input().split(" "))
    i = 0
    while i < len(commands) - 1:
        i += 3
        place = int(commands[i - 2]) # 삽입할 위치
        count = int(commands[i - 1]) # 삽입할 숫자의 개수
        if place > 10:
            i += count
            continue
        part = commands[i : i + count]
        i += count

        nums = nums[:place] + part + nums[place:]
        nums = nums[:10]
    print("#" + str(tc) + " " + ' '.join(nums))

