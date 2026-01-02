def bubbleSort(n,arr):


    steps = []

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

        steps.append(list(arr))

    for i in range(len(steps) - 1, -1, -1):
        step_num = i + 1
        print(f"Buoc {step_num}: ", end="")
        print(' '.join(map(str, steps[i])))


t = int(input())
for _ in range(t):
    k =int(input())
    arr = list(map(int,input().split()))
    bubbleSort(k,arr)