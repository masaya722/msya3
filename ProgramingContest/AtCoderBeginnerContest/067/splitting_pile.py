N  = int(input())
A = list(map(int,input().split()))
S= sum(A)
total = 0
ans = 10**18
count = 0
for a in A:
    count += 1
    if len(A)>count:
        total +=a
    ans = min(ans,abs(total*2-S))
print(ans)
