from collections import deque
import heapq
A1 = deque()
A2 = []
heapq.heapify(A2)
Q = int(input())
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] ==1:
        A1.append(query[1])
    elif query[0] ==2:
        if len(A2) ==0:
            print(A1.popleft())
        else:
            print(heapq.heappop(A2))
    else:
        for i in range(len(A1)):
            heapq.heappush(A2,A1.popleft())