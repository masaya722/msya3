A= int(input())

def f(i):
    ans = 0
    base = i
    digit =1
    while i//10>0:
        i//=10
        ans+=(base**digit)*(i%10)
        digit+=1
    return ans+(base%10)
for i in range(10,10**4+1):
    if A == f(i):
        print(i)
        exit()
print(-1)
