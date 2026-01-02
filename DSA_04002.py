MOD = 10**9 + 7
PHI = MOD - 1

MOD = 10**9 + 7

def luy_thua_dao(s):
    a = int(s) % MOD
    r = int(s[::-1])
    if a == 0 and r > 0:
        return 0
    return pow(a, r, MOD)

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(luy_thua_dao(s))
   
