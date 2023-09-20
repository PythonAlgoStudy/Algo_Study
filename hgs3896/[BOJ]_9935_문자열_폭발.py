# 18분
import sys
s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
S = []
for c in s:
    S.append(c)
    if len(S) >= len(p) and S[-1] == p[-1]:
        is_bomb = True
        for i, pc in enumerate(reversed(p), 1):
            if S[-i] != pc:
                is_bomb = False
                break
        if is_bomb:
            for _ in range(len(p)):
                S.pop()
print(''.join(S) if S else "FRULA")