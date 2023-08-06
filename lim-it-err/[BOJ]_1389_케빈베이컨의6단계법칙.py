from collections import defaultdict, deque

# FIXME : Dijestra method?

N, M = map(int, input().split())
relation = defaultdict(list)

for _ in range(M):
    src, dst = map(int, input().split())
    relation[src-1].append(dst-1)
    relation[dst-1].append(src-1)


def bacon(user):
    q = deque(relation[user])
    temp_q = deque()
    distance_user = [0 for _ in range(N)]
    distance = 1
    while True:
        while q:
            dst = q.pop()
            if distance_user[dst] > 0:
                continue
            distance_user[dst] = distance
            temp_q.extend(relation[dst])
        if all(distance_user):
            # print(distance_user)
            return sum(distance_user) + 1
        distance += 1
        q = temp_q
        temp_q = deque()

if __name__ == "__main__":
    result = []
    # For Every User
    for i in range(N):
        result.append((bacon(i), i))
    result.sort()
    print(result[0][1]+1)
