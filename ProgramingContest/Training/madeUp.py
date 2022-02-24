N = int(input())
A = list(map(int, input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

cnt = [0 for _ in range(N+1)]
for a in A:
    cnt[a]+=1
ans = 0
for i in range(N):
    ans += cnt[B[C[i]-1]]
print(ans)