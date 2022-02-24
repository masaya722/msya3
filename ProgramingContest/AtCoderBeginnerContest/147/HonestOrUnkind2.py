from collections import defaultdict


N = int(input())
testimony = [[-1 for _ in range(N)] for _ in range(N)]

for i in range(N):
    A = int(input())
    for j in range(A):
        x,y = map(int,input().split())
        testimony[i][x-1] = y
ALL = 1<<N
ans = 0

for i in range(ALL):
    cnt = [0 for _ in range(N)]
    for j in range(N):
        if i>>j&1:
            cnt[j] = 1
    ok = True
    for j in range(N):
        if cnt[j]==1:
            for k in range(N):
                if testimony[j][k] ==-1:
                    continue
                if testimony[j][k]!=cnt[k]:
                    ok = False
    if ok:
        ans = max(ans,sum(cnt))
print(ans)
