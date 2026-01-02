def solution(arr):
    l = len(arr)
    if l == 1 :
        return f"[{arr[0]}]"
    new_arr = [arr[i]+arr[i+1] for  i in range(l-1)]
    current_row = "[" + " ".join(map(str, arr)) + "]"
    return current_row + "\n" + solution(new_arr)
t = int(input())
for _ in range(t):
    n = int(input())
    arr  = list(map(int,input().split()))
    print(solution(arr))

