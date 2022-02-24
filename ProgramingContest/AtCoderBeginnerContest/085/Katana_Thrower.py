n, h = map(int, input().split())
throw = []
max_a = 0
for i in range(n):
    a, b = map(int, input().split())
    max_a = max(a, max_a)
    throw.append(b)
throw.sort(reverse=True)
ans= 10**18
if h%max_a==0:
    ans = h//max_a
else:
    ans= h//max_a+1
tmp= h
for i in range(n):
    tmp-=throw[i]
    if tmp>0:
        if tmp%max_a==0:
            ans = min(ans,tmp//max_a+i+1)
        else:
            ans = min(ans,tmp//max_a+i+2)
    else:
        ans = min(ans,i+1)
print(ans)
