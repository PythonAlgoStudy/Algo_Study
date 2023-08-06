from collections import deque
import sys


def bfs(arr, start):
    visited = [start]  # 방문 배열 초기화
    friends = [0] * (N + 1)  # 친구들 마다 베이컨
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()
        for friend in arr[cur]:
            if friend not in visited:
                friends[friend] = friends[cur] + 1
                visited.append(friend)
                q.append(friend)
    return sum(friends) # i의 베이컨 합


input = sys.stdin.readline
N, M = map(int, input().split())  # 유저의 수 N, 친구 관계의 수 M
arr = [[] for _ in range(N + 1)]  # 1번부터 N까지 유저 목록

for _ in range(M):  # 관계수 만큼 추가
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

answer = []
for i in range(1, N + 1):
    answer.append(bfs(arr, i))

print(answer.index(min(answer)) + 1)
