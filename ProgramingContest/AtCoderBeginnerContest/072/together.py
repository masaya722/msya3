from collections import Counter

N = int(input())
A = list(map(int,input().split()))
a = Counter(A)
new_a = Counter(A)
for key,val in a.items():
    if key != 0:
        new_a[key-1] +=val
    new_a[key+1] += val

print(new_a.most_common()[0][1])