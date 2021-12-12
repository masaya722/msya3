L,R = map(int,input().split())
s =R//2019
for i in range(s+1):
    if L<=i*2019<=R:
        print(0)
        exit()
lmod = L%2019
rmod = R%2019
ans = 2019
for i in range(lmod,rmod+1):
    for j in range(i+1,rmod+1):
        ans = min(ans,i*j%2019)
print(ans)
