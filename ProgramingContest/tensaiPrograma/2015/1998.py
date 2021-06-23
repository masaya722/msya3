A = [100,100,200]
for i in range(20):
    A.append(A[-1]+A[-2]+A[-3])

print(A[19])