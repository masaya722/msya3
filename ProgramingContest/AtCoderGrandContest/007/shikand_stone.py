from collections import deque
H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(input()))

count = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            count += 1
if H+W-1 != count:
    print("Impossible")
    exit()

Q = deque()
Q.append((0, 0))

while Q:
    i, j = Q.popleft()
    for i1, j1 in [(i, j+1), (i+1, j)]:
        if i1 < H and j1 < W:
            if A[i1][j1] == "#":
                Q.append((i1, j1))
        if i1 == H-1 and j1 == W-1:
            print("Possible")
            exit()
print("Impossible")
