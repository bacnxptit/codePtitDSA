def doiTien(s,menhGia):
    menhGia.sort(reversed = True)
    total = 0
    conLai = s
    for c in menhGia:
        if conLai == 0 :
            break
        count = conLai // c
        if count > 0 :
            total 