from sys import stdin


def memoization(func):
    _dict = {}

    def memoized(*args):
        if args not in _dict:
            _dict[args] = func(*args)
        return _dict[args]

    return memoized


@memoization
def g(w, h):
    """
    w개의 W, h개의 H로 이루어진 문자열의 개수를 반환
    단, w >= h
    """
    if h > w:
        return 0
    if h == 0:
        return 1
    return g(w - 1, h) + g(w, h - 1)


def solution(n):
    return g(n, n)


if __name__ == "__main__":
    while N := int(stdin.readline()):
        print(solution(N))
