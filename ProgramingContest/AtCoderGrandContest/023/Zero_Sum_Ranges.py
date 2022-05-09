from collections import defaultdict


N =int(input())
A = list(map(int,input().split()))

sumA=[]
tmp = 0
for a in A:
    tmp+=a
    sumA.append(tmp)

cnt = defaultdict(int)
for i in range(N):
    cnt[sumA[i]]+=1

ans =0
for val,ct in cnt.items():
    if val ==0:
        ans+=ct
    if ct>1:
        ans+=ct*(ct-1)//2
print(ans)