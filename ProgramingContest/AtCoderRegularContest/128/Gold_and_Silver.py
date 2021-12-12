n = int(input())
A= list(map(int,input().split()))
flag = False
ans = []
for i in range(n-1):
    if not flag and A[i]>A[i+1]:
        flag = True
        ans.append(1)
    elif flag and A[i]<A[i+1]:
        flag = False
        ans.append(1)
    else:
        ans.append(0)
if flag:
    ans.append(1)
else:
    ans.append(0)
print(*ans)