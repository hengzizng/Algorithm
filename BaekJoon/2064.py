import sys
read = sys.stdin.readline


# <설명>
# IP 네트워크 <= 네트워크 주소 , 네트워크 마스크
#
# IP 네트워크 : 32-m자리 (0 or 1) 가 네트워크 주소와 일치하는 모든 IP 포함
# 네트워크 주소 : 32-m자리 (0 or 1) | m자리 (0)
# 네트워크 마스크 : 32-m자리 (1) | m자리 (0)

# <출력>
# 네트워크 주소
# 네트워크 마스크


# 같은 비트 중 가장 오른쪽의 위치를 반환
# m: 바이트 인덱스 (0 ~ 3)
def get_bit_pos(m):
    for bit_pos in range(7, 0 - 1, -1):
        bit = 1 << bit_pos
        for ip_no in range(n - 1):
            # 다른 비트를 발견했다면
            if ip_addresses[ip_no][m] & bit != ip_addresses[ip_no + 1][m] & bit:
                return bit_pos + 1

    # 이번 바이트의 비트가 모두 같다
    return 0


def get_network_mask(last_bit_pos):
    network_mask = 0

    for bit_pos in range(7, last_bit_pos - 1, -1):
        network_mask |= 1 << bit_pos

    return network_mask


n = int(read())  # IP 주소 개수
ip_addresses = [list(map(int, read().split("."))) for _ in range(n)]  # IP 주소들

network_address = ip_addresses[0]  # 네트워크 주소
network_mask = [0] * 4  # 네트워크 마스크

for m in range(4):  # 각 바이트별로 확인
    bit_pos = get_bit_pos(m)  # 이번 바이트에서 마지막으로 같은 비트 자리

    if bit_pos == 0:  # 모든 비트가 같다면
        network_mask[m] = 255
    else:  # 다른 비트를 찾았다면
        network_mask[m] = get_network_mask(bit_pos)
        for i in range(m, 4):
            network_address[i] &= network_mask[i]
        break

print('.'.join(map(str, network_address)))
print('.'.join(map(str, network_mask)))
