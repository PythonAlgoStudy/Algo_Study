import sys
from typing import List, Tuple

def get_input() -> List[int]:
    input = lambda: sys.stdin.readline().rstrip()
    _ = input()
    arr = list(map(int, input().split()))

    return arr

# Approach 1. Divide and Conquer O(N^2)
def findAproxZero1(arr: List[int]) -> Tuple[int, int]:
    sys.setrecursionlimit(10**4)

    def binary_search(l: int, r: int) -> Tuple[Tuple[int, int], int]:
        if r - l <= 1:
            return (-1, -1), float('inf')
        if r - l == 2:
            return (l, r-1), abs(arr[l] + arr[r-1])
        
        m = l + (r - l) // 2

        # Find the minimum pair from the left array
        left_pair, left_abs_diff = binary_search(l, m)
        if left_abs_diff == 0:
            return left_pair, left_abs_diff
        
        # Find the minimum pair from the right array
        right_pair, right_abs_diff = binary_search(m, r)
        if right_abs_diff == 0:
            return right_pair, right_abs_diff
        
        min_diff = min(left_abs_diff, right_abs_diff)
        min_pair = None

        # Find the minimum pair from the entire array
        for i in range(l, m):
            for j in range(m, r):
                diff = abs(arr[i] + arr[j])
                if min_diff > diff:
                    min_diff = diff
                    min_pair = (i, j)

        if min_pair is None:
            if left_abs_diff < right_abs_diff:
                return left_pair, left_abs_diff
            else:
                return right_pair, right_abs_diff

        return min_pair, min_diff
    
    pair, _ = binary_search(0, len(arr))
    a, b = arr[pair[0]], arr[pair[1]]
    if a > b:
        a, b = b, a
    return a, b

# Approach 2. Divide and Conquer O(NlgN)
def findAproxZero2(arr: List[int]) -> Tuple[int, int]:
    sys.setrecursionlimit(10**4)

    # Sort the array
    arr.sort()

    def binary_search(l: int, r: int) -> Tuple[Tuple[int, int], int]:
        if r - l <= 1:
            return (-1, -1), float('inf')
        if r - l == 2:
            return (l, r-1), abs(arr[l] + arr[r-1])
        
        m = l + (r - l) // 2

        # Find the minimum pair from the left array
        left_pair, left_abs_diff = binary_search(l, m)
        if left_abs_diff == 0:
            return left_pair, left_abs_diff
        
        # Find the minimum pair from the right array
        right_pair, right_abs_diff = binary_search(m, r)
        if right_abs_diff == 0:
            return right_pair, right_abs_diff
        
        min_diff = min(left_abs_diff, right_abs_diff)
        min_pair = None

        # Find the minimum pair from the entire sorted array
        i, j = l, r - 1
        while i < j:
            s = arr[i] + arr[j]
            diff = abs(s)
            if min_diff > diff:
                min_diff = diff
                min_pair = (i, j)
            if s > 0:
                j -= 1
            elif s < 0:
                i += 1
            else:
                break

        if min_pair is None:
            if left_abs_diff < right_abs_diff:
                return left_pair, left_abs_diff
            else:
                return right_pair, right_abs_diff

        return min_pair, min_diff
    
    pair, _ = binary_search(0, len(arr))
    a, b = arr[pair[0]], arr[pair[1]]
    if a > b:
        a, b = b, a
    return a, b

# Approach 3. Two Pointer O(NlgN)
def findAproxZero3(arr: List[int]) -> Tuple[int, int]:
    # Sort the array
    arr.sort()

    i, j = 0, len(arr) - 1
    min_abs = max(abs(arr[0] + arr[1]), abs(arr[-1] + arr[-2]))
    result = (i, j)
    while i < j:
        s = arr[i] + arr[j]
        abs_s = abs(s)
        
        # Every time the minimum absoulte value is found,
        # validate the result index tuple
        if min_abs > abs_s:
            min_abs = abs_s
            result = (i, j)
        if s > 0:
            j -= 1
        else:
            i += 1
    
    return arr[result[0]], arr[result[1]]

print(*findAproxZero3(get_input()))