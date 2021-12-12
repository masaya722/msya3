n,m = map(int,input().split())
MOD = 10**9+7
if abs(n-m)>1:
    print(0)
else:
    ans = 1
    for i in range(1,n+1):
        ans*=i
        ans%=MOD
    for i in range(1,m+1):
        ans*=i
        ans%=MOD
    if abs(n-m)==1:
        print(ans)
    else:
        print(ans*2%MOD)
