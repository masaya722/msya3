N,K = map(int,input().split())

ans = 0
for i in range(1,N+1):
    count = 0
    while K>i:
        i*=2
        count+=1
    ans+=((1/2)**count)*(1/N)
print(ans)    