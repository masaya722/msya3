from collections import deque

N,M = map(int,input().split())
friends = [[]for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a -=1
    b -=1
    friends[a].append(b)
    friends[b].append(a)

Q= deque()
for i in range(N):
    Q.append(i)
    dist = [-1 for _ in range(N)]
    dist[i] = 0
    while Q:
        one = Q.popleft()
        for j in friends[one]:
            if dist[j] != -1:
                continue    
            dist[j] = dist[one]+1
            Q.append(j)
    print(dist.count(2))
