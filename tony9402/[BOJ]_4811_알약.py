import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


DP = [[0 for j in range(32)] for i in range(32)]


def init():
    for j in range(31):
        DP[0][j] = 1
    for i in range(1, 31):
        DP[i][0] = DP[i - 1][1]
        for j in range(1, 31):
            DP[i][j] = DP[i - 1][j + 1] + DP[i][j - 1]


def solution(N):
    if DP[0][0] == 0:
        init()
    return DP[N - 1][1]


if __name__ == "__main__":
    inputs = open(0).readlines()[:-1]
    for N in map(int, inputs):
        print(solution(N))
