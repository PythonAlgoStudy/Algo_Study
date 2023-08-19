N = int(input())
M = int(input())
S = input()

def count_pattern():
    # Time Complexity: O(M)
    # Space Complexity: O(1)
    
    ans = 0
    
    # I(OI)+ 패턴이 마지막으로 발견된 (위치, 패턴의 반복 횟수)
    last_found_pat_info = (-3, -1)
    for idx, c in enumerate(S):
        if c == 'I':
            if idx-2 == last_found_pat_info[0] and S[idx - 1] == 'O':
                # 직전에 패턴이 존재한 경우
                last_found_pat_info = (idx, last_found_pat_info[1] + 1)
                # 패턴의 반복횟수가 N이상이면 idx번째 문자를 마지막 문자로하는 2*N+1 크기 패턴이 존재함
                if last_found_pat_info[1] >= N:
                    ans += 1
            else:
                # 그렇지 않은 경우
                last_found_pat_info = (idx, 0)
    return ans

print(count_pattern())