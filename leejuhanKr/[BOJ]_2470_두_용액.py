from sys import stdin


def solution(M, arr: list):
    arr.sort()

    l_iter = iter(arr)
    r_iter = reversed(arr)

    l = next(l_iter)
    r = next(r_iter)
    cnt = len(arr) - 2

    tmp = r + l
    res = tmp
    ans = l, r

    while cnt > 0:
        if tmp > 0:
            r = next(r_iter)
        else:
            l = next(l_iter)
        cnt -= 1

        tmp = l + r
        if abs(tmp) < abs(res):
            res = tmp
            ans = l, r
    return ans


if __name__ == "__main__":
    M = int(stdin.readline())
    arr = [*map(int, stdin.readline().split())]

    answer = solution(M, arr)

    print(*answer)
