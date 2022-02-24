H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
dp = [[0 for _ in range(W)]for _ in range(H)]

for i in range(H):
    for j in range(W):
        tmp1 = 0
        tmp2 = 0
        if i>0 and j==0:
            if S[i][j] != S[i-1][j]:
                tmp1 = 1
            dp[i][j] = dp[i-1][j]+tmp1
        elif i==0 and j >0:
            if S[i][j] != S[i][j-1]:
                tmp2 = 1
            dp[i][j] = dp[i][j-1]+tmp2
        elif i>0 and j>0:
            if S[i][j] != S[i-1][j]:
                tmp1 = 1
            if S[i][j] != S[i][j-1]:
                tmp2 = 1
            dp[i][j] = min(dp[i-1][j]+tmp1,dp[i][j-1]+tmp2)

if S[0][0] =="#" or S[H-1][W-1]=="#":
    print(dp[H-1][W-1]//2+1)
else:
    print(dp[H-1][W-1]//2)