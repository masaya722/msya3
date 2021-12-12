import heapq
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
heapq.heapify(B)
tmp = heapq.heappop(B)
flag = False
for i in range(N):
    if tmp<=A[i]:
        if len(B) !=0:
            tmp = heapq.heappop(B)
        else:
            flag = True
            break
if len(B)==0 and flag:
    print('YES')
else:
    print('NO')

