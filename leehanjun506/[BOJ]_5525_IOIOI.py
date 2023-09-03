# n+1 개의 i와 n개의 o 로 이루어짐
# Pn은 i o 가 교대로 나오는 문자열 
n = int(input())
m = int(input())
s = input()
# s의 길이는 m
answer = 0
pattern = 0
index = 0
while index < m-2:
    if s[index:index+3] == 'IOI':
        pattern+=1
        index+=2
        if pattern == n:
            answer+=1
            pattern-=1
    else:
        index+=1
        pattern = 0

print(answer)