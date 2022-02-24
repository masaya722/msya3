from collections import defaultdict

cnt = defaultdict(int)
N = int(input())
A= list(map(int,input().split()))
for a in A:
    cnt[a]+=1
ans =0
for i in cnt.keys():
    ans+=1
print(ans)
