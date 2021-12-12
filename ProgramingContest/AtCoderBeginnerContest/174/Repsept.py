k = int(input())
def f(x):
    return (10*x+7)%k
ans = 1
get_rem = f(0)
for i in range(k):
    if get_rem ==0:
        print(ans)
        exit()
    else:
        ans+=1
        get_rem = f(get_rem)
print(-1)