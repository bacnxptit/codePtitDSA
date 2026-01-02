n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if swapped:
        print(f'Buoc {i + 1}: {" ".join(map(str, arr))}')
    else:
        break
