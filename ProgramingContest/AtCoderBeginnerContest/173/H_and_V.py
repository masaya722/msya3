H, W, K = map(int, input().split())
C = []
for i in range(H):
    C.append(list(input()))
ans=0
count = 0
for i in range(2**H):
    for j in range(2**W):
        for h in range(H):
            for w in range(W):
                if i>>h&1:
                    break
                if j>>w&1:
                    continue
                if C[h][w] =='#':
                    count+=1
        if count ==K:
            ans+=1
        count =0
print(ans)
