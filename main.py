"""def sinhhoanvi(n,m):
    a = list(range(1,n+1))
    while True :
        if a[0] == m :
            print(' '.join(str(x) for x in a ))
        i = n- 2
        while i >= 0 and a[i]> a[i+1]:
            i-= 1
        if i < 0 :
            break
        j = n- 1
        while a[j] < a[i]:
            j-= 1
        a[i],a[j] = a[j],a[i]
        a[i+1:]=reversed(a[i+1:])
n,m = map(int,input().split())
sinhhoanvi(n,m)
"""
import shlex

"""s = input().strip()

n = len(s)
mark = [''] * n
stack = []

# Bước 1: duyệt chuỗi
for i, ch in enumerate(s):
    if ch == '(':
        stack.append(i)   # lưu vị trí nếu thấy (
    elif ch == ')':
        if stack:
            open_pos = stack.pop()
            mark[open_pos] = '0'  # ( hợp lệ
            mark[i] = '1'         # ) hợp lệ
        else:
            mark[i] = '-1'        # ) sai vì không có ( tương ứng
# Bước 2: các ( còn lại trong stack là ngoặc sai
for pos in stack:
    mark[pos] = '-1'

# Bước 3: tạo output
res = []
for i in range(n):
    if s[i] not in "()":
        res.append(s[i])
    else:
        # các ngoặc chưa xử lý thì là ngoặc sai
        if mark[i] == '':
            mark[i] = '-1'
        res.append(mark[i])

print("".join(res))"""






""" sinh to hop co tong la mot so fibonaci
def fibonaci(max_sum):
    fib=[0,1]
    while fib[-1] <= max_sum:
        fib.append(fib[-1]+fib[-2])
    return set(fib)
def sol(n,k):
    max_sum = (k*(2*n-k+1))//2
    res=[]
    def sinhtohop():
        a = list(range(1,k+1))
        while True :
            if sum(a) in fibonaci(max_sum):
                res.append(a.copy())
            i = k-1
            while i >= 0 and a[i] == n-k+i+1:
                i-= 1
            if i < 0 :
                break
            a[i] += 1
            for j  in range(i+1,k):
                a[j] = a[j-1]+1

    sinhtohop()
    return res
print(sol(5,3))"""


"""def sinhhoanvi(n):
    a = list(range(1,n+1))
    while True :
        tong = 0
        for i in range(n-1):
            tong += a[i]-a[i+1]
        if tong > 0 :
            print(' '.join(str(x) for x in a))
        i = n -2
        while i >= 0 and a[i] > a[i+1]:
            i -= 1
        if i < 0 :
            break
        j = n- 1
        while a[j] < a[i]:
            j-= 1
        a[i],a[j] = a[j],a[i]
        a[i+1:] = reversed(a[i+1:])

a = int(input())
sinhhoanvi(a)
"""




"""n = int(input())
for _ in range(n):
    s= input().strip()
    stack = []
    res = []
    chiso = 0
    for i in s :
        if i == '(':
            chiso += 1
            stack.append(chiso)
            res.append(chiso)
        elif i == ')':
            so = stack.pop()
            res.append(so)
print(' '.join(str(x) for x in res))
"""



"""def sinhhoanvi(a):
    n = len(a)
    i = n -2
    while i >= 0 and a[i] > a[i+1]:
        i-= 1
    if i < 0 :
        return False
    j = n - 1
    while a[j] < a[i]:
        j-= 1
    a[j],a[i]=a[i],a[j]
    a[i+1:]=reversed(a[i+1:])
    return True
n = int(input())
danh_sach_ten = map(str,input().split())
ten_cuoi = input().strip()
ten_con_lai = []
for i in danh_sach_ten:
    if i != ten_cuoi :
        ten_con_lai.append(i)
ten_con_lai.sort()
while True :
    print(' '.join(ten_con_lai),ten_cuoi)
    if not sinhhoanvi(ten_con_lai):
        break"""


"""def sinh_day(a,n,k):
    path = []
    ketqua = set()
    def backTrack(start):
        if len(path) == k:
            s = ""
            for i in path:
                s+= str(i)
            ketqua.add(s)
            return
        for i in range(start,n):
            path.append(a[i])
            backTrack(i+1)
            path.pop()
    backTrack(0)
    for i in sorted(ketqua):
        print(i)
n,k = map(int,input().split())
a = list(map(int,input().split()))
sinh_day(a,n,k)"""

