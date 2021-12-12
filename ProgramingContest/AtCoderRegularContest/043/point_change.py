N,A,B = map(int,input().split())
total = A*N
S =[]
for i in range(N):
    S.append(int(input()))
S.sort()

if S[N-1]-S[0] ==0:
    print(-1)
else:
    P = B/(S[N-1]-S[0])
    Q = A -(sum(S)/N)*P
    print(P,Q)