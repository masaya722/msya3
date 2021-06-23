import statistics

N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
s = A[N//2]
t = B[N//2]

ans =0
for i in range(N):
    ans += abs(s - A[i]) + abs(A[i] - B[i]) + abs(B[i] - t)

print(ans)