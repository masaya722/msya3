H,W = map(int,input().split())

x = [False]*W
y = [False]*H

A = []
for i in range(H):
    a = list(input())
    A.append(a)
    for j in range(W):
        if A[i][j] == '#':
            x[j] = True
            y[i] = True

for i in range(H):
    if not y[i]:
        continue
    ans = []
    for j in range(W):
        if x[j]:
            ans.append(A[i][j])
    print("".join(ans))
