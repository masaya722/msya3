N = int(input())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append([a, b])
A.sort(key=lambda x: x[1] * -1)

B = []
for i in range(N):
    c, d = map(int, input().split())
    B.append([c, d])
B.sort()

count = 0
for a, b in A:
    for c, d in B:
        if a < c and b < d:
            B.remove([c, d])
            count += 1
            break
print(count)
