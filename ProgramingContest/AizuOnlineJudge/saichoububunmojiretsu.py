# pythonだとこの解き方で間に合わない

q = int(input())
for _ in range(q):
    A = input()
    B = input()

    dp = [[0 for _ in range(len(B)+1)]for _ in range(len(A)+1)]
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] +1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    print(dp[len(A)][len(B)])