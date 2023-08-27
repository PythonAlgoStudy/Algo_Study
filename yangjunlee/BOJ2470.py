N = int(input())
sol = list(map(int, input().split()))
sol.sort()
l, r = 0, N-1
ans = []
while r>l:
    s = sol[r] + sol[l]
    ans.append((abs(s), sol[l], sol[r]))
    if s > 0:
        r-=1
    elif s < 0:
        l+=1
    else:
        break
    
ans.sort()

s, a, b = ans[0]
print(a, b)
