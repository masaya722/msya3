N,P = map(int,input().split())
MOD = 10**9+7
a = pow(P-2,N-1,MOD)
ans = (P-1)*a%MOD
print(ans)