"""def tinh(s):
    for i in range(len(s)):
        if not s[i].isdigit():
            s1 = int(s[:i])
            s2 = int(s[i+1:])
            if s[i] == '+':
                return s1+s2
            elif s[i] == '-':
                return s1-s2
            else:
                return s1*s2
print(tinh('2*1'))
"""
"""def check(number,ds):
    res= []
    path = []
    def backTrack(start,sum):
        if sum == number :
            res.append(path[:])
            return
        if sum > number :
            return
        for i in range(start,len(ds)):
            # dung de loai bo phan tu trung
            if i > start and ds[i] == ds[i-1] :
                continue
            path.append(ds[i])
            backTrack(i+1,sum+ds[i])
            path.pop()
    backTrack(0,0)
    return res
ds = [1,1,2,1]
number = 3
res = check(number,ds)
for i in res :
    print(" ".join(map(str,i)))"""

"""
#Tinh gia tri bieu thuc tien to va hau to
n = int(input())
for _ in range(n):
    k = int(input())
    s =input().strip().split()
    stack = []
    if s[0].isdigit() :
        for i in s :
            if i.isdigit():
                stack.append(int(i))
            else:
                s1 = stack.pop()
                s2 = stack.pop()
                if i == '+':
                    stack.append(s1+s2)
                elif i == '-':
                    stack.append(s1-s2)
                elif i == '*':
                    stack.append(s1*s2)
                elif i == '/':
                    stack.append(s1//s2)
    else:
        for i in s[::-1]:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                s1 = stack.pop()
                s2 = stack.pop()
                if i == '+':
                    stack.append(s1 + s2)
                elif i == '-':
                    stack.append(s1 - s2)
                elif i == '*':
                    stack.append(s1 * s2)
                elif i == '/':
                    stack.append(s1 // s2)
    print(stack[0])
"""

"""# so phat loc 68
t = int(input())
for _ in range(t):
    n = int(input())
    res= []
    def backtrack(path):
        if 1<= len(path)<=n:
            res.append(int(''.join(map(str,path[:]))))
        if len(path) == n :
            return

        path.append('6')
        backtrack(path)
        path.pop()

        path.append('8')
        backtrack(path)
        path.pop()
    backtrack([])
    res.sort() # res.sort(reverse = True) neu yeu cau sap xep tu lon den nho
    for i in res :
        print(i,end=" ")
    print() # xuong dong testcase tiep theo"""
"""
# Xay cay nhi phan tim kiem roi duyet postorder
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def insert(root,val):
    if root is None :
        return Node(val)
    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root
def postorder(root,res):
    if root is None :
        return
    #res.append(root.val)
    postorder(root.left,res)
    postorder(root.right,res)
    res.append(root.val)
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    root = None
    for x in arr :
        root = insert(root,x)
    res = []
    postorder(root,res)
    print(*res)
"""

"""def sinhhoanvi(n):
    a = list(range(1, n + 1))
    res = []

    while True:
        # Lưu hoán vị dưới dạng xâu
        res.append("".join(str(x) for x in a))

        # ===== sinh hoán vị kế tiếp =====
        i = n - 2
        while i >= 0 and a[i] > a[i + 1]:
            i -= 1
        if i < 0:
            break

        j = n - 1
        while a[j] <= a[i]:
            j -= 1

        a[i], a[j] = a[j], a[i]
        a[i + 1:] = reversed(a[i + 1:])

    # Sắp xếp ngược (giảm dần)
    res.sort(reverse=True)

    # In kết quả
    print(*res)
sinhhoanvi(3)"""

"""def check(s):
    if '88' in s:
        return False
    if '6666' in s:
        return False
    return True

def sinhxau68(n):
    if n < 6:
        return

    a = ['6'] * n
    a[0] = '8'
    a[-1] = '6'

    def kiemTra():
        s = "".join(a)
        if check(s):
            print(s)

    kiemTra()

    while True:
        i = n - 2
        while i > 0 and a[i] == '8':
            i -= 1
        if i == 0:
            break

        a[i] = '8'
        for j in range(i + 1, n):
            a[j] = '6'

        kiemTra()
sinhxau68(6)"""

"""
sinh danh sach theo tam giac
def sol(a):
    l = len(a)
    if l == 1 :
        return f'[{a[0]}]'

    new_arr = [a[i]+a[i+1] for i in range(l-1)]
    ind = "[" + " ".join(map(str,a)) + "]"
    return ind + "\n" + sol(new_arr)
print(sol([1,2,3,4,5]))

"""
"""
def sol(n,k):
    res =[]
    def backtrack(path,start):
        if  len(path) == k   and path[-1] - path[0] > k :
            res.append("".join(map(str,path[:])))

        for i in range(start,n+1):
            path.append(i)
            backtrack(path,i+1)
            path.pop()
    backtrack([],1)
    print(res)
sol(6,4)"""


"""
sinh day con co tong nho hon k
def sol(arr,n,k):
    res = []
    def backtrack(start,path,sum):
        if sum >= k :
            return
        if path:
            res.append(path[:])
        for i in range(start,n):
            path.append(arr[i])
            backtrack(i+1,path,sum+arr[i])
            path.pop()
    backtrack(0,[],0)
    return res
print(sol([3,4,5],3,10))"""

