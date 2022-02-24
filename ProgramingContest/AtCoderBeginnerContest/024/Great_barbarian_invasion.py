from collections import defaultdict


N,D,K = map(int,input().split())
L = []
R = []
for i in range(D):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)
S = []
T = []
for i in range(K):
    s,t = map(int,input().split())
    S.append(s)
    T.append(t)
cnt = [0 for i in range(K)]
for i in range(D):
    for j in range(K):
        if L[i]<=S[j]<=R[i]:
            if L[i]<=T[j]<=R[i] and cnt[j]==0:
                cnt[j] = i+1
            elif R[i]<T[j]:
                S[j] = R[i]
            else:
                S[j] = L[i]
for ans in cnt:
    print(ans)