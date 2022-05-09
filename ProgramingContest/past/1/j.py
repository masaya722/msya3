from collections import deque

H,W = map(int,input().split())
A = []
for i in range(H):
    A.append(list(map(int,input().split())))

done = [[False for _ in range(W)]for _ in range(H)]
cost = [[10**9 for _ in range(W)]for _ in range(H)]
cost[H-1][0] = 0
Q = deque()
Q.append((H-1,0))
while Q:
    i,j = Q.popleft()
    A[i][j] =0
    if done[i][j]:
        continue
    done[i][j] = True
    if i ==H-1 and j ==0:
        cost[H-1][1] = min(cost[H-1][1],cost[i][j]+A[H-1][1])
        Q.append((H-1,1))
        cost[H-2][0] = min(cost[H-2][0],cost[i][j]+A[H-2][0])
        Q.append((H-2,0))
    elif i ==H-1 and j ==W-1:
        cost[H-1][W-2] = min(cost[H-1][W-2],cost[i][j]+A[H-1][W-2])
        Q.append((H-1,W-2))
        cost[H-2][W-1] = min(cost[H-2][W-1],cost[i][j]+A[H-2][W-1])
        Q.append((H-2,W-1))
        done = [[False for _ in range(W)]for _ in range(H)]
    elif i ==0 and j ==W-1:
        continue
    elif i ==0 and j == 0:
        cost[1][0] = min(cost[1][0],cost[i][j]+A[1][0])
        Q.append((1,0))
        cost[0][1] = min(cost[0][1],cost[i][j]+A[0][1])
        Q.append((0,1))
    elif j ==0:
        cost[i-1][0] = min(cost[i-1][0],cost[i][j]+A[i-1][0])
        Q.append((i-1,0))
        cost[i][1] = min(cost[i][1],cost[i][j]+A[i][1])
        Q.append((i,1))
        cost[i+1][0] = min(cost[i+1][0],cost[i][j]+A[i+1][0])
        Q.append((i+1,0))
    elif j ==W-1:
        cost[i-1][W-1] = min(cost[i-1][W-1],cost[i][j]+A[i-1][W-1])
        Q.append((i-1,W-1))
        cost[i][W-2] = min(cost[i][W-2],cost[i][j]+A[i][W-2])
        Q.append((i,W-2))
        cost[i+1][W-1] = min(cost[i+1][W-1],cost[i][j]+A[i+1][W-1])
        Q.append((i+1,W-1))
    elif i ==0:
        cost[0][j-1] = min(cost[0][j-1],cost[i][j]+A[0][j-1])
        Q.append((0,j-1))
        cost[1][j] = min(cost[1][j],cost[i][j]+A[1][j])
        Q.append((1,j))
        cost[0][j+1] = min(cost[0][j+1],cost[i][j]+A[0][j+1])
        Q.append((0,j+1))
    elif i ==H-1:
        cost[H-1][j-1] = min(cost[H-1][j-1],cost[i][j]+A[H-1][j-1])
        Q.append((H-1,j-1))
        cost[H-2][j] = min(cost[H-2][j],cost[i][j]+A[H-2][j])
        Q.append((H-2,j))
        cost[H-1][j+1] = min(cost[H-1][j+1],cost[i][j]+A[H-1][j+1])
        Q.append((H-1,j+1))
    else:
        cost[i-1][j] = min(cost[i-1][j],cost[i][j]+A[i-1][j])
        Q.append((i-1,j))
        cost[i+1][j] = min(cost[i+1][j],cost[i][j]+A[i+1][j])
        Q.append((i+1,j))
        cost[i][j-1] = min(cost[i][j-1],cost[i][j]+A[i][j-1])
        Q.append((i,j-1))
        cost[i][j+1] = min(cost[i][j+1],cost[i][j]+A[i][j+1])
        Q.append((i,j+1))
print(cost[0][W-1])