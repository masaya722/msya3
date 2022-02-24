H,W,A,B = map(int,input().split())
ans = [[]for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i <B and j <A:
            ans[i].append(0)
        elif i>=B and j>=A:
            ans[i].append(0)
        else:
            ans[i].append(1)
for a in ans:
    row = ''
    for t in a:
        row+=str(t)
    print(row)