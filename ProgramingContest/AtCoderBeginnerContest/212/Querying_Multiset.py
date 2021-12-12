import heapq
Q = int(input())
ans = []
heapq.heapify(ans)
plus = 0
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] ==1:
        heapq.heappush(ans,query[1]-plus)
    elif query[0] ==2:
        plus+=query[1]
    else:
        print(heapq.heappop(ans)+plus)