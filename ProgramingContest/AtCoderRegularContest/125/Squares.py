import math
INF = 998244353
N = int(input())
n = int(math.sqrt(N))
ans = 0
for p in range(1,n+1):
    q = N//p -p
    ans += q//2+1
    ans %=INF
print(ans)

