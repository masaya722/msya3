from collections import deque
H,W = map(int,input().split())
S = []
for _ in range(H):
    S.append(input())
ans = []
for h in range(H):
    for w in range(W):
        cnt = [[0 for _ in range(W)]for _ in range(H)]
        Q = deque()
        Q.append((h,w))
        tmp = 0
        while Q:
            i,j = Q.popleft()
            if S[i][j] =='#':
                continue
            else:
                for i1,j1 in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=i1<H and 0<=j1<W:
                        if cnt[i1][j1]>0 or (i1 ==h and j1 ==w):
                            continue
                        else:
                            if S[i1][j1]=='.':
                                cnt[i1][j1] = cnt[i][j]+1
                                tmp = max(tmp,cnt[i1][j1])
                                Q.append((i1,j1))
        ans.append(tmp)
print(max(ans))
                            
