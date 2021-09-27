import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    
    mix_count = 0 # 섞인 횟수
    min1 = heapq.heappop(scoville) # 가장 맵지 않은 음식의 스코빌 지수
    while min1 < K: # 최소 스코빌이 K보다 작은동안 반복
        mix_count += 1 # 섞인 횟수 증가
        min2 = heapq.heappop(scoville) # 두 번째로 맵지 않은 음식의 스코빌 지수

        mix = min1 + (min2 * 2) # 섞인 음식의 스코빌 지수
        heapq.heappush(scoville, mix)

        min1 = heapq.heappop(scoville)

        if len(scoville) == 0: # 음식이 남아있지 않으면 종료
            break

    return -1 if min1 < K else mix_count


# print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 1], 1))