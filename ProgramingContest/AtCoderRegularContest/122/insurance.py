N = int(input())
A = list(map(int,input().split()))
def f(x):
    return N*x +sum(A)- sum(min(A[i],2*x) for i in range(N)) 
ok = max(A)
ng = 0
while ok -ng>10**-6:
    mid_left = ok/3+ng*2/3
    mid_right = ok*2/3+ng/3
    if f(mid_left)>=f(mid_right):
        ng = mid_left
    else:
        ok = mid_right
print(f(ok)/N)