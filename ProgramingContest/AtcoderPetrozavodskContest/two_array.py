from math import floor


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = sum(B)-sum(A)
if cnt<0:
    print('No')
else:
    one = cnt
    two = cnt
    for i in range(N):
        if A[i]>B[i]:
            one -=A[i]-B[i]
        elif A[i]<B[i]:
            if (B[i]-A[i])%2 ==1:
                two -=1
                one-=1
            two-=floor((B[i]-A[i])/2)
    if one<0 or two<0:
        print('No')
    else:
        if two*2==one:
            print('Yes')
        else:
            print('No')