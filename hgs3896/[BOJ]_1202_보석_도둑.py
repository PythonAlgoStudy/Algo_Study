import sys
from heapq import heappush, heappop
from bisect import bisect_right

input_ = sys.stdin.readline

def get_input():
    # 보석 갯수, 가방 갯수 입력
    N, K = map(int, input_().split(' '))
    # 보석 무게 입력
    jewels = [tuple(map(int, input_().split(' '))) for _ in range(N)]
    # 가방 최대 중량 입력
    bags = [int(input_()) for _ in range(K)]

    return jewels, bags

def preprocess(jewels, bags):
    # 무게의 오름차순으로 정렬
    jewels.sort(key=lambda jewel: jewel[0])
    # 가방 최대 중량의 오름차순으로 정렬
    bags.sort()

def maxValue(jewels, bags):
    answer = 0
    pidx = 0
    available = []
    for bag in bags:
        # 가방 최대 중량보다 많은 무게의 보석의 인덱스 이진 탐색
        idx = bisect_right(jewels, bag, key=lambda jewel: jewel[0])
        # 이전까지 탐색한 인덱스(pidx)에서
        # 현재 탐색한 인덱스(idx) 전까지 보석의 가치를
        # 힙에 추가하여 최대 힙 구성
        for value in jewels[pidx:idx]:
            heappush(available, -value)
        # 이전 인덱스 갱신
        pidx = idx
        # 힙이 비어있지 않다면 힙에서 가장 큰 가치를 갖는 보석에 대한 가치를 정답에 누적
        if available:
            answer += -heappop(available)

    return answer

jewels, bags = get_input()
preprocess(jewels, bags)
print(maxValue(jewels, bags))