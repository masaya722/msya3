na, nb = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.extend(B)
print((na+nb-len(set(A)))/len(set(A)))