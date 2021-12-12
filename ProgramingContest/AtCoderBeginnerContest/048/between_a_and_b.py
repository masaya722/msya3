a,b,x = map(int,input().split())

count = 0
if a %x ==0:
    count += b//x-a//x+1
elif a>x and a%x !=0:
    count += b//x-a//x
else:
    count +=b//x
print(count)