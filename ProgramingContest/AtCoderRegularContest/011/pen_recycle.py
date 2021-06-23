m,n,N = map(int,input().split())

total =0
rem = 0
while 0<N:
    total += N
    a,b = divmod(N,m)
    rem +=b
    if a==0 and rem>=m:
        c,d = divmod(rem,m)
        N = c*n
        rem = d
    else:
        N = a*n
print(total)