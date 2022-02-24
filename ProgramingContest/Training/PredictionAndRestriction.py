N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

checkList = [[] for _ in range(K)]
for i in range(N):
    checkList[i % K].append(T[i])

total = 0
for cl in checkList:
    # dp[i][j] i..0=rock 1 = scissors 2=paper
    dp = [[0]*3 for _ in range(len(cl))]

    dp[0][0] = R if cl[0] == "s" else 0
    dp[0][1] = S if cl[0] == "p" else 0
    dp[0][2] = P if cl[0] == "r" else 0

    for i in range(len(cl)-1):
        if cl[i+1] == "s":
            dp[i+1][0] = max(R + dp[i][1], R + dp[i][2])
            dp[i+1][1] = max(dp[i][0], dp[i][2])
            dp[i+1][2] = max(dp[i][0], dp[i][1])
        if cl[i+1] == "p":
            dp[i+1][0] = max(dp[i][1], dp[i][2])
            dp[i+1][1] = max(S+dp[i][0], S+dp[i][2])
            dp[i+1][2] = max(dp[i][0], dp[i][1])
        if cl[i+1] == "r":
            dp[i+1][0] = max(dp[i][1], dp[i][2])
            dp[i+1][1] = max(dp[i][0], dp[i][2])
            dp[i+1][2] = max(P+dp[i][0], P+dp[i][1])
    total += max(dp[len(cl)-1])
print(total)