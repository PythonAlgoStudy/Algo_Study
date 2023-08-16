n = int(input())
list = []
for i in range(n):
    tempX,tempY = map(int,input().split())
    list.append((tempX,tempY))
    
list.sort(key=lambda x : (x[1],x[0]))

count = 0

startT = 0
endT=0
i = 0

while i<n:
    if(endT<=list[i][0]):
        count += 1
        startT,endT= list[i][0],list[i][1]
    i +=1    
    
print(count)