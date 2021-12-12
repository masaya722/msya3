x,y,a,b = map(int,input().split())
ans = 0
while x*a<y or x+b<y:
    if x*a>x+b:
        if (y-x)%b ==0:
            ans+=(y-x)//b-1
        else:
            ans+=(y-x)//b
        break
    else:
        x*=a
        ans+=1
print(ans)