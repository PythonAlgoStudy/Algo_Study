# https://www.acmicpc.net/problem/1202
import sys
import heapq
input = sys.stdin.readline
n,k = map(int, input().split())

jewels=[]
# 차례로 주얼리를 내림차순으로 정렬한다.
for _ in range(n):
    heapq.heappush(jewels, list(map(int,input().split())))

# 백팩은 백팩의 최대 무게 기준으로 오름차순 정렬
backpacks = []
for _ in range(k):
    backpacks.append(int(input()))
backpacks = sorted(backpacks)

ans = 0 
possible = []
# 백팩요소중 jewls 와 가방 요소가 jewles의 
for backpack in backpacks :
    while jewels and backpack >= jewels[0][0]:
        heapq.heappush(possible,-heapq.heappop(jewels)[1])
        #possible을 넣는다
    if possible:
        ans -=heapq.heappop(possible)
print(ans)
