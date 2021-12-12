N,M,Q = map(int,input().split())
S = []
for _ in range(N):
    w,v = map(int,input().split())
    S.append((v,w))
S.sort(reverse=True)
x = list(map(int,input().split()))
for _ in range(Q):
    l,r = map(int,input().split())
    l -=1
    ans= 0
    X = []
    for i in range(l):
        X.append(x[i])
    for i in range(r,M):
        X.append(x[i])
    X.sort()
    tmp = []
    for i in range(len(X)):
        for j in range(len(S)):
            v,w = S[j]
            if X[i] >=w and j not in tmp:
                ans+=v
                tmp.append(j)
                break
    print(ans)
