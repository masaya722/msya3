C = int(input())
N = []
M =[]
L =[]
for i in range(C):
    obj =list(map(int,input().split()))
    obj.sort()
    N.append(obj[0])
    M.append(obj[1])
    L.append(obj[2])

print(max(N)*max(M)*max(L))

