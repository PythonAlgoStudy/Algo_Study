
n, k = map(int,input().split())
juwel = []
bag = []
for i in range(n):
    m, v = map(int,input().split())
    juwel.append((m,v))

for j in range(k):
    c = int(input())
    bag.append(c)


juwel.sort(key= lambda x: -x[1])
bag.sort()

answer = 0
breaker = False

for i in range(n):
    if(breaker == True):
        break
    
    for j in range(k):
        temp = juwel[i][1]
        if(juwel[i][0] < bag[j]):
            del bag[j-1]
            answer += temp
            
        if(len(bag)==0):
            breaker = True
            break    

print(answer)