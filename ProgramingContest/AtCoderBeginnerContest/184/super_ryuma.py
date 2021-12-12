r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
start_plus =  r1+c1
start_minus = r1-c1

if r1 ==r2 and c1==c2:
    print(0)
elif start_plus ==r2+c2 or start_minus ==r2-c2 or abs(r1-r2)+abs(c1-c2)<=3:
    print(1)
else:
    if (start_plus)%2 ==(r2+c2)%2:
        print(2)
    elif abs(r1-r2)+abs(c1-c2)<=6:
        print(2)
    elif abs(start_plus-r2-c2)<=3 or abs(start_minus-r2+c2)<=3:
        print(2)
    else:
        print(3)