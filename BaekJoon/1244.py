def change_multiple(switches, num):
    for i in range(num, len(switches) + 1, num):
        switches[i - 1] = '1' if switches[i - 1] == '0' else '0'


def change_near(switches, num):
    left, right = num - 1, num - 1

    while left >= 0 and right < len(switches):
        if switches[left] == switches[right]:
            switches[left] = '1' if switches[left] == '0' else '0'
            switches[right] = switches[left]
        else:
            break

        left -= 1
        right += 1


switch_count = int(input())
switches = list(input().split())
student_count = int(input())
for i in range(student_count):
    gender, num = map(int, input().split())

    if gender == 1:
        change_multiple(switches, num)
    else:
        change_near(switches, num)

for i in range(switch_count):
    if (i != 0 and i % 20 == 0):
        print()
    print(switches[i], end=" ")
