N,K = map(int,input().split())
A = list(map(int,input().split()))

def f(m):
    return sum([a-m+1 if a-m+1>0 else 0 for a in A])

high = max(A)+1
low = 0
while high-low>1:
    mid = (high+low)//2
    if f(mid)>K:
        low = mid
    else:
        high = mid
ans = 0
ans += sum([(a+high)*(a-high+1)//2 if a-high+1>0 else 0 for a in A])
K-=f(high)
if high>0:
    ans+=(high-1)*K
print(ans)
    

