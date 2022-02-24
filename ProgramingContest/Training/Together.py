from collections import Counter

N = int(input())
A = list(map(int,input().split()))

a= Counter(A)
new_a = Counter(A)

for i,j in a.items():
    if i>0:
        new_a[i-1] += j
    new_a[i+1] += j

print(new_a.most_common()[0][1])