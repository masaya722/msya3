N,K = map(int,input().split())
A = []
for i in range(N):
    a = list(map(int,input().split()))
    A.append(a)

L = K**2 //2 + 1

wa  = -1
ac = 10**9+1

while wa +1 < ac:
    wj = (wa + ac)//2
    ok = False
    s = [[0]*(N+1)for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            s[i+1][j+1] = 1 if A[i][j]>wj else 0
    for i in range(N+1):
        for j in range(N):
            s[i][j+1] += s[i][j]
    for i in range(N):
        for j in range(N+1):
            s[i+1][j] += s[i][j]
    for i in range(N+1-K):
        for j in range(N+1-K):
            now = s[i+K][j+K]
            now -= s[i][j+K]
            now -= s[i+K][j]
            now += s[i][j]

            if now <L:
                ok = True
    if ok:
        ac = wj
    else:
        wa = wj

print(ac)