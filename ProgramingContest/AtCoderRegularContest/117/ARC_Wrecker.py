N = int(input())
A = list(map(int,input().split()))
A.append(0)
A.sort()
INF = 10**9+7
ans = 0
for i in range(N):
    if ans ==0:
        ans+=A[i+1]-A[i]+1
    else:
        ans*=A[i+1]-A[i]+1
    ans%=INF
print(ans%INF)