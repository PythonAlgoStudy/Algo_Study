N, M = map(int, input().split())

lectures = list(map(int, input().split()))
avg: float = sum(lectures) / M


def search(start, M, max_value):
    if M == 0 and start == N:
        return max_value
    elif M == 0 and start != N:
        return 9999999
    if start >= N and M != 0:
        return 9999999
    idx = start
    sum, values = 0, []
    while True:
        if idx >= N:
            return 99999
        sum += lectures[idx]
        if sum > avg:
            values.append(search(idx, M - 1, max(sum - lectures[idx], max_value)))
            values.append(search(idx + 1, M - 1, max(sum, max_value)))
            break
        idx += 1
    return min(values)

print(search(0, M, 0))
