from collections import Counter

N,M = map(int,input().split())
A = list(map(int,input().split()))
count = Counter(A)
if N//2<count.most_common()[0][1]:
    print(count.most_common()[0][0])
else:
    print("?")