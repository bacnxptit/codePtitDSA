def solve(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != b[j]:
                break
    return i
print(solve([1,2,3],[1,2,3,5,6]))