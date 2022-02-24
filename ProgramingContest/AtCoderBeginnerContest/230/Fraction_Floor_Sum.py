import math
N = int(input())
harf = int(math.sqrt(N))
ans = 0
for k in range(1,N//(harf+1)+1):
    ans+=(N//k-N//(k+1))*k
for i in range(1,harf+1):
    ans+=N//i
print(ans)
