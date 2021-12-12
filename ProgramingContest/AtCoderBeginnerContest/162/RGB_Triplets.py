N = int(input())
S = input()
dp = [[0 for _ in range(3)]for _ in range(N)]
for i in range(N):
    if S[i] =="R":
        dp[i][0]+=1
        if i!=0:
            dp[i][0]=dp[i-1][0]+1
            dp[i][1] = dp[i-1][1]
            dp[i][2] = dp[i-1][2]
    elif S[i] =="G":
        dp[i][1] +=1
        if i!=0:
            dp[i][1]=dp[i-1][1]+1
            dp[i][0] = dp[i-1][0]
            dp[i][2] = dp[i-1][2]
    else:
        dp[i][2] +=1
        if i!=0:
            dp[i][2]=dp[i-1][2]+1
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]
ans = 0
for i in range(N):
    for j in range(i+1,N):
        if S[i] != S[j] and S[i] != "R" and S[j] != "R":
            if j+j-i<N and S[j+j-i] =="R":
                ans +=dp[N-1][0]-dp[j][0]-1
            else:
                ans +=dp[N-1][0]-dp[j][0]
        elif S[i] != S[j] and S[i] != "G" and S[j] != "G":
            if j+j-i<N and S[j+j-i] =="G":
                ans +=dp[N-1][1]-dp[j][1]-1
            else:
                ans +=dp[N-1][1]-dp[j][1]
        elif S[i] != S[j] and S[i] != "B" and S[j] != "B":
            if j+j-i<N and S[j+j-i] =="B":
                ans +=dp[N-1][2]-dp[j][2]-1
            else:
                ans +=dp[N-1][2]-dp[j][2]
print(ans)