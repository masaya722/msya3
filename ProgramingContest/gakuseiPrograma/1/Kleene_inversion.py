N,K = map(int,input().split())
A= list(map(int,input().split()))

INF =10**9+7
count1 =0
count2 =0
for i in range(N):
    for j in range(i+1,N):
        if A[i] >A[j]:
            count1 +=1
for i in range(N):
    for j in range(N):
        if A[i]>A[j]:
            count2 +=1

ans = (count1*K+count2*K*(K-1)//2)%INF
print(ans)