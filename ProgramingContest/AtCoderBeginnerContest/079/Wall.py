import sys
sys.setrecursionlimit(10**7)
H,W = map(int,input().split())
C = []
for i in range(10):
    C.append(list(map(int,input().split())))

INF = 10**18
dp = [C[i][1] for i in range(10)]

def dfs(i,j,total):
    if total>=dp[i]:
        return
    for num,c in enumerate(C[j]):
        if num == j or num ==i:
            continue
        if num ==1:
            dp[i] = min(dp[i],total+c)
        elif total+c<dp[i]:
            dfs(i,num,total+c)
    return
for i in range(10):
    dfs(i,i,0)
ans = 0
for i in range(H):
    A = list(map(int,input().split()))
    for a in A:
        if a ==-1:
            continue
        else:
            ans+=dp[a]
print(ans)


    