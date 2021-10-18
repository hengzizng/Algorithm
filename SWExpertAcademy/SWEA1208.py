import sys
sys.stdin = open("TestCase/SWExpertAcademy/1208input.txt")

for tc in range(1, 10 + 1):
    dump = int(input())
    heights = [0] * 101
    low, high = 101, 0
    for height in list(map(int, input().split())):
        heights[height] += 1
        low = min(low, height)
        high = max(high, height)

    while dump > 0 and high > low:
        heights[high] -= 1
        heights[low] -= 1
        heights[high - 1] += 1
        heights[low + 1] += 1
        
        while heights[high] == 0:
            high -= 1
        while heights[low] == 0:
            low += 1
        dump -= 1

    print("#" + str(tc), high - low)

