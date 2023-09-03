from functools import cache

@cache
def f(one, half):
    if one == 0:
        if half == 0:
            return 1
        return f(one, half - 1)
    else:
        if half == 0:
            return f(one - 1, half + 1)
        return f(one - 1, half + 1) + f(one, half - 1)

while True:
    n = int(input())
    if n == 0:
        break
    print(f(n, 0))