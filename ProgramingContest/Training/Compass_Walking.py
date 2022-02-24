R,X,Y = map(int,input().split())
ans = 1
d2 = X**2+Y**2
while True:
    if R*R*ans*ans >=d2:
        break
    ans +=1
if ans ==1:
    if R*R !=d2:
        ans = 2

print(ans)