"""n = int(input())
jobs = []

for _ in range(n):
    d, p = map(int, input().split())
    jobs.append((d, p))

# Sắp xếp theo lợi nhuận giảm dần
jobs.sort(key=lambda x: x[1], reverse=True)

max_deadline = max(job[0] for job in jobs)
slot = [False] * (max_deadline + 1)

total_profit = 0

for d, p in jobs:
    for t in range(min(d, max_deadline), 0, -1):
        if not slot[t]:
            slot[t] = True
            total_profit += p
            break

print(total_profit)"""

"""def sinhxaunhiphan(n):
    a = [0] * n
    while True :
        print(*a)
        i = n-1
        while i >= 0 and a[i] ==1 :
            i-= 1
        if i < 0 :
            break
        a[i] = 1
        for j in range (i+1,n) :
            a[j] = 0
sinhxaunhiphan(3)
"""
"""def sinhhoanvi(n,k):
    a =list(range(1,n+1))
    while True :
        if a[-1] == k :
            print(*a)
        i = n-2
        while i >=0 and a[i] >= a[i+1]:
            i-=1
        if i < 0 :
            break
        j = n-1
        while  a[i] > a[j]:
            j-= 1
        a[j],a[i] = a[i],a[j]
        a[i+1:] = reversed(a[i+1:])
sinhhoanvi(4,2)"""

"""def sinhtohop(n,k):
    a =list(range(1,k+1))
    while True :
        print(a)
        i = k-1
        while i >= 0 and a[i] == n-k+i+1:
            i-= 1
        if i < 0:
            break
        a[i]+= 1
        for j in range(i+1,k):
            a[j] = a[j-1]+1
sinhtohop(5,3)"""

"""def check(s):
    if '88' in s :
        return False
    if '6666' in s :
        return False
    return True
def sinhso68(n):
    if n < 6 :
        return
    a = ['6'] * n
    a[0] = '8'
    a[-1] = '6'
    def kiemtra():
        if check("".join(a)):
            print("".join(a))
    kiemtra()
    while True :
        i = n-2
        while i >= 0 and a[i] == '8':
            a[i] = '6'
            i-= 1
        if i == 0 :
            break
        a[i] = '8'
        kiemtra()"""
"""def sinhtohop(n,k):
    a = list(range(1,k+1))

    while True :
        count  = 0
        for i in a :
            if i % 2 != 0 :
                count += 1
        if count > k - count :
            print(*a)
        i = k-1
        while i >=0 and a[i] == n-k+i+1:
            i-= 1
        if i < 0 :
            break
        a[i] += 1
        for j in range(i+1,k):
            a[j] =a[j-1]+1
sinhtohop(5,3)"""

"""class Node:
    def  __init__(self,val):
        self.val = val
        self.left  = None
        self .right  = None
def insert(root,val):
    if root is None :
        return Node(val)
    if val < root.val :
        root.left  = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root
def postorder(root,res):
    if root is None :
        return
    postorder(root.left,res)
    postorder(root.right,res)
    res.append(root)
arr = list(map(int,input().split()))
root = None
for x  in arr :
    root = insert(root,x)
res = []
postorder(root,res)
print(*res)"""

"""def nto(x):
    if x < 2 :
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0 :
            return False
    return True
def  sinhtohop(n,k):
    a = list(range(1,k+1))
    index = 1
    while True :
         if nto(index):
             print(f"{index}:",*a)
         i = k - 1
         while i >= 0 and a[i] == n-k+i+1 :
             i-= 1
         if i < 0 :
             break
         a[i] += 1
         for j in range(i+1,k):
             a[j] = a[j-1]+1
         index += 1
n,k = map(int,input().split())
sinhtohop(n,k)
""""""
def max_subarray_sum(A):
    current_sum = A[0]
    max_sum = A[0]

    for i in range(1, len(A)):
        current_sum = max(A[i], current_sum + A[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
n = int(input())
for _ in range(n):
    k= int(input())
    a = list(map(int,input().split()))
    print(max_subarray_sum(a))
"""


"""def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        A.sort()
        root = A[(n-1) // 2]
        print(root)
solve()
"""
"""def caynhiphancanbang(arr,l,r,res):
    if l > r :
        return
    mid = (l+r) // 2

    caynhiphancanbang(arr,l,mid -1,res)
    caynhiphancanbang(arr,mid+1,r,res)
    res.append(str(arr[mid]))


n = int(input())
for _ in range(n):
    k =int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    l = 0
    r = k-1
    res= []
    caynhiphancanbang(arr,l,r,res)
    print(" ".join(res))"""
