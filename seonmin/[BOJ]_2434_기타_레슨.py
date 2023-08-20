n, m = map(int,input().split())
lecture = list(map(int,input().split()))

start = max(lecture)
end = 1000000

while start <= end:
    
    mid = (start+end)//2
    
    sum = 0
    count = 0
    

    for i in lecture:
        if(sum+i>mid):
            count += 1
            sum = 0 
        sum += i
    
    if(sum != 0):
        count += 1
    
    if(count <= m):
        end = mid -1
    else:
        start = mid +1
    
print(start)    
