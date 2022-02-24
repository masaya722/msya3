MOD = 998244353
N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = A[0]*A[0]
t = 0
for i in range(1,N):
    t+=A[i-1]
    ans += A[i]*A[i]+A[i]*t
    t= t*2%MOD
print(ans%MOD)