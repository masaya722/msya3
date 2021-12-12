N, P = map(int, input().split())
A = list(map(int, input().split()))
even = []
for a in A:
    if a % 2 == 0:
        even.append(a)
if P == 0:
    if len(even) == N:
        print(2**N)
    else:
        print(2**(N-1))
else:
    if len(even) == N:
        print(0)
    else:
        print(2**(N-1))