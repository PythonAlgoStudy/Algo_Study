import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solution(N: int, M: int, S: str) -> int:
    answer, idx = 0, 0  # type: (int, int)
    while idx < M - 2:
        if S[idx] == "I":
            cnt = 0
            while idx < M and S[idx + 1 : idx + 3] == "OI":
                idx += 2
                cnt += 1
                if cnt >= N:
                    answer += 1
        idx += 1
    return answer


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    S = input()
    answer = solution(N, M, S)
    print(answer)
