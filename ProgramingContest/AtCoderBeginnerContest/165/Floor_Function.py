A,B,N = map(int,input().split())

if B ==1:
    print((A*N)//B-A*(N//B))
else:
    if N>=B:
        a = (A*N)//B-A*(N//B)
        b = (A*(B-1))//B - A*((B-1)//B)
        ans = max(a,b)
        print(ans)
    else:
        print((A*N)//B - A*(N//B))