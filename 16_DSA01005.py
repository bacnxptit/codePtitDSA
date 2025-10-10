n = int(input("Nhập n: "))

def inKQ():
    print("".join(str(x[i]) for i in range(1, t + 1)), end=" ")

def Try(i):
    for j in range(1,t+1):
        if chuaxet[j]:
            x[i] = j
            chuaxet[j] = False

            if i == t:
                inKQ()
            else:
                Try(i + 1)

            chuaxet[j] = True  # backtrack

for _ in range(n):
    t = int(input())
    chuaxet = [True] * (t + 1)
    x = [0] * (t + 1)
    Try(1)
    print()  
