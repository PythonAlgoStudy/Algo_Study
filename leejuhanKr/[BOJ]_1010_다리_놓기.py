from sys import stdin


def memoization(func):
    _dict = {}

    def inner(*args):
        if args not in _dict:
            _dict[args] = func(*args)
        return _dict[args]

    return inner


@memoization
def f(l, r):
    # if l > r:
    #     raise ValueError
    if l == 1:
        return r

    return sum(f(l - 1, i) for i in range(l - 1, r))


if __name__ == "__main__":
    for _ in range(int(stdin.readline())):
        l, r = map(int, stdin.readline().split())
        print(f(l, r))
