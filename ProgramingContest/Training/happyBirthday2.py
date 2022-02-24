N = int(input())
A = list(map(int,input().split()))
N = min(N,8)
bits = 1 <<N
s = 1

st = [0 for _ in range(200)]

def output(s):
    i = 1
    a = []
    while s:
        if s &1:
            a.append(i)
        s >>= 1
        i+=1
    print(len(a),end=" ")
    for j in a:
        print(j,end=" ")
    print()

while s <bits:
    x = 0
    for i in range(N):
        if s>>i &1:
            x = (x+A[i])%200
    if st[x] == 0:
        st[x] = s
    else:
        print("Yes")
        output(s)
        output(st[x])
        exit()
    s+=1

print("No")