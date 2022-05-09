N,X =map(int,input().split())
S = input()
tmp = []
for i in range(N):
    if (len(tmp)>0 and S[i]=='U') and (tmp[-1]=='L' or tmp[-1]=='R'):
        tmp.pop()
    else:
        tmp.append(S[i])

for t in tmp:
    if t=='U':
        if X %2==0:
            X = X//2
        else:
            X = (X-1)//2
    elif t=='L':
        X = X*2
    else:
        X = X*2+1
print(X)