H,W,K = map(int,input().split())
blocks = []
S = []
for i in range(H):
    s = input()
    S.append(s)
    if "#" in s:
        blocks.append(i)

ans = [[0]*W for _ in range(H)]
berry =0
for i in range(H):
    flag = False
    for j in range(W):
        if S[i][j] =="#":
            berry+=1
            flag =True
        if flag:
            ans[i][j] = berry

for i in range(H):
    berry = 0
    for j in range(W-1,-1,-1):
        if S[i][j] =="#":
            berry = ans[i][j]
        if ans[i][j] ==0:
            ans[i][j] = berry
for i in range(H):
    if ans[i] == [0]*W:
        if i ==0:
            tmp = 1
            while ans[tmp] == [0]*W:
                tmp+=1
            ans[i] = ans[tmp]
        else:
            ans[i] = ans[i-1]
for i in range(H):
    print(*ans[i]) 
            