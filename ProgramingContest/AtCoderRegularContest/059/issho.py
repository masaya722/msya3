N = int(input())
A = list(map(int,input().split()))

maxval = 200*N


ans = 10**18
for i in range(-100,101):
    ans1 = 0
    for j in range(len(A)):
        ans1 +=(A[j]-i)**2
    
    ans = min(ans1,ans)

print(ans)
