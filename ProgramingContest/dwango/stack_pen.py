N = int(input())
K = list(map(int,input().split()))
maxk = max(K)
INF = 10**18
temp = [INF]
for i in range(N-1):
    temp.append(K[i])
temp.append(INF)
ans = []
for i in range(N):
    ans.append(min(temp[i],temp[i+1]))
print(*ans)

