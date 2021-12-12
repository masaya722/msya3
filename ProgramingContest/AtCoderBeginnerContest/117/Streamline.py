N,M= map(int,input().split())
X = list(map(int,input().split()))
X.sort()

diff = []
for i in range(M-1):
    diff.append(X[i+1]-X[i])
diff.sort(reverse=True)

maximun =X[M-1]-X[0]

if N>=M:
    print(0)
else:
    for i in range(N-1):
        maximun-=diff[i]
    print(maximun)