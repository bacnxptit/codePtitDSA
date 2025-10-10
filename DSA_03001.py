a=[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
def doiTien(menhGia):
    a.sort(reverse= True)
    conLai = menhGia
    total = 0
    for i in a :
        if conLai == 0 :
            break
        count = conLai // i
        if count > 0 :
            total += count
            conLai -= i * count
    return total
n = int(input())
for  _ in range(n):
    k = int(input())
    print(doiTien(k))

