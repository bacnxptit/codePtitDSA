def solution(arr):
    if len(arr) == 1:
        return ["[" + str(arr[0]) + "]"]
    next_arr = [arr[i] + arr[i+1] for i in range(len(arr)-1)]
    current = "[" + " ".join(map(str, arr)) + "]"
    return solution(next_arr) + [current]

t = int(input())
for _ in range(t):
    n = int(input())
    arr  = list(map(int,input().split()))
    print(" ".join(solution(arr)))

