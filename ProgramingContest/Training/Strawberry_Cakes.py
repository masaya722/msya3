H,W,K = map(int,input().split())
S =[]
for _ in range(H):
    S.append(input())
ans = [[0]*W for _ in range(H)]
berry= 0
for i in range(H):
    flag = False
    for j in range(W):
        if S[i][j] =='#':
            berry+=1
            ans[i][j] = berry
            flag = True
        if flag:
            ans[i][j] = berry
for i in range(H-1,-1,-1):
    berry = 0
    for j in range(W-1,-1,-1):
        if ans[i][j] != 0:
            berry = ans[i][j]
        else:
            ans[i][j] = berry
for i in range(H):
    if i ==0:
        count = 0
        while ans[count] == [0]*W:
            count+=1
        ans[i] = ans[count]
    elif ans[i]==[0]*W:
        ans[i] = ans[i-1]
for i in range(H):
    print(*ans[i])
