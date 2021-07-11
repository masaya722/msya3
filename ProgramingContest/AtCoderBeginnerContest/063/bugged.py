N = int(input())

S = []
for i in range(N):
    S.append(int(input()))

S.sort()
ans = sum(S)

for s in S:
    if ans%10 == 0:
        if s%10 !=0:
            ans -=s
            break
if ans %10 ==0:
    ans=0

print(ans)
