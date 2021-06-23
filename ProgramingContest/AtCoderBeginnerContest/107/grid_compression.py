H,W = map(int,input().split())
A= []
for _ in range(H):
    a = list(input())
    A.append(a)

x = [False]*W
y = [False]*H
for i in range(H):
    for j in range(W):
        if A[i][j] =='#':
            x[j] = True
            y[i] = True


for i in range(H):
    if not y[i]:
        continue
    ans =[]
    for j in range(W):
        if x[j]:
            ans.append(A[i][j])
    print("".join(ans))





