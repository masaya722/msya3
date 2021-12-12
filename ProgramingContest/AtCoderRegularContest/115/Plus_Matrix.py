N = int(input())
C = []
for i in range(N):
    C.append(list(map(int,input().split())))

A = [0]
B = [0]
for i in range(N-1):
    A.append(A[-1]+C[i+1][0]-C[i][0])
    B.append(B[-1]+C[0][i+1]-C[0][i])

minA = min(A)
minB = min(B)
for i in range(N):
    A[i]+=abs(minA)
    B[i]+=abs(minB)
plus = 0
if C[0][0]>=A[0]+B[0]:
    plus =C[0][0]-A[0]-B[0]
else:
    print('No')
    exit()
for i in range(N):
    A[i]+=plus
for i in range(N):
    for j in range(N):
        if C[i][j] != A[i]+B[j]:
            print('No')
            exit()
print('Yes')
print(*A)
print(*B)
