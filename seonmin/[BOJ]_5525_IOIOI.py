n = int(input())
m = int(input())
s = input()

words = 'IO'*n+'I'
answer = 0

for i in range(m-(n*2)):
    if(s[i:i+(n*2+1)] == words):
        answer+=1
        
print(answer)