import sys
sys.setrecursionlimit(10000000)

def find(maps):
    r, c=len(maps), len(maps[0])
    if max(max(maps))==0:
        return 0
    seen=set()
    def dfs(i,j):
        if (i<0 or j<0 or (i,j) in seen or i==r or j==c or maps[i][j]==0):
            return 0
        seen.add((i,j))
        return (maps[i][j]+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1))
    ans=0
    for i in range(r):
        for j in range(c):
            res=dfs(i,j)
            if res:
                ans+=1
    return ans

n=int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))


m = min(min(row) for row in maps)
M= max(max(row) for row in maps)
ans = []
for r in range(m,M+1):
    tmp = [[1 if x>=r else 0 for x in row] for row in maps]
    ans.append(find(tmp))
    
print(max(ans))
