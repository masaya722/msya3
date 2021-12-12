N,A,B = map(int,input().split())
if A>B:
    print(0)
    exit()
if N == 1 :
    if A !=B:
        print(0)
    else:
        print(1)
elif N==2:
    print(1)
else:
    minimum = (N-1)*A+B
    maximum = (N-1)*B+A
    print(maximum-minimum+1)
