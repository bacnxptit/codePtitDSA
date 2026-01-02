def thapHN(n,A,B,C):
    if n == 1 :
        print(f"{A} -> {C}")
        return
    thapHN(n-1,A,C,B)
    print(f"{A} -> {C}")
    thapHN(n-1,B,A,C)
n = int(input())
thapHN(n,'A','B','C')


"""
def thapHN(n,A,B,C):
    if n == 1 :
        print(f"{A}->{C}")
        return
    thapHN(n-1,A,C,B)
    print(f"{A}->{C}")
    thapHN(n-1,B,A,C)
n = int(input())
thapHN(3,'A','B','C')

"""