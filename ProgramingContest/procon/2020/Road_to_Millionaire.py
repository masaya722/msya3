n = int(input())
A = list(map(int, input().split()))

flag = False
stk = 0
ans = 1000
rest = 0
for i in range(n-1):
    if not flag:
        if A[i]<A[i+1]:
            flag = True
            stk=ans//A[i]
            rest = ans%A[i]
    if A[i]>=A[i+1]:
        flag = False
        if stk !=0:
            ans =stk*A[i]+rest
            stk =0
            rest = 0
    if i ==n-2:
        if stk !=0:
            ans=stk*A[i+1]+rest
print(ans)
