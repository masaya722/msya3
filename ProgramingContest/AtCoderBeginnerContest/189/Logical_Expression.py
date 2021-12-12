N = int(input())
dp = [[0 for _ in range(2)]for _ in range(N+1)]
dp[0][0] = 1
dp[0][1] = 1
S = []
for _ in range(N):
    S.append(input())

for i in range(1, N):
    if S[i-1] == 'AND':
        dp[i][0] += dp[i-1][0]
        dp[i][1] += dp[i-1][1]*2+dp[i-1][0]
    else:
        dp[i][0] += dp[i-1][0]*2+dp[i-1][1]
        dp[i][1] += dp[i-1][1]
if S[N-1]=='AND':
    print(dp[N-1][0])
else:
    print(dp[N-1][1]+dp[N-1][0]*2)

