stairs_count = int(input())
stairs = [0]
for _ in range(stairs_count):
    stairs.append(int(input()))

# d: [[현재 계단을 연속해서 밟음, 현재 계단을 첫 번째로 밟음, 현재 계단을 밟지 않음], ...]
d = [[0] * 3 for _ in range(stairs_count + 1)]
d[1] = [stairs[1], stairs[1], stairs[0]]
if stairs_count > 1:
    d[2] = [stairs[1] + stairs[2], stairs[2], stairs[0] + stairs[1]]
    
for i in range(3, stairs_count + 1):
    d[i][0] = d[i - 1][1] + stairs[i]
    d[i][1] = max(d[i - 2][:2]) + stairs[i]
    d[i][2] = max(d[i - 1][:2])

print(max(d[-1][:2]))