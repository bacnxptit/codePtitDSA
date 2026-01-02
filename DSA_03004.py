def sol(arr):
    arr.sort()
    num1,num2 = "",""
    for i in range(len(arr)):
        if i % 2 == 0 :
            num1 += str(arr[i])
        else:
            num2 += str(arr[i])
    return int(num1)+int(num2)
t =int(input())
for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr))