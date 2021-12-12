import math
N = int(input())

n = math.ceil(math.sqrt(N))

if N==1:
    print("Not Prime")
    exit()
if N==2:
    print("Prime")
    exit()
flag = True
for i in range(2,n+1):
    if N%i ==0:
        flag =False
if flag:
    print("Prime")
else:
    if N%5 !=0 and N%2 !=0:
        if sum(list(map(int,str(N).split())))%3 !=0:
            print("Prime")
            exit()
    print("Not Prime")
