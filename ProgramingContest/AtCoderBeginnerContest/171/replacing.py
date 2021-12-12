from collections import Counter
N = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)
count = Counter(A)
Q = int(input())
for i in range(Q):
    b, c = map(int, input().split())
    sum_A +=c*count[b]
    sum_A -=b*count[b]
    count[c]+=count[b]
    count[b] = 0
    print(sum_A)