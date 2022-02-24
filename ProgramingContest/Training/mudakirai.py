from collections import defaultdict

N, X = map(int, input().split())
A = []
B = []
for i in range(N):
    if i % 2 == 0:
        A.append(int(input()))
    else:
        B.append(int(input()))


def has_bit(n, i):
    return n & (1 << i) > 0


dic = defaultdict(int)
for n in range(1 << len(A)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += A[i]
    dic[s] += 1

ans = 0
for n in range(1 << len(B)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += B[i]
    ans += dic[X - s]

print(ans)