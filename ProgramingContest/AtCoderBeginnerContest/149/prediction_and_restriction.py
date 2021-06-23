N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

result = [[]for _ in range(K)]

for i, j in enumerate(T):
    result[i % K].append(j)

ans = 0
for one_set in result:
    dp = [[0]*3 for _ in range(len(one_set))]
    dp[0][0] = R if one_set[0] == "s" else 0
    dp[0][1] = S if one_set[0] == "p" else 0
    dp[0][2] = P if one_set[0] == "r" else 0
    for turn in range(len(one_set)-1):
        if one_set[turn+1] == "s":
            dp[turn+1][0] = max(dp[turn][1]+R, dp[turn][2]+R)
            dp[turn+1][1] = max(dp[turn][0], dp[turn][2])
            dp[turn+1][2] = max(dp[turn][0], dp[turn][1])
        if one_set[turn+1] == "p":
            dp[turn+1][0] = max(dp[turn][1], dp[turn][2])
            dp[turn+1][1] = max(dp[turn][0]+S, dp[turn][2]+S)
            dp[turn+1][2] = max(dp[turn][0], dp[turn][1])
        if one_set[turn+1] == "r":
            dp[turn+1][0] = max(dp[turn][1], dp[turn][2])
            dp[turn+1][1] = max(dp[turn][0], dp[turn][2])
            dp[turn+1][2] = max(dp[turn][0]+P, dp[turn][1]+P)
    ans += max(dp[len(one_set)-1])
print(ans)

