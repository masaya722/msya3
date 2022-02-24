N = int(input())
A = []
for i in range(2*N-1):
    a = [0]*(i+1)+list(map(int,input().split()))
    A.append(a)

ans = 0
def dfs(s,x):
    global ans
    si = -1
    for i in range(2*N):
        if not s[i]:
            si = i
            break
    if si == -1:
        ans = max(ans,x)
        return
    s[si] = True
    for i in range(2*N):
        if (not s[i]) and si !=i:
            s[i] = True
            dfs(s,x^A[si][i])
            s[i] = False

s = [False for _ in range(2*N)]
dfs(s,0)
print(ans)
