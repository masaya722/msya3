N = int(input())
ans= 0
for i in range(16):
    x = int('1'*(i+1))
    y = int('1'*i+'2')
    temp =1
    while N>=y:
        ans+=1*temp
        temp*=10
        x*=10
        y*=10
    if N>=x:
        ans+=N-x+1
print(ans)



