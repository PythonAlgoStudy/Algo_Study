from collections import defaultdict

N = int(input())
input_history, info, cum_info = [], defaultdict(list), defaultdict(list)
for i in range(N):
    color, size = map(int, input().split())
    input_history.append((color, size))
    info[color].append(size)

for key in info.keys():
    info[key].sort()  # defaultdict(<class 'list'>, {1: [3, 10], 3: [15], 4: [8]})


def timeout_solution(input_history):
    for history in input_history:
        cnt = 0
        history_color, history_size = history

        for key in info.keys():
            if key == history_color:
                continue
            cnt += sum([i if i < history_size else 0 for i in info[key]])
        return cnt


cnt = timeout_solution(input_history)
print(cnt)
