import sys
sys.stdin = open("TestCase/BaekJoon/1927input.txt")
read = sys.stdin.readline


def push(val):
    # 원소를 가장 마지막에 삽입
    target = len(heap)
    heap.append(val)

    # 삽입한 원소가 부모 원소보다 커질때까지 이동
    while target > 0 and heap[target] < heap[target // 2]:
        heap[target], heap[target // 2] = heap[target // 2], heap[target]
        target = target // 2


def pop():
    if len(heap) == 1:
        return 0

    # 가장 마지막 원소를 루트로 이동
    heap[1], heap[-1] = heap[-1], heap[1]
    # 가장 작은 값 삭제
    val = heap.pop()

    # 이동한 원소가 자식 원소보다 작아질때까지 이동
    target = 1
    while target < len(heap):
        # 왼쪽 자식 인덱스, 오른쪽 자식 인덱스
        left, right = target * 2, target * 2 + 1

        # 자식이 없을 경우
        if len(heap) <= left:
            break
        # 왼쪽 자식만 있을 경우
        elif len(heap) <= right:
            # 왼쪽 자식 원소보다 크면
            if heap[target] > heap[left]:
                heap[target], heap[left] = heap[left], heap[target]
                target = left
            else:
                break
        # 왼쪽, 오른쪽 둘 다 자식이 있을 경우
        else:
            # 더 작은 자식 원소가 없으면
            if heap[target] < heap[left] and heap[target] < heap[right]:
                break
            # 왼쪽 자식 원소가 더 작으면
            elif heap[left] < heap[right]:
                heap[target], heap[left] = heap[left], heap[target]
                target = left
            # 오른쪽 자식 원소가 더 작으면
            else:
                heap[target], heap[right] = heap[right], heap[target]
                target = right

    return val


heap = [0]
N = int(read())  # 연산의 개수
for _ in range(N):
    x = int(read())  # 연산 정보
    if x == 0:
        print(pop())
    else:
        push(x)
