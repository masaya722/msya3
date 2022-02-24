n,k = map(int,input().split())
MOD = 10**9+7
get_nums = [i for i in range(k,n+2)]
ans = 0
for s in get_nums:
    max_s = (n+n-s+1)*s//2
    min_s = (s-1)*s//2
    ans+=max_s-min_s+1
    ans%=MOD
print(ans%MOD)