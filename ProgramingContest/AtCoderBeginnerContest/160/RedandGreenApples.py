import heapq


X,Y,A,B,C = map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
R = list(map(int,input().split()))
P.sort(reverse=True)
Q.sort(reverse=True)
uses = []
for i in range(X):
    uses.append(P[i])
for i in range(Y):
    uses.append(Q[i])

heapq.heapify(uses)
R.sort(reverse=True)
for i in range(C):
    j = heapq.heappop(uses)
    if R[i]>j:
        heapq.heappush(uses,R[i])
    else:
        heapq.heappush(uses,j)
        break
print(sum(uses))
