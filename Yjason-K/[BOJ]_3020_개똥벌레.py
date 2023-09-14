# 3020 / 누적합, 이분탐색

import sys
input = sys.stdin.readline

def count_obstacles():
    stalagmites = [0] * (H + 1)  # 석순
    stalactites = [0] * (H + 1)  # 종유석

    for i in range(N):
        if i % 2 == 0:
            stalagmites[int(input())] += 1  # 석순
        else:
            stalactites[H - int(input()) + 1] += 1  # 종유석

    # 각 높이별 장애물의 개수를 누적하여 저장
    for i in range(H-1, 0, -1):
        stalagmites[i] += stalagmites[i+1]
    for j in range(2, H+1):
        stalactites[j] += stalactites[j-1]

    # 각 높이별로 석순과 종유석에 부딪히는 장애물의 총 개수 계산
    total = [0] * (H+1)
    for k in range(1, H+1):
        total[k] = stalagmites[k] + stalactites[k]

    res = total[1:] # 0번 인덱스는 0이기 떄문에 제외
    v = min(res) # 최소 장애물 개수 계산
    
    return v, res.count(v) # 최소 장애물 갯수, 그 구간의 갯수

N, H = map(int, input().split()) # 길이 N, 높이 H인 동굴
min_obs, counts = count_obstacles()
print(min_obs, counts)