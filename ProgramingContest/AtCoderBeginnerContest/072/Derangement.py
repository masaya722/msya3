N = int(input())
p = list(map(int,input().split()))
flag  =False
ans = 0
for i in range(N):
    if i ==N-1:
        if p[i]==i+1:
            flag = True
    if flag:
        p[i],p[i-1]=p[i-1],p[i]
        ans+=1
    if p[i]==i+1:
        flag = True
    else:
        flag = False
print(ans)