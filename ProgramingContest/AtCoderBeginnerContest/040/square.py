import math
N = int(input())
n = math.floor(math.sqrt(N))
count = 0
ans = N-n*n

for i in range(1,N+1):
    ans = min(ans,(N-(N//i*i))+abs(N//i-i))
print(ans)