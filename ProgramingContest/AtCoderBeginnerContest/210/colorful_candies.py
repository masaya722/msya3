from collections import Counter

N,K = map(int,input().split())
c = list(map(int,input().split()))

now = 0
ans = 0
count = Counter()
for i in range(N):
    if count[c[i]] ==0:
        count[c[i]]+=1
        now +=1
    else:
        count[c[i]]+=1
    if i>=K:
        count[c[i-K]]-=1
        if count[c[i-K]]==0:
            now -=1
    ans =max(now,ans)
print(ans)
    