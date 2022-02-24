from bisect import bisect_left

N,M = map(int,input().split())
x,y = map(int,input().split())
A = list(map(int,input().split()))
B =list(map(int,input().split()))

now = A[0]+x
ans =0
flag = False
while now <=B[M-1]:
    if not flag:
        flag = True
        idx = bisect_left(B,now)
        if idx !=M:
            now = B[idx]+y
            ans+=1
        else:
            break
    else:
        flag = False
        idx = bisect_left(A,now)
        if idx !=N:
            now = A[idx]+x
        else:
            break
print(ans)