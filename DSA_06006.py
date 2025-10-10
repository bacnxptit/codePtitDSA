def sapXep(arr):
    count_0 =count_1=count_2 = 0
    res = []
    for i in range(len(arr)):
        if arr[i] == 0 :
            count_0 += 1
        elif arr[i] == 1 :
            count_1 += 1
        else :
            count_2 +=1
    return [0] * arr.count(0) + [1] * arr.count(1) + [2] * arr.count(2)
t =int(input())
for _ in range(t):
    n =int(input())
    x = list(map(int,input().split()))
    print(" ".join(map(str,sapXep(x))))
