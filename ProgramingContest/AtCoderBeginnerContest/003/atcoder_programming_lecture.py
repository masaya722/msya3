N,K = map(int,input().split())
R= list(map(int,input().split()))
R.sort()
chR = R[N-K:N]

ans = 0
for plus in chR:
    if plus>ans:
        ans =(plus+ans)/2
print(ans)
