N = int(input())
S = input()
cnt = 0
ans = 0
for i in range(N-1):
    if S[i] ==S[i+1]:
        cnt+=1
        if i ==N-2:
            cnt+=1
            ans +=cnt*(cnt-1)//2
    else:
        if cnt !=0:
            cnt+=1
        ans+=cnt*(cnt-1)//2
        cnt = 0 
print(ans)
