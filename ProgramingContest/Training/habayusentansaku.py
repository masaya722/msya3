from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1
S = []
for _ in range(R):
    c = input()
    S.append(c)
maze = []
for _ in range(R):
    maze.append([-1] * C)

Q = deque()
Q.append((sy, sx))
maze[sy][sx] =0
while len(Q) > 0:
    jy, jx = Q.popleft()
    for jy2,jx2 in [(jy+1,jx),(jy-1,jx),(jy,jx-1),(jy,jx+1)]:
        if not 0 <= jy <R or not 0 <= jx < C:
            continue
        if S[jy][jx] == '#':
            continue
        if maze[jy2][jx2] == -1:
            maze[jy2][jx2] = maze[jy][jx]+1
            Q.append((jy2,jx2))

print(maze[gy][gx])