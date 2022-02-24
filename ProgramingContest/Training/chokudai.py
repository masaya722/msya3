MOD = 10**9+7
chokudai = "chokudai"
S= input()
lens = len(S)
dp = [[0]*lens for _ in range(8)]
for i in range(8):
    for j in range(lens):
        if i ==0:
            if S[j] == chokudai[i]:
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] =dp[i][j-1]+1
            else:
                dp[i][j] = dp[i][j-1]
        else:
            if j>0:
                if S[j] == chokudai[i]:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
print(dp[7][lens-1]%MOD)