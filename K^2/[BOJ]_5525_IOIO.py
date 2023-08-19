#https://www.acmicpc.net/problem/5525
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    string = input()
    index =1
    ans =0
    pattern  = 0
    while index < m-1 :
        if string[index -1] == 'I' and string[index] == 'O' and string[index+1]=='I':
            pattern +=1
            if pattern == n:
                ans  +=1
                pattern -=1
            index +=1
        else:
            pattern = 0
        index +=1
    print(ans)