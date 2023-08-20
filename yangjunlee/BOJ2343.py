import sys
input = sys.stdin.readline

N,M = map(int,input().split())

q = list(map(int,input().split()))


l = max(q)
r = sum(q)

while 1:

    m = (l+r)//2
    if l >= r:
        break
    count = 0
    tmp = m
    for i in q:
        if tmp < i:
            count += 1
            tmp = m
        tmp-=i

    if count >= M:
        l=m+1
    else:
        r=m

print(r)
