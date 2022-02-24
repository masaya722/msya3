N = int(input())
A = []
B = []
ttl = []
for i in range(N):
    a,b = map(int,input().split())
    ttl.append(a+b)
    A.append(a)
    B.append(b)
same = min(ttl)
diff= 10**18
for i in range(N):
    for j in range(N):
        if i !=j:
            diff = min(diff,max(A[i],B[j]))
print(min(same,diff))

