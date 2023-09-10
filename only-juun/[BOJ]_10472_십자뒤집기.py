import sys

# 3x3 판에서 각 위치를 눌렀을 때 변하는 위치들
change = [
    [0, 1, 3], [0, 1, 2, 4], [1, 2, 5],
    [0, 3, 4, 6], [1, 3, 4, 5, 7], [2, 4, 5, 8],
    [3, 6, 7], [4, 6, 7, 8], [5, 7, 8]
]

# 현재 상태에서 pos 위치를 누르면 어떻게 변하는지
def press(curr, pos):
    for i in change[pos]:
        curr[i] = 1 - curr[i]  # 0은 1로, 1은 0으로 바꿔줌

# 누를 수 있는 모든 경우의 수 확인
def solve(start):
    ans = sys.maxsize  # 최대 값으로 초기화
    for k in range(512):  # 2^9 == 512 모든 경우의 수
        cnt = 0
        curr = start.copy()  # 시작 상태 복사
        for i in range(9):
            if (k >> i) & 1:  # i번째 위치를 누르는 경우
                press(curr, i)
                cnt += 1
        if sum(curr) == 0:  # 모든 버튼이 흰색인 경우
            ans = min(ans, cnt)
    return ans

T = int(input())
for _ in range(T):
    start = []
    for _ in range(3):
        start.extend(list(map(int, input().strip().replace('*', '1').replace('.', '0'))))
    print(solve(start))
