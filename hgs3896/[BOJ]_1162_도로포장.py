#풀이시간: 4시간
import sys
from heapq import heappush, heappop
from collections import defaultdict
INF = sys.maxsize

def read_input():
    read_line = lambda: sys.stdin.readline().rstrip()
    N, M, K = map(int, read_line().split())
    roads = defaultdict(dict)
    for _ in range(M):
        a, b, c = map(int, read_line().split())
        roads[a][b] = roads[b][a] = min(roads[a].get(b, INF), c)
    return N, K, roads

def solve(N, K, roads):
    min_dists = defaultdict(lambda: [INF] * (K+1))
    min_dists[1] = [0] * (K+1)

    min_heap = [(min_dists[1][K], K, 1)]
    while min_heap:
        d, k, v = heappop(min_heap)

        if min_dists[v][k] < d:
            continue

        for w in roads[v]:
            if k > 0:
                if min_dists[w][k-1] > d:
                    min_dists[w][k-1] = d
                    heappush(min_heap, (min_dists[w][k-1], k-1, w))

            if min_dists[w][k] > d + roads[v][w]:
                min_dists[w][k] = d + roads[v][w]
                heappush(min_heap, (min_dists[w][k], k, w))

    return min(min_dists[N])

print(solve(*read_input()))