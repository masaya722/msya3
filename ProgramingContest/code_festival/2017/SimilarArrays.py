N = int(input())
A = list(map(int, input().split()))
B = []
for a in A:
    if a % 2 == 0:
        B.append(a)
print(3**N -2**len(B))
