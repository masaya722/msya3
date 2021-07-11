from bisect import bisect_left
N, M = map(int,input().split())
A = list(map(int, input().split()))
A.sort()

while M>0:
    a = A.pop()
    a = a//2
    M -=1
    idx = bisect_left(A,a)
    A.insert(idx,a)

print(sum(A))