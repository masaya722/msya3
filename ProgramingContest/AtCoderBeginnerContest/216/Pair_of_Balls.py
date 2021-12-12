from collections import deque
n,m = map(int,input().split())
A = []
memo = [[]for _ in range(n)]
cnt= [0 for _ in range(n)]
for i in range(m):
    k = int(input())
    A.append(deque(map(lambda x: int(x)-1,input().split())))
    memo[A[i][0]].append(i)
    cnt[A[i][0]] +=1
Q = deque()
for i in range(n):
    if cnt[i] ==2:
        Q.append(i)
        Q.append(i)
while Q:
    x = Q.popleft()
    y = memo[x].pop()
    A[y].popleft()
    if A[y]:
        memo[A[y][0]].append(y)
        cnt[A[y][0]]+=1
        if cnt[A[y][0]] ==2:
            Q.append(A[y][0])
            Q.append(A[y][0])
for i in range(m):
    if A[i]:
        print("No")
        exit()
print("Yes")
