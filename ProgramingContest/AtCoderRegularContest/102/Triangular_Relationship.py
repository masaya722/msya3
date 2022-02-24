n,k = map(int,input().split())
ans = 0
cnt = 0
for i in range(1,n+1):
    if i%k ==0:
        cnt+=1
ans += cnt**3
cnt=0
if k%2==0:
    for i in range(1,n+1):
        if i%k ==k//2:
            cnt+=1
    ans += cnt**3
print(ans)
