N,M = map(int,input().split())
if M !=0:
    A = list(map(int,input().split()))
    A.append(0)
    A.append(N+1)
else:
    print(1)
    exit()

A.sort()
diff = []
for i in range(M+1):
    diff.append(A[i+1]-A[i]-1)

set_diff = set(diff)
if 0 in set_diff:
    set_diff.remove(0)
if len(set_diff) !=0:
    s = min(set_diff)
else:
    print(0)
    exit()


ans = 0
for df in diff:
    if df%s ==0:
        ans +=df//s
    else:
        ans +=df//s+1
print(ans)