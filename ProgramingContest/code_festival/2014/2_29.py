A,B = map(int,input().split())
leave = B//4-B//100+B//400
born =A//4-A//100+A//400
if A ==B and A%4 ==0:
    if A%100==0 and A%400 !=0:
        print(0)
    else:
        print(1)
    exit()
if A%4 ==0 and A%100 !=0:
    print(leave-born+1)
else:
    print(leave-born)