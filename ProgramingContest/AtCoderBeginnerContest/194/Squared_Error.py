N = int(input())
A = list(map(int,input().split()))
suma = []
temp = 0
for a in A:
    temp+=a
    suma.append(temp)
suma.pop()
powa = []
for a in A:
    powa.append((a**2)*(N-1))
minus = []
for i,a in enumerate(A):
    if i==0:
        continue
    minus.append(2*suma[i-1]*a)
print(sum(powa)-sum(minus))