n,w = map(int,input().split())
dp = [0 for _ in range(2*(10**5)+1)]
for i in range(n):
    s,t,p = map(int,input().split())
    dp[s]+=p
    dp[t]-=p
total = 0
for d in dp:
    total+=d
    if total>w:
        print('No')
        exit()
print('Yes')
