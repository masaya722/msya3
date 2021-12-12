N = int(input())
MOD= 998244353
A= list(map(int,input().split()))
B =list(map(int,input().split()))
dp = [[0 for _ in range(3001)]for _  in range(N)]
for i in range(A[0],B[0]+1):
    if i>0:
        dp[0][i] = dp[0][i-1]+1
    else:
        dp[0][i] = 1
for i in range(B[0]+1,3001):
    dp[0][i] = dp[0][i-1]
for i in range(1,N):
    tmp = 0
    for j in range(A[i],B[i]+1):
        dp[i][j] = (dp[i-1][j]+tmp)%MOD
        tmp = dp[i][j]
    for j in range(B[i]+1,3001):
        dp[i][j] = dp[i][j-1]
print(dp[N-1][3000]%MOD) 