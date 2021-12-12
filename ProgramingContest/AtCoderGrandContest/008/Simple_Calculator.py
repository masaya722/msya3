x,y = map(int,input().split())
if x ==y:
    print(0)
    exit()
if x ==0:
    if y<0:
        print(abs(y)+1)
    else:
        print(abs(y))
    exit()
if y ==0:
    if x<0:
        print(abs(x))
    else:
        print(abs(x)+1)
    exit()
if (x>=0 and y>=0) or (x<0 and y<0):
    if x<y:
        print(y-x)
    else:
        print(x-y+2)
elif(x>=0 and y<0) or (x<0 and y>=0):
    if abs(x)<abs(y):
        print(abs(y)-abs(x)+1)
    else:
        print(abs(x)-abs(y)+1)