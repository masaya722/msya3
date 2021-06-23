N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
count = [0 for _ in range(N+1)]
for i in range(N):
    count[A[i]] +=1

ans =0
for j in range(N):
    ans += count[B[C[j]-1]]
print(ans)
