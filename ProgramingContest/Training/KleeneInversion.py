N,K = map(int,input().split())
A = list(map(int,input().split()))
count1 =0
for i in range(N):
    for j in range(i+1,N):
        if A[i] >A[j]:
            count1+=1

count2 = 0
for i in range(N):
    for j in range(N):
        if A[i]>A[j]:
            count2+=1

ans = (K*count1+K*(K-1)//2*count2)%(10**9+7)
print(ans)