N = int(input())
A =list(map(int,input().split()))
x = 0
for i in range(N-1,-1,-1):
    if i%2==0:
        x+=A[i]
    else:
        x-=A[i]
first =x//2
ans = [x]
for i in range(N):
    if i==N-1:
        break
    tmp = A[i]-(ans[len(ans)-1]//2)
    ans.append(tmp*2)
print(*ans)