N,M = map(int,input().split())
B = []
for i in range(N):
    b = input()
    tmp =[]
    for j in range(M):
        tmp.append(int(b[j]))
    B.append(tmp)
A =[[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i ==0 and 0<j<M-1:
            A[i+1][j]+=B[i][j]
            B[i+1][j-1]-=B[i][j]
            B[i+2][j]-=B[i][j]
            B[i+1][j+1]-=B[i][j]
            B[i][j]-=B[i][j]
        elif i ==N-1 and 0<j<M-1:
            A[i-1][j]+=B[i][j]
            B[i-1][j-1]-=B[i][j]
            B[i-2][j]-=B[i][j]
            B[i-1][j+1]-=B[i][j]
            B[i][j]-=B[i][j]
        elif 0<i<N-1 and j ==0:
            A[i][j+1]+=B[i][j]
            B[i][j+2]-=B[i][j]
            B[i-1][j+1]-=B[i][j]
            B[i+1][j+1]-=B[i][j]
            B[i][j]-=B[i][j]
        elif 0<i<N-1 and j ==M-1:
            A[i][j-1]+=B[i][j]
            B[i][j-2]-=B[i][j]
            B[i-1][j-1]-=B[i][j]
            B[i+1][j-1]-=B[i][j]
            B[i][j]-=B[i][j]
        else:
            if B[i][j]>0:
                A[i+1][j]+=B[i][j]
                B[i+1][j-1]-=B[i][j]
                B[i+2][j]-=B[i][j]
                B[i+1][j+1]-=B[i][j]
                B[i][j]-=B[i][j]

for i in range(N):
    ans = ''
    for j in range(M):
        ans+=str(A[i][j])
    print(ans)

