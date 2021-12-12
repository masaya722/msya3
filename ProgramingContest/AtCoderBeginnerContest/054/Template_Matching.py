n,m = map(int,input().split())
A = []
B = []
for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())
for i in range(n):
    for j in range(n-m+1):
        cnt = 0
        if A[i][j:j+m] == B[0]:
            cnt+=1
            for k in range(1,m):
                if i+k <n:
                    if A[i+k][j:j+m] ==B[k]:
                        cnt+=1
        if cnt ==m:
            print('Yes')
            exit()
print('No')


