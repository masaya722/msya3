N = int(input())
A = []
B = []
C = []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

happy = [[0]*3 for _ in range(N)]
happy[0][0]= A[0]
happy[0][1] = B[0]
happy[0][2]= C[0]

for i in range(1,N):
    happy[i][0] = max(happy[i-1][1]+A[i],happy[i-1][2]+A[i])
    happy[i][1] = max(happy[i-1][0]+B[i],happy[i-1][2]+B[i])
    happy[i][2] = max(happy[i-1][0]+C[i],happy[i-1][1]+C[i])
print(max(happy[N-1]))
