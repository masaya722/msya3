N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
for i in range(N):
    if i !=N-1:
        if A[i]<A[i+1]:
            print('up',A[i+1]-A[i])
        elif A[i] ==A[i+1]:
            print('stay')
        else:
            print('down',A[i]-A[i+1])
