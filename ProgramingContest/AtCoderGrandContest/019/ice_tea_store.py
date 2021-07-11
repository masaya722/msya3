Q,H,S,D = map(int,input().split())
N = int(input())

one = min(4*Q,2*H,S)
D

if 2*one <=D:
    print(N*one)
else:
    if N%2 ==0:
        print(D*N//2)
    else:
        print(D*(N-1)//2 +one)