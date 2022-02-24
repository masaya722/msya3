X,Y = map(int,input().split())
if (X+Y)%3 !=0:
    print(0)
    exit()
mv_cnt = (X+Y)//3
MOD = 10**9+7

def ncr(n, r):
    top = b2 = 1
 
    for i in range(n, n-r, -1): top = top*i % MOD
    for k in range(r, 0, -1): b2 = b2*k % MOD
 
    return top*pow(b2, -1, mod=MOD) % MOD

print(ncr(X-mv_cnt+Y-mv_cnt,X-mv_cnt))