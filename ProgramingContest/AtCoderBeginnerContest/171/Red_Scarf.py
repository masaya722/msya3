N = int(input())
A = list(map(int, input().split()))
tmp = 0
for i in range(N):
    tmp ^=A[i]
ans = []
for i in range(N):
    ans.append(tmp^A[i])
print(*ans)