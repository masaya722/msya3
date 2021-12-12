N,K= map(int,input().split())
a = list(map(int,input().split()))

ans= sum(a[0:K])
tmp =ans
for i in range(N-K):
    tmp =tmp-a[i]+a[i+K]
    ans+=tmp
print(ans)