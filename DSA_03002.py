def tinh(a,b):
    min = int(str(a).replace('6','5'))+int(str(b).replace('6','5'))
    max = int(str(a).replace('5','6'))+int(str(b).replace('5','6'))
    print(min ,max)
a ,b  = map(int,input().split())
tinh(a,b)
