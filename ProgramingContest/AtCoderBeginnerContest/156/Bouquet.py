n,a,b =map(int,input().split())
MOD = 10**9+7

 
def ncr(n, r):
    top = b2 = 1
 
    for i in range(n, n-r, -1): top = top*i % MOD
    for k in range(r, 0, -1): b2 = b2*k % MOD
 
    return top*pow(b2, -1, mod=MOD) % MOD
 
print((pow(2,n,MOD)-1-((ncr(n,a)+ncr(n,b))%MOD))%MOD)