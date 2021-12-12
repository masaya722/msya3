N = int(input())
ans = 10**12+1
flag = False
for i in range(2,10**6+1):
    if N%i ==0:
        flag = True
        ans =min(ans,i+N//i)
if flag:
    print(ans-2)
else:
    print(N-1)