from bisect import bisect_left
n,x = map(int,input().split())
A= list(map(int,input().split()))
idx = bisect_left(A,x)
if idx<n:
    rest = A[idx]-x
    