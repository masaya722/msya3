R,X,Y = map(int,input().split())
d2 = X**2+Y**2
ans = 1
while True:
    if R*R*ans*ans >=d2:
        break
    ans+=1
if ans ==1:
    if R*R !=d2:
        ans = 2
print(ans)