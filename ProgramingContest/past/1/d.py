from collections import defaultdict
N = int(input())
A = defaultdict(int)
for i in range(N):
    A[int(input())]+=1
bef = 0
aft = 0
for i in range(1,N+1):
    if A[i] ==0:
        bef= i
    if A[i]==2:
        aft = i
if bef !=0 and aft != 0:
    print(aft,bef)
else:
    print('Correct')