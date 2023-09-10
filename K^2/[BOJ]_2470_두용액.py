n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left =0
right = n-1

ans = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]

while left <right:
    left_v = arr[left]
    right_v = arr[right]
    
    sum = left_v + right_v

    if abs(sum) < ans:
        ans = abs(sum)
        final = [left_v,right_v]

        if ans == 0:
            break
        if sum <0:
            left +=1
        else:
            right -=1
print(final[0],final[1])
