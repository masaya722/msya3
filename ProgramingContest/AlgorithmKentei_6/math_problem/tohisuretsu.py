def solve(A, R, N):
    for _ in range(0, N - 1):
        if R==1:
            return A
        A *= R

        if A > 10 ** 9:
            return "large"
    return A


A, R, N = map(int, input().split())
ans = solve(A, R, N)
print(ans)
