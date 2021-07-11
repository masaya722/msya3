from collections import Counter

N = int(input())
A = list(map(int, input().split()))
count = Counter(A)
diffs = []
for i in range(N):
    diff = (count[A[i]])*(count[A[i]]-1)//2 - (count[A[i]]-1)*(count[A[i]]-2)//2
    diffs.append(diff)

total = 0
for i in count.keys():
    total += (count[i])*(count[i]-1)//2

for df in diffs:
    print(total-df)