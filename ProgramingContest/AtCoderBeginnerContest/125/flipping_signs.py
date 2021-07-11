N = int(input())
A = list(map(int,input().split()))
count =0
for a in A:
    if a <0:
        count +=1
ans =0
if count %2==0:
    for a in A:
        ans+=abs(a)
else:
    minumun = 10**18
    for a in A:
        minumun = min(minumun,abs(a))
    for a in A:
        ans+=abs(a)
    ans-=minumun*2

print(ans)

