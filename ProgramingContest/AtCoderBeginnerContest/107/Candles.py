n,k = map(int,input().split())
x = list(map(int,input().split()))
dp = [0 for _ in range(n-k+1)]
flag = x.count(0) ==1
if flag and k ==1:
    print(0)
    exit()
for i in range(n-k+1):
    if flag:
        if x[i+k-2]>=0 and x[i]<=0:
            dp[i] = min(x[i+k-2]*2+abs(x[i]),x[i+k-2]+abs(x[i]*2))
        elif x[i+k-2]<=0 and x[i]<=0:
            dp[i] = abs(x[i])
        elif x[i+k-2]>=0 and x[i]>=0:
            dp[i] = x[i+k-2]
    else:
        if x[i+k-1]>=0 and x[i]<=0:
            dp[i] = min(x[i+k-1]*2+abs(x[i]),x[i+k-1]+abs(x[i]*2))
        elif x[i+k-1]<=0 and x[i]<=0:
            dp[i] = abs(x[i])
        elif x[i+k-1]>=0 and x[i]>=0:
            dp[i] = x[i+k-1]
print(min(dp))