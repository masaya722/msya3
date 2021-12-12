N = int(input())
A =list(map(int,input().split()))
tmp = [0]
for i in range(N):
    tmp.append(tmp[i]+A[i])
ans = 0
max_tmp = 0
next = 0
for i in range(N+1):
    max_tmp = max(max_tmp,tmp[i])
    ans = max(ans,next+max_tmp)
    next = next+tmp[i]
print(ans)
