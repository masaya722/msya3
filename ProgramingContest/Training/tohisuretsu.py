def dfs(A, R, N):
    if R == 1:
        return A
    for i in range(0, N - 1):

        A *= R
        if A > 10 ** 9:
            return "large"
    return A


A, R, N = map(int, input().split())
print(dfs(A, R, N))
