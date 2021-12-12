N = int(input())
A = list(map(int,input().split()))
ans= 0
cnt = 1
for i in range(N-1):
    if A[i]<A[i+1]:
        cnt+=1
        if i ==N-2:
            ans+=(cnt+1)*cnt//2
    else:
        if cnt>=2:
            ans += (cnt+1)*cnt//2
            cnt =1
            if i ==N-2:
                ans+=1
        else:
            ans += 1
            if i ==N-2:
                ans+=1
print(ans)