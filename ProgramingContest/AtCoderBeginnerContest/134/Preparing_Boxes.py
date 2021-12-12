N = int(input())
A = [0]+list(map(int,input().split()))
B = [0 for _ in range(N+1)]
for i in range(N,0,-1):
    sum = 0
    for j in range(i+i,N+1,i):
        sum ^=B[j]
    if sum ==A[i]:
        B[i]=0
    else:
        B[i]=1

ans = []
for i in range(1,N+1):
    if B[i]==1:
        ans.append(i)
if len(ans)==0:
    print(0)
else:
    print(len(ans))
    print(*ans)

