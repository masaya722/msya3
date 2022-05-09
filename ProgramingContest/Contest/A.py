from collections import defaultdict
import itertools


N,K = map(int,input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)

ans = 0
for i in range(1,N+1):
    for ls in itertools.combinations(range(N),i):
        T = ''
        for j in ls:
            cnt = defaultdict(int)
            for s in S[j]:
                T+=s
        tmp = 0
        for t in list(T):
            cnt[t]+=1
        for c in cnt.values():
            if c ==K:
                tmp+=1
        ans = max(ans,tmp)
print(ans)
