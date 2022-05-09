from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

cnt = defaultdict(int)

for a in A:
    prod = 1
    if cnt[a]!=0:
        cnt[a]+=1
        continue
    while a*prod<=10**6:
        cnt[a*prod]+=1
        prod+=1

ans =0
for a in A:
    if cnt[a]==1:
        ans+=1
print(ans)